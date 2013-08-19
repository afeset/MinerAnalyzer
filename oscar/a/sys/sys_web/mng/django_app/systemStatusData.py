
import os
import socket

# === DataProvider ====================================================================================================

class DataProvider():
    def __init__(self, systemStatusDir, apiLogger = None, mainLogger = None):
        from a.sys.sys_web.server.log import NullLogger
        self.systemStatusDir = systemStatusDir
        self.apiLogger  = apiLogger  if apiLogger  is not None else NullLogger()
        self.mainLogger = mainLogger if mainLogger is not None else NullLogger()

    # --- _readSingleLine ---------------------------------------------------------------------------------------------
    def _readSingleLine(self, fileName):
        
        # Calc file path               
        filePath = os.path.join(self.systemStatusDir, fileName)

        # Open the file
        try:         
            file = open(filePath, 'r')
        except:
            self.apiLogger.warn("Failed openning %s to read single line" % filePath)
            self.mainLogger.warn("Failed openning %s to read single line" % filePath)
            raise
                       
        # Read a line and close the file
        try:
            line = file.readline()
            line = line.rstrip("\n")
        except:
            self.apiLogger.warn("Failed to read line from %s" % filePath)
            self.mainLogger.warn("Failed to read line from %s" % filePath)
            raise
        else:
            self.apiLogger.debug("Read '%s' from %s" % (line, filePath) )
        finally:
            file.close() 

        # OK
        return line        

    # --- _assignString -------------------------------------------------------------------------------------------------
    def _assignString(self, fileName, keyName, destination):

        # Read a line from the file
        try: 
            line =  self._readSingleLine(fileName)
        except:
            # Log read failure and don't assign value
            self.apiLogger.exception("Exception occurred, failed to read line for %s to key %s " % ( fileName , keyName) )
            self.mainLogger.exception("Exception occurred, failed to read line for %s to key %s " % ( fileName , keyName) )
            return 

        # successful read, assing it
        destination[keyName] = line
        
    # --- _assignInt --------------------------------------------------------------------------------------------------
    def _assignInt(self, fileName, keyName, destination):

        # Read a line from the file
        try: 
            line =  self._readSingleLine(fileName)
        except:
            # Log read failure and don't assign value
            self.apiLogger.exception("Exception occurred, failed to read line for %s to key %s " % ( fileName , keyName) )
            self.mainLogger.exception("Exception occurred, failed to read line for %s to key %s " % ( fileName , keyName) )
            return 

        # Convert the line to int
        try:
            val = int(line)
        except ValueError:
            # Log value error and don't assign 
            self.apiLogger.info("could not convert '%s' to integer for '%s' to key %s" % (line, fileName, keyName) )
            self.mainLogger.info("could not convert '%s' to integer for '%s' to key %s" % (line, fileName, keyName) )
            return
        except:
            # Unknown error, raise and exception 
            raise

        # OK
        destination[keyName] = val
            
        
    # --- System status

    def systemStatusHealth(self):
        result = {}
        result['overallStatus']     = { 'severity': 'info',  'value': 'OK' }
        #result['cpuUtilization']    = { 'severity': 'info',  'value': 0.25 }
        #result['memoryUtilization'] = { 'severity': 'info',  'value': 0.3 }
        #result['storageStatus']     = { 'severity': 'error', 'value': 'Almost full' }
        return result

    def systemStatusCache(self):
        result = {}
        self._assignInt("titles-acquired.dat",    'acquired', result)
        self._assignInt("titles-stored.dat",    'stored', result)
        self._assignInt("titles-delivered.dat", 'delivered', result)
        return result

    def systemStatusNetwork(self):
        result = {}
        return result

    def systemStatusSoftware(self):
        result = {}
        self._assignString("software-version.dat", 'version', result)
        result['license']  = "Content-Delivery"
        #result['sitePack'] = "1.4zzz3"
        return result

    def systemStatusAlerts(self):
        result = []
        #result.append( { "severity" : "warning",  "text" : "Raining",     "time" :   int( time.time() ) - 3600 * 1.6 } )
        #result.append( { "severity" : "critical", "text" : "Out of snow", "time" :   int( time.time() ) - 3600 * 2.5 } )
        return result
                    
    def systemStatusMediaSignaturePack(self):
        result = {}
        self._assignString("msp-version.dat", 'version', result)
        return result

    def systemStatusSystem(self):
        result = {}
        result['hostname'] = socket.gethostname()
        return result

