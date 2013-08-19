#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 
import httplib

import utils
import delivery_conf

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_NGINX_IPC = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_NGINX_IPC

#-------------------------------------------------------------------------------
class Request:

    def __init__ (self):
        self.host = ""
        self.port = 0
        self.url = ""     
        self.timeout = delivery_conf.KDeliveryConf.kIpcHttpRequestTimeoutSec   

#-------------------------------------------------------------------------------
class Response:

    def __init__ (self):
        self.status = 0
        self.reason = None
        self.data   = None

#-------------------------------------------------------------------------------
class NginxIpc(object):
   
    def __init__ (self, name, logger):
        self.__name = name        
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_NGINX_IPC)  
         
    #-------------------------------------------------------------------------------------------------
    def sendRequest (self, request, response):

        try:
            if request.timeout == 0:
                # Use Global Timeout 
                conn = httplib.HTTPConnection(request.host,request.port)
            else:
                conn = httplib.HTTPConnection(request.host,request.port,timeout=request.timeout)
        except Exception, e:
            self.__log("connect-failed").notice("Connect to - %s:%s%s Failed - %s",request.host,request.port,request.url,utils.parseErrnoToString(e))
            return False
         
        # Send Request   
        try:
            self.__log("send-http-req").debug3("Send HTTP Request - %s:%s%s",request.host,request.port,request.url)
            conn.request("GET",request.url)            
        except Exception, e:
            self.__log("send-http-req-failed").notice("Failed to Send HTTP Request - Hostname = %s:%s, URL - %s - %s",
                                                 request.host,request.port,request.url,utils.parseErrnoToString(e))
            # to be on the safe side
            conn.close()
            return False

        # Get Response
        try:
            httpResponse = conn.getresponse()
        except Exception, e :
            self.__log("http-get-response-failed").notice("Failed to receive HTTP Response - Hostname = %s:%s, URL - %s - %s",
                                                 request.host,request.port,request.url,utils.parseErrnoToString(e))
            conn.close()
            return False

        response.status = httpResponse.status
        response.reason = httpResponse.reason
        

        while 1:
    
            # Get Response
            try:
                response.data   = httpResponse.read()
                self.__log("http-get-response").debug3("Received Http Response on URL: %s Status = %s Reason = %s",
                                               request.url,str(httpResponse.status),str(httpResponse.reason))            
            except Exception, e :

                if utils.isEINTR(e):
                    continue
                else:
                    self.__log("http-get-data-failed").notice("Failed to receive Data from HTTP Responce - Hostname = %s:%s, URL - %s - %s",
                                                     request.host,request.port,request.url,utils.parseErrnoToString(e))
                    
            break
              
        conn.close()

        return True
