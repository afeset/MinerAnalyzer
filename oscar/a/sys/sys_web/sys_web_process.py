import os
import os.path
import email.utils  # for formatdate
import parameters
import subprocess
import platform
import glob
import stat
import traceback
import random
import string

# increase  max number of arguments to pass our big init function
__pychecker__ = "maxargs=15"
RRDTOOL_PATH_RLATIVE_TO_CONST_DIR = "../rrdtool/bin"

class CallException(Exception):
    """This class is used to raise exception when process execution return non zero error code"""
    def __init__(self, command, error):
        self.myCommand = command
        self.myError = error
    def __str__(self):
        return "Command '%s' failed - return code: %d" % (" ".join(self.myCommand), self.myError)

# === SysWebProcess ===================================================================================================
class SysWebProcess():

    # --- init --------------------------------------------------------------------------------------------------------
    def init(self, constDir, sysVarDir, sysRunDir, dataVarDir, 
             mngWebClientAppConstDir, topperReportsDir, systemStatusDir, siteDataConstDir,
             statsWebAppConstDir, statsDbDir, statsRrdDir,
             contentDir, contentMetaDir):

        self.constDir   = constDir
        self.sysVarDir  = sysVarDir
        self.sysRunDir  = sysRunDir
        self.dataVarDir = dataVarDir
        self.mngWebClientAppConstDir = mngWebClientAppConstDir
        self.topperReportsDir        = topperReportsDir
        self.systemStatusDir         = systemStatusDir
        self.siteDataConstDir        = siteDataConstDir
        self.statsWebAppConstDir     = statsWebAppConstDir
        self.statsDbDir              = statsDbDir
        self.statsRrdDir             = statsRrdDir
        self.contentDir              = contentDir
        self.contentMetaDir          = contentMetaDir

        # Calc the paths 
        self._calcPaths();

        # Set httpd executable & command base
        self.httpdExecutable  = "/usr/sbin/httpd"
        self.httpdCommandBase = [self.httpdExecutable, '-f', os.path.abspath(self.httpdConfFile)]
        self.mySecretKey = None

    # --- setListenParams ---------------------------------------------------------------------------------------------
    def setListenParams(self, listenAddressesHTTP, listenAddressesHTTPS):
        self.myListenAddressesHTTP  = listenAddressesHTTP
        self.myListenAddressesHTTPS = listenAddressesHTTPS

    # --- set application specific params
    def setParams(self, sysWebParamsDict, mngWebClientAppParamsDict, statsWebAppParamsDict, techWebAppParamsDict, uxModuleParamsDict):
        self.sysWebParams          = parameters.Parameters(dictionary=sysWebParamsDict)
        self.mngWebClientAppParams = parameters.Parameters(dirName=self.mngDataDir, dictionary=mngWebClientAppParamsDict)
        self.statsWebAppParams     = parameters.Parameters(dirName=self.statsWebDataDir, dictionary=statsWebAppParamsDict)
        self.techWebAppParams      = parameters.Parameters(dirName=self.techWebDataDir, dictionary=techWebAppParamsDict)
        self.uxModuleParams        = parameters.Parameters(fileName=os.path.join(self.mngDataDir, "ux-parameters.json"), dictionary=uxModuleParamsDict)
        self.provideSharedParameters()

    # --- Provides database configuration settings to sys-web django applications
    def provideSharedParameters(self):
        # currently we do it in explicit hardcoded manner
        self.databaseName = os.path.join(self.mngDbDir, "database.sqlite")
        secretKey = self.getSecretKey()
        self.mngWebClientAppParams.setParameter("database/name", self.databaseName)
        self.mngWebClientAppParams.setParameter("database/engine", "django.db.backends.sqlite3")
        self.mngWebClientAppParams.setParameter("secret_key", secretKey)
        self.statsWebAppParams.setParameter("database/name", self.databaseName)
        self.statsWebAppParams.setParameter("database/engine", "django.db.backends.sqlite3")
        self.statsWebAppParams.setParameter("secret_key", secretKey)
        self.techWebAppParams.setParameter("database/name", self.databaseName)
        self.techWebAppParams.setParameter("database/engine", "django.db.backends.sqlite3")
        self.techWebAppParams.setParameter("secret_key", secretKey)

    # --- install -----------------------------------------------------------------------------------------------------
    def install(self):
        error = None
        cmd   = None
        return (error, cmd)

    # --- start -------------------------------------------------------------------------------------------------------
    def start(self):

        # Create sys web dirs and files
        self._createDirsAndFiles()

        # Set start command 
        cmd   = self.httpdCommandBase   
        envToAppend = {"SYS_WEB_APPLICATIONS_BASE_DIR": self.applicationsBaseDir}
        error = None
        return (error, cmd, envToAppend)      

    # --- stop --------------------------------------------------------------------------------------------------------
    def stop(self):

        # Set stop command 
        cmd   = self.httpdCommandBase + ['-k', 'stop']  
        error = None
        return (error, cmd)

    # --- update config -----------------------------------------------------------------------------------------------
    def updateConfiguration(self):

        # Create sys web dirs and files
        self._createDirsAndFiles()

        # Set update command 
        cmd   = self.httpdCommandBase + ['-k', 'graceful']  
        error = None
        return (error, cmd)

    # --- getLogDirs --------------------------------------------------------------------------------------------------
    def getLogDirs(self):

        # Returns a list of directories containing log files 
        return self.logDirs.values()

    # --- getLogDir --------------------------------------------------------------------------------------------------
    def getLogDir(self, entity):
        dirPerEntity = self.getLogDirsPerEntity()
        if entity in dirPerEntity:
            return dirPerEntity[entity]
        return None

    def getLogDirsPerEntity (self):
        return self.logDirs
        

    # --- _safeMkdir --------------------------------------------------------------------------------------------------
    def _safeMkdir(self, dir):
        # Don't remake dir if alreay exists
        if os.path.isdir(dir):
            return

        # Create the dir. Set umask to zero, creating 777 dirs, allowing apache user to write them
        oldUmask = os.umask(0) 
        os.mkdir(dir)
        os.umask(oldUmask)

    # --- _safeSymlink ------------------------------------------------------------------------------------------------
    def _safeSymlink(self, source, linkName):

        # If linkName already exists then delete it
        if os.path.lexists(linkName):
            os.remove(linkName)

        # Create the link
        os.symlink(source, linkName)

    # --- _calcPaths --------------------------------------------------------------------------------------------------
    def _calcPaths(self):

        # General
        self.logsDir       = os.path.join(self.dataVarDir,"log")
        self.pidDir        = os.path.join(self.sysRunDir,"pid")
        self.dbDir         = os.path.join(self.sysVarDir,"db")

        self.logDirs = {}
          
        # httpd    
        self.httpdDirLevel = "httpd"
        self.httpdConstDir = os.path.join(self.constDir, self.httpdDirLevel)
        self.httpdDataDir  = os.path.join(self.sysVarDir,  self.httpdDirLevel)
        #self.httpdVarDir   = os.path.join(self.varDir,   self.httpdDirLevel)
        #self.httpdRamDir   = os.path.join(self.ramDir,   self.httpdDirLevel)
        self.httpdServerRootDir = os.path.join(self.httpdDataDir,       "server_root")
        self.httpdConfDir       = os.path.join(self.httpdServerRootDir, "conf")
        self.httpdConfFile      = os.path.join(self.httpdConfDir,       "httpd.conf")
        self.httpdLogsDir       = os.path.join(self.logsDir,             self.httpdDirLevel)
        self.logDirs["httpd"] = self.httpdLogsDir
        self.httpdPidFile       = os.path.join(self.pidDir,             "pidFile")
        self.httpdSSLDir        = os.path.join(self.httpdServerRootDir, "ssl")
        self.httpdSSLPrivateKey = os.path.join(self.httpdSSLDir,        "privatekey.pem")
        self.httpdSSLCertificate= os.path.join(self.httpdSSLDir,        "certificate.pem")

        # mng web client app
        self.mngWebClientAppStaticDir   = os.path.normpath( os.path.join(self.mngWebClientAppConstDir, "static") )
        self.mngWebClientAppTemplateDir = os.path.normpath( os.path.join(self.mngWebClientAppConstDir, "template") )

        # site data
        self.siteDataStaticDir   = os.path.normpath( os.path.join(self.siteDataConstDir, "static") )

        self.applicationsBaseDir = os.path.join(self.sysRunDir)

        self.mngDirLevel    = "mng"
        self.mngDataDir     = os.path.join(self.applicationsBaseDir,    self.mngDirLevel)
        self.mngTemplateDir = os.path.join(self.mngDataDir, "template")
        self.mngLogsDir     = os.path.join(self.logsDir,    self.mngDirLevel)
        self.logDirs["mng-web"] = self.mngLogsDir
        self.mngDbDir       = os.path.join(self.dbDir, self.mngDirLevel)

        # Stats web app
        self.statsWebAppStaticDir   = os.path.normpath( os.path.join(self.statsWebAppConstDir, "static") )
        self.statsWebAppTemplateDir = os.path.normpath( os.path.join(self.statsWebAppConstDir, "template") )
        self.statsDirLevel    = "stats"
        self.statsWebDataDir  = os.path.join(self.applicationsBaseDir,    self.statsDirLevel)
        self.statsTemplateDir = os.path.join(self.statsWebDataDir, "template")
        self.statsLogsDir     = os.path.join(self.logsDir,    self.statsDirLevel)
        self.logDirs["stats-web"] = self.statsLogsDir

        # Tech web app
        self.techDirLevel    = "tech"
        self.techWebDataDir  = os.path.join(self.applicationsBaseDir,    self.techDirLevel)
        self.techWebDataContentDir  = os.path.join(self.techWebDataDir,  "content")
        self.techLogsDir     = os.path.join(self.logsDir,    "%s-web-app" % self.techDirLevel)
        self.logDirs["tech-web"] = self.techLogsDir
        #import pprint 
        #pprint.pprint (self.__dict__)

    # --- _createDirsAndFiles -----------------------------------------------------------------------------------------
    def _createDirsAndFiles(self):

        # Create general dirs
        self._safeMkdir(self.logsDir)
        self._safeMkdir(self.pidDir)
                  
        # Create the httpd dirs
        self._safeMkdir(self.httpdDataDir)
        #self._safeMkdir(self.httpdVarDir)
        #self._safeMkdir(self.httpdRamDir)
        self._safeMkdir(self.httpdServerRootDir)
        self._safeMkdir(self.applicationsBaseDir)

        # Create server root modules slink
        self._safeSymlink("/usr/lib64/httpd/modules", os.path.join(self.httpdServerRootDir, "modules") )

        # Create server root const slink
        constRelPath = os.path.relpath(self.httpdConstDir, self.httpdServerRootDir)
        self._safeSymlink( constRelPath, os.path.join(self.httpdServerRootDir, "const") ) 
    
        # Create server root log dir and its symlink
        self._safeMkdir(self.httpdLogsDir)
        logsRelPath = os.path.relpath(self.httpdLogsDir, self.httpdServerRootDir)
        self._safeSymlink( logsRelPath, os.path.join(self.httpdServerRootDir, "logs") ) 
        
        # Create server root pid dir and its symlink
        pidRelPath = os.path.relpath(self.pidDir, self.httpdServerRootDir)
        self._safeSymlink( pidRelPath, os.path.join(self.httpdServerRootDir, "pid") ) 
     
        # Create the config dir and file
        self._safeMkdir(self.httpdConfDir)

        self.generateCertificateAndPrivateKey()
        self._safeMkdir(self.dbDir)
        self._createMngWebDirsAndFiles()
        self._createStatsWebDirsAndFiles()
        self._createTechWebDirsAndFiles()

        # create Authentication data
        if not os.path.isfile(self.databaseName):
            self.createAuthenticationDatabase()
            self.createDefaultUsers()
            self.fixMngWebFilesPermissions()

        confFileInString = self._getConfigFileInString()
        confFile       = open(self.httpdConfFile, "w")
        confFile.write ( confFileInString )
        confFile.close();

    def _createMngWebDirsAndFiles(self):
        # Managment web
        self._safeMkdir(self.mngDataDir)
        self._safeMkdir(self.mngTemplateDir)
        self._safeMkdir(self.mngLogsDir)
        self._safeMkdir(self.mngDbDir)

        logsRelPath = os.path.relpath(self.mngLogsDir, self.mngDataDir)
        self._safeSymlink( logsRelPath, os.path.join(self.mngDataDir, "logs") ) 

        # Mng web - link to client app  
        templateRelPath = os.path.relpath(self.mngWebClientAppTemplateDir, self.mngTemplateDir)
        self._safeSymlink( templateRelPath, os.path.join(self.mngTemplateDir, "mng_web_client_app") ) 

        # Mng web - link to topper reports dir
        topperReportsRelPath = os.path.relpath(self.topperReportsDir, self.mngDataDir)
        self._safeSymlink( topperReportsRelPath, os.path.join(self.mngDataDir, "topper_reports") ) 

        # Mng web - link to system status dir
        systemStatusRelPath = os.path.relpath(self.systemStatusDir, self.mngDataDir)
        self._safeSymlink( systemStatusRelPath, os.path.join(self.mngDataDir, "sys_status") ) 

        # Soft link to SmartXLS jar
        SX_jarRelPath = os.path.relpath(os.path.join(self.constDir, "..", "jar", "SX.jar"), self.mngDataDir)
        self._safeSymlink( SX_jarRelPath, os.path.join(self.mngDataDir, "SX.jar") )

        # Soft link to Export templates
        exportTemplatesRelPath = os.path.relpath(os.path.join(self.constDir, "..", "mng_web_export"), self.mngDataDir)
        self._safeSymlink(exportTemplatesRelPath, os.path.join(self.mngDataDir, "export_templates") )

        # temp folder will contain temporary files created during export
        # since root folder is in /run/... hierarchy then temp will in run as well
        # and thus will be removed at each system restart
        self._safeMkdir(os.path.join(self.mngDataDir, "temp"))

        # Link to db dir which contains all persistent files
        mngDbDirRelPath = os.path.relpath(self.mngDbDir, self.mngDataDir)
        self._safeSymlink(mngDbDirRelPath, os.path.join(self.mngDataDir, "db") )
        self.saveSecretKey()

        self.mngWebClientAppParams.save()
        self.uxModuleParams.save()

    def _createStatsWebDirsAndFiles(self):
        # Stats web
        self._safeMkdir(self.statsWebDataDir)
        innerDataDir = os.path.join(self.statsWebDataDir, "data")
        self._safeMkdir(innerDataDir)
        self._safeMkdir(self.statsLogsDir)
        logsRelPath = os.path.relpath(self.statsLogsDir, self.statsWebDataDir)
        self._safeSymlink( logsRelPath, os.path.join(self.statsWebDataDir, "logs") ) 

        # Currently there is no templetes in stats but we expect to be
        # templateRelPath = os.path.relpath(self.statsWebAppTemplateDir, self.statsTemplateDir)
        # self._safeSymlink( templateRelPath, self.statsTemplateDir ) 

        # link to stats data dir
        statsDbDirRelPath = os.path.relpath(self.statsDbDir, innerDataDir)        
        self._safeSymlink( statsDbDirRelPath, os.path.join(innerDataDir, "db")) 

        statsRrdDirRelPath = os.path.relpath(self.statsRrdDir, innerDataDir)        
        self._safeSymlink(statsRrdDirRelPath, os.path.join(innerDataDir, "rrd")) 

        #link to rrdtool dir 
        statsRrdToolRelPath = os.path.relpath(os.path.join(self.constDir,RRDTOOL_PATH_RLATIVE_TO_CONST_DIR), self.statsWebDataDir)
        self._safeSymlink(statsRrdToolRelPath, os.path.join(self.statsWebDataDir, "rrdtool")) 

        self.statsWebAppParams.save()

    def _createTechWebDirsAndFiles(self):
        # Technitian web application
        self._safeMkdir(self.techWebDataDir)
        self._safeMkdir(self.techWebDataContentDir)
        self._safeMkdir(self.techLogsDir)
        logsRelPath = os.path.relpath(self.techLogsDir, self.techWebDataDir)
        self._safeSymlink( logsRelPath, os.path.join(self.techWebDataDir, "logs") ) 
        contentRelPath = os.path.relpath(self.contentDir, self.techWebDataContentDir)
        self._safeSymlink(contentRelPath, os.path.join(self.techWebDataContentDir, "media"))
        contentMetaRelPath = os.path.relpath(self.contentMetaDir, self.techWebDataContentDir)
        self._safeSymlink(contentMetaRelPath, os.path.join(self.techWebDataContentDir, "meta"))
        self.techWebAppParams.save()

    # --- _getConfigFileInString --------------------------------------------------------------------------------------
    def _getConfigFileInString(self):

        # Build config vars. Begin with all object vars and some more
        configVars = self.__dict__.copy();
        configVars['currentDate'] = email.utils.formatdate(timeval=None, localtime=True)
    
        configVars['listenAddressesText'] = self.getListenAddresses()

        # parameter names coming from ini script are always in lower case!
        configVars['StartServers']        = self.sysWebParams.getIntParameter("httpd-startservers", 5)
        configVars['MinSpareServers']     = self.sysWebParams.getIntParameter("httpd-minspareservers", 4)
        configVars['MaxSpareServers']     = self.sysWebParams.getIntParameter("httpd-maxspareservers", 8)
        configVars['MaxClients']          = self.sysWebParams.getIntParameter("httpd-maxclients", 16)
        # ServerLimit is the apache lifetime limit on the number of MaxClients
        configVars['ServerLimit']         = self.sysWebParams.getIntParameter("httpd-serverlimit", 128)
        configVars['MaxRequestsPerChild'] = self.sysWebParams.getIntParameter("httpd-maxrequestsperchild", 100)
        # Embedded config vars into config text

        if self.mngWebClientAppParams.getBooleanParameter("enable-django-admin", False):
            configVars['djangoAdminRule'] = "RewriteRule ^/m/static/admin/(.*) %s/../ext/lib/python2.6/site-packages/django/contrib/admin/media/$1" % self.constDir
        else:
            configVars['djangoAdminRule'] = ""

        configVars['deflateRule'] = self.getDeflateConfiguration()
        configVars['cacheRules'] = self.getCacheRules()

        s = """# %(httpdConfFile)s created at %(currentDate)s. 


# --- httpd general configuration


ServerRoot %(httpdServerRootDir)s

Include conf/start*.conf
PidFile pid/pidFile
%(listenAddressesText)s

<IfModule prefork.c>
StartServers         %(StartServers)s
MinSpareServers      %(MinSpareServers)s
MaxSpareServers      %(MaxSpareServers)s
ServerLimit          %(ServerLimit)s
MaxClients           %(MaxClients)s
MaxRequestsPerChild  %(MaxRequestsPerChild)s
</IfModule>

Include conf/before*.conf
Include const/conf/httpd_core.conf
Include conf/after*.conf
""" % configVars
        if not self.sysWebParams.getBooleanParameter("disable-http", False):
            s += self.getHttpConfiguration(configVars)
        if not self.sysWebParams.getBooleanParameter("disable-https", False) and self.isCertificateAvailable:
            s += self.getHttpsConfiguration(configVars)

        apacheUser = self.sysWebParams.getParameter("apache-user", None)
        if apacheUser is not None:
            s += "User %s\n" % apacheUser
        apacheGroup = self.sysWebParams.getParameter("apache-group", None)
        if apacheGroup is not None:
            s += "Group %s\n" % apacheGroup
  
        # configure logging
        if self.sysWebParams.getBooleanParameter("enable-access-log", True):
            logFormat = self.sysWebParams.getParameter("access-log-format", "qwiltpredefined")
            s += "CustomLog logs/access_log %s\n" % logFormat
        s += "Include conf/end*.conf\n"
        # Mark the end 
        s += "# --- End\n"
 
        return s;

    def getVirtualHostConfiguration(self, configVars):
        """
        Returns shared content of VirtualHost directive
        This is used to create http and https configurations
        """
        return """
# Use hostname provided by client in redirects
UseCanonicalName Off

RewriteEngine On
<Directory wsgi>
   Order deny,allow
   Allow from all
</Directory>

<IfModule mod_mime_magic.c>
    MIMEMagicFile const/conf/magic
</IfModule>

%(cacheRules)s

%(deflateRule)s

# Redirect home page
RewriteRule ^/$         m/client/system/  [R=301]

# --- mng web configuration

WSGIScriptAlias /wsgi-mng %(httpdServerRootDir)s/const/wsgi/mng.wsgi

%(djangoAdminRule)s
RewriteRule ^/m/([^/]*)/static/site/(.*)  %(siteDataStaticDir)s/$2 [L]
RewriteRule ^/m/([^/]*)/static/(.*)       %(mngWebClientAppStaticDir)s/$2 [L]
RewriteRule ^/m/([^/]*)/(.*)              /wsgi-mng/m/$1/$2  [PT,L]

<Directory %(mngWebClientAppStaticDir)s>
   Order deny,allow
   Allow from all
</Directory>


# --- Stats web configuration

WSGIScriptAlias /wsgi-stats %(httpdServerRootDir)s/const/wsgi/stats.wsgi

RewriteRule ^/stats[/]*$                  /stats/static/site/index.htm [R,L]
RewriteRule ^/stats/static/(.*)       %(statsWebAppStaticDir)s/$1 [L]
RewriteRule ^/stats/(.*)              /wsgi-stats/$1  [PT,L]

# --- Technitian web configuration

## WSGIScriptAlias /wsgi-tech %(httpdServerRootDir)s/const/wsgi/tech.wsgi

## RewriteRule ^/tech/(.*)$              /wsgi-tech/tech/$1  [PT,L]

""" % configVars

    def invokeMngDjangoAdmin(self, commandArgs):
        """This function is used to invoke general django-admin commands for mng web application"""
        env = os.environ.copy()
        env['A_MNG_WEB_ROOT_DIR'] = self.mngDataDir
        env['DJANGO_SETTINGS_MODULE'] = "a.sys.sys_web.mng.django_app.settings"
        pathListSeparator = ";" if platform.system()=='Windows' else ":"
        if env['PYTHONPATH']:
            pythonpath = pathListSeparator + env['PYTHONPATH']
        else:
            pythonpath = ""
        env['PYTHONPATH'] = os.path.join(self.constDir, "..", "python") + pathListSeparator + os.path.join(self.constDir, "..", "ext", "lib", "python2.6", "site-packages") + pythonpath
        djangoAdminPath = os.path.join(self.constDir, "../ext/lib/python2.6/site-packages/django/bin/django-admin.py")

        command = ["/usr/local/bin/python2.6", djangoAdminPath]
        command.extend(commandArgs)
        #print "==== Dumping environment:"
        #subprocess.call("env", env=env)
        #print "Django admin command: '%s'" % " ".join(command)
        result = subprocess.call(command, env=env)
        #print "Django command end"
        return result
        
    def setPasswordInteractively(self, user):
        self.invokeMngDjangoAdmin(["changepassword", user])
        print ""

    def createAuthenticationDatabase(self):
        # create database
        self.invokeMngDjangoAdmin(["syncdb", "--noinput"])

    def createDefaultUsers(self):
        # create superuser
        # password for administrator should be set manually
        self.invokeMngDjangoAdmin(["createsuperuser", "--username", "administrator", "--email", "administrator@qwilt.com", "--noinput"])
        # Create regular users
        self.invokeMngDjangoAdmin(["createuser", "--username", "viewer", "--email", "viewer@qwilt.com", "--password", "viewer", "--noinput"])

    def fixMngWebFilesPermissions(self):
        """Fixes permission of user datables and log files created during sys_web initialization phase"""
        # The fix is only relevant if apache user is different from the user running the oscar
        apacheUser = self.sysWebParams.getParameter("apache-user", None)
        if not apacheUser:
            return
        filesToFix = [self.databaseName]
        filesToFix.extend(glob.glob(os.path.join(self.mngLogsDir, "*.log")))
        for f in filesToFix:
            os.chmod(f, stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH|stat.S_IWUSR|stat.S_IWGRP|stat.S_IWOTH) # 666


    def getDeflateConfiguration(self):
        if self.sysWebParams.getBooleanParameter("disable-compression", False):
            return ""
        else:
            return """
<Location />
# Insert filter
SetOutputFilter DEFLATE

# Don't compress images and fonts
SetEnvIfNoCase Request_URI \
\.(?:gif|jpe?g|png|ico|eot|ttf|)$ no-gzip dont-vary

SetEnvIfNoCase Request_URI \
^/tech/content/ no-gzip dont-vary

# Make sure proxies don't deliver the wrong content
Header append Vary User-Agent env=!dont-vary
</Location>

"""

    def generateCertificateAndPrivateKey(self):

        if self.sysWebParams.getBooleanParameter("disable-https", False):
            self.isCertificateAvailable = False
            return
        self._safeMkdir(self.httpdSSLDir)

        if not os.path.isfile(self.httpdSSLPrivateKey) or not os.path.isfile(self.httpdSSLCertificate):
            try:
                # Create private key
                # update umask so that private key will be created with the no read by others
                oldUmask = os.umask(077) 
                command = ["/usr/bin/openssl", "genrsa", "-out", self.httpdSSLPrivateKey, "2048"]
                result = subprocess.call(command)
                os.umask(oldUmask)
                if result != 0:
                    raise CallException(command, result)
    
                # create configuration file for extension options
                sslConfFileName = os.path.join(self.httpdSSLDir, "conf")
                sslConfFile = open(sslConfFileName, "w")
                sslConfFile.write("""
[req]
prompt=no
distinguished_name = req_distinguished_name
x509_extensions = extensions
[extensions]
basicConstraints = CA:false
[req_distinguished_name]
C=US
ST=California
L=Redwood
O=Qwilt Ltd.
OU=Tech Dept.
CN=Qwilt-QB-100
""")
                sslConfFile.close()
                # Create certificate
                command = ["/usr/bin/openssl", "req", "-new", "-x509", "-key", self.httpdSSLPrivateKey, "-out", self.httpdSSLCertificate, "-config", sslConfFileName, "-days", str(365*4)]
                result = subprocess.call(command)
                if result != 0:
                    raise CallException(command, result)
            except:
                print "====Creation of Private Key and/or Certificate failed========"
                traceback.print_exc()
                self.isCertificateAvailable = False
            else:
                self.isCertificateAvailable = True
        else:
            self.isCertificateAvailable = True

    def getVirtualHostAddresses(self, listenAddresses):
        """Returns list of addresses for VirtualHost directive"""
        vhostAddresses = []
        # if we listen on 0.0.0.0:XXX we need to replace it to _default_:XXX
        for address in listenAddresses:
            hostAndPort = address.split(':')
            if not hostAndPort[0] or hostAndPort[0]=="0.0.0.0":
                hostAndPort[0] = "_default_"
            vhostAddresses.append(":".join(hostAndPort))
        return " ".join(vhostAddresses)

    def getHttpConfiguration(self, configVars):
        """Returns Http VirtualHost configuration"""
        configVars['httpVirtualHostAddresses'] = self.getVirtualHostAddresses(self.myListenAddressesHTTP)
        configuration  = "<VirtualHost %(httpVirtualHostAddresses)s>\n" % configVars
        configuration += self.getVirtualHostConfiguration(configVars)
        configuration += "</VirtualHost>\n"
        return configuration

    def getHttpsConfiguration(self, configVars):
        """Returns Https VirtualHost configuration"""
        configuration = """
SSLCertificateFile %s
SSLCertificateKeyFile %s

SSLProtocol all -SSLv2
""" % (self.httpdSSLCertificate,  self.httpdSSLPrivateKey)
        configVars['httpsVirtualHostAddresses'] = self.getVirtualHostAddresses(self.myListenAddressesHTTPS)
        configuration += """
<VirtualHost %(httpsVirtualHostAddresses)s>
SSLEngine on
SetEnvIf User-Agent ".*MSIE.*" nokeepalive ssl-unclean-shutdown
""" % configVars
        configuration += self.getVirtualHostConfiguration(configVars)
        configuration += "</VirtualHost>\n"
        return configuration

    def getListenAddresses(self):
        """Returns text containing Listen statements"""
        listenAddressesText = ""
        if not self.sysWebParams.getBooleanParameter("disable-http", False):
            for address in self.myListenAddressesHTTP:
                listenAddressesText += "Listen %s\n" % ( address )
        if not self.sysWebParams.getBooleanParameter("disable-https", False):
            for address in self.myListenAddressesHTTPS:
                listenAddressesText += "Listen %s\n" % ( address )
        return listenAddressesText

    def getListeningAddressesText(self):
        """Returns text for status line"""
        listenAddresses = []
        if not self.sysWebParams.getBooleanParameter("disable-http", False):
            for address in self.myListenAddressesHTTP:
                listenAddresses.append("http://%s" % ( address ))
        if not self.sysWebParams.getBooleanParameter("disable-https", False):
            for address in self.myListenAddressesHTTPS:
                listenAddresses.append("https://%s" % ( address ))
        return ", ".join(listenAddresses)

    def getCacheRules(self):
        if self.sysWebParams.getBooleanParameter("disable-cache-rules", False):
            return ""
        else:
            return """
# Define cache rules for hashed files
ExpiresActive On
<Directory %s>
<Files "*-MD5-*">
ExpiresDefault "now plus 1 month"
</Files>
</Directory>

<Directory %s>
ExpiresByType image/* "now plus 1 week"
</Directory>

<Directory %s>
<Files "*">
ExpiresDefault "now plus 5 minutes"
</Files>
</Directory>

""" % (self.mngWebClientAppStaticDir, self.siteDataStaticDir, self.statsWebAppStaticDir)

    def getSecretKey(self):
        """
        Returns secret key which is used in encryption of session data and some other stuff
        It should be shared between all web applications
        """
        __pychecker__ = 'no-local'
        secretKeyFileName = os.path.join(self.mngDbDir, "secret_key")
        if self.mySecretKey:
            return self.mySecretKey
        elif os.path.isfile(secretKeyFileName):
            secretKeyFH = open(secretKeyFileName, "rb")
            self.mySecretKey = secretKeyFH.readline().rstrip()
            secretKeyFH.close()
        else:
            # generate random secret key
            self.mySecretKey = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(40))
        return self.mySecretKey

    def saveSecretKey(self):
        """
        Returns secret key which is used in encryption of session data and some other stuff
        It should be shared between all web applications
        """
        secretKeyFileName = os.path.join(self.mngDbDir, "secret_key")
        if not os.path.isfile(secretKeyFileName):
            secretKey = self.getSecretKey()
            secretKeyFH = open(secretKeyFileName, "wb")
            secretKeyFH.write(secretKey)
            secretKeyFH.close()

