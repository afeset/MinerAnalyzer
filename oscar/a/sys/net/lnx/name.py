# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from common import *

##############################################
# hostname - show or set the system's host name
##############################################
class Hostname(object):

    HOST_NAME_COMMAND_NAME = "/bin/hostname"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showHostname(logger):
        """This function shows the system's host name"""
        rc =  Command.execute(logger, "host", 
                                [Hostname.HOST_NAME_COMMAND_NAME])
        return rc 


#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def setHostname(logger, hostname):
        """This function sets the system's host name"""
        rc =  Command.execute(logger, "host", 
                                [Hostname.HOST_NAME_COMMAND_NAME, hostname])   
        return rc
                                                                                        
##############################################
# dnsdomainname - show the system's DNS domain name
##############################################
class DnsDomainName(object):

    DNS_DOMAIN_NAME_COMMAND_NAME = "/bin/dnsdomainname"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showDomainname(logger):
        """This function shows the system's DNS domain name"""
        rc =  Command.execute(logger, "dns", 
                                [DnsDomainName.DNS_DOMAIN_NAME_COMMAND_NAME]) 
        return rc 


#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def setDomainname(logger, domainname):
        """This function sets the system's DNS domain name"""
        rc =  Command.execute(logger, "dns", 
                                [DnsDomainName.DNS_DOMAIN_NAME_COMMAND_NAME, domainname])   
        return rc




##############################################
#  This class view/edit the /etc/hosts configuration file
#  The file is used to specify static table lookup for host names
#  
# example:
#
#       127.0.0.1        localhost
#       192.168.1.10     foo.mydomain.org   foo
#       192.168.1.13     bar.mydomain.org   bar
#       146.82.138.7     master.debian.org  master
#       209.237.226.90   www.opensource.org
##############################################
class HostsFile(object):

    def __init__(self, logger):
        self._log = logger
        self.filename = "/etc/hosts"
        #self.filename = "/users/eng/amiry/tmp/resolve/hosts"
        self.tempfile = "%s.tmp" % self.filename
        self.data = ["127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4", 
                     "::1         localhost localhost.localdomain localhost6 localhost6.localdomain6"]

    def isExists(self):
        return os.path.exists(self.filename)

    def dumpData(self, pairList):
        """dump data into hosts file"""

        data = []

        self._log("dump-data-pait-list").debug3("%s: dump data input - %s", self.filename, pairList)

        for ip, hosts in pairList:
            if isinstance(hosts, str):
                hosts = [hosts]
            hostsStr = ""
            for host in hosts:
                hostsStr += (host + " ")
            data.append("%s\t%s" % (ip, hostsStr))

        data += self.data

        self._log("dump-data-hosts").debug3("%s: dump data - %s", self.filename, data)

        fd =  open(self.tempfile, 'w')
        fd.writelines("\n".join(data))
        fd.close()

    def commit(self):
        self._log("commit-hosts-file").debug3("%s: from %s commit data", self.filename, self.tempfile)
        shutil.move(self.tempfile, self.filename)

    def abort(self):
        self._log("abort-hosts-file").debug3("%s: abort data", self.tempfile)
        os.remove(self.tempfile)

##############################################
#  This class view/edit the /etc/resolv.conf configuration file
#  This file contains a list of keywords with values that provide various types of resolver information
#  that provide access to the Internet Domain Name System (DNS)
#  
# example:
# 
#       search qwilt.com
#       domain qwilt.com
#       nameserver 10.9.8.231
#       nameserver 10.9.8.232
##############################################
class ResolvConfFile(object):
    """Resolv conf file contains information that provide various types of resolver information"""

    def __init__ (self, logger):
        self._log = logger
        self.filename = "/etc/resolv.conf"
        #self.filename = "/users/eng/amiry/tmp/resolve/resolv.conf"
        self.tempfile = "%s.tmp" % self.filename

    def isExists(self):
        return os.path.exists(self.filename)

    def dumpData(self, nameServers, searchDomains):
        """dump data into resolve.conf file"""

        data = []

        for nameServer in nameServers:
            data.append("nameserver %s" % nameServer)

        for searchDomain in searchDomains:
            data.append("search     %s" % searchDomain)

        self._log("dump-data-resolve-conf").debug3("%s: dump data - %s", self.filename, data)

        fd =  open(self.tempfile, 'w')
        fd.writelines("\n".join(data))
        fd.close()

    def commit(self):
        self._log("commit-resolve-conf-file").debug3("%s: from %s commit data", self.filename, self.tempfile)
        shutil.move(self.tempfile, self.filename)

    def abort(self):
        self._log("abort-resolve-conf-file").debug3("%s: abort data", self.tempfile)
        os.remove(self.tempfile)

