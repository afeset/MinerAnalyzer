'''
Created on Mar 27, 2013

@author: eliran shemer bla
'''
import mysql.connector
import datetime
from HttpObjects import *
from time import strftime
from datetime import datetime
from Configuration.Config import Config
from DAL import ConnectorPool
       
class RequestsHandler:
        
    
    
    def insertRequest(self, req):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        #Handle requests table:
        add_requests=("INSERT INTO Requests "
                   "(Transactions_ID, method, http_version) "
                   "VALUES (%s, %s, %s)")
        data_requests=(req.transID, req.method, req.httpVersion)
        cursor.execute(add_requests, data_requests)
        ConnectorPool.ConnectorPool.CloseConnector()
    
    #Insert all requests in the given list to requests table on DB
    def insertRequestsList(self, reqList):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        for i in range(0, len(reqList)):
            add_requests=("INSERT INTO Requests "
                   "(Transactions_ID, method, http_version) "
                   "VALUES (%s, %s, %s)")
            data_requests=(reqList[i].Transactions_ID, reqList[i].method, reqList[i].http_version)
            cursor.execute(add_requests, data_requests)
        cursor = ConnectorPool.ConnectorPool.CloseConnector()
    
    #Return a list of requests with the given transaction id    
    def getTransRequests(self, transID):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        #Handle requests table:
        cursor.execute("Select * from Requests where Transactions_ID="+str(transID))
        reqList=[]
        for (Req_ID, http_version, Transactions_ID, method) in cursor:
            request=Request.Request(Req_ID, http_version, Transactions_ID, method)
            reqList.append(request)
        cursor = ConnectorPool.ConnectorPool.CloseConnector()
        return reqList
    
    #Insert all Request Headers in a given list to Requests-Headers table on DB
    def insertReqHeadersList(self, reqheaderList):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        for i in range(0, len(reqheaderList)):
            add_reqheaders=("INSERT INTO `Requests-Headers` "
                   "(Request_ID, Header_Name, Value) "
                   "VALUES (%s, %s, %s)")
            data_reqheaders=(reqheaderList[i].Request_ID, reqheaderList[i].Header_Name, reqheaderList[i].Value)
            cursor.execute(add_reqheaders, data_reqheaders)
        ConnectorPool.ConnectorPool.CloseConnector()
    
    #Insert all Request Headers in a given list to Requests-Headers table on DB
    def insertReqParamsList(self, reqparamList):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        for i in range(0, len(reqparamList)):
            add_reqparams=("INSERT INTO `Requests-Params` "
                   "(Request_ID, Name_request_param, Value) "
                   "VALUES (%s, %s, %s)")
            data_reqparams=(reqparamList[i].Request_ID, reqparamList[i].Name_request_param, reqparamList[i].Value)
            cursor.execute(add_reqparams, data_reqparams)
        ConnectorPool.ConnectorPool.CloseConnector()
    
    

#Testing:
#r=RequestsHandler()
#reqList=r.getTransRequests(308)
#for i in range(0, len(reqList)):
#    print(reqList[i].Req_ID)
