'''
Created on Jun 1, 2013

@author: asaf
'''
#This query returns the percentage of requests with uri_param "begin", out of all requests in that coal file
from DAL import ConnectorPool

class ReqParamStatisticsReport:
    
    def __init__(self, ParamName):
        self.ParamName=ParamName
        self.RequestsWithURIParamTrans=0
        self.RequestsWithURIParamBytes=0
        self.NoParamBytes=0
        self.NoParamPercent=0
        self.RequestsWithParamEqZeroTrans=0
        self.RequestsWithParamEqZeroBytes=0
        self.RequestsWithParamNotEqZeroTrans=0
        self.RequestsWithParamNotEqZeroBytes=0
        
    def loadResults(self):
        
        cursor=ConnectorPool.ConnectorPool.GetConnector()
        #print("execute DB")
        #Percentage in terms of number of transactions:
        cursor.execute("SELECT COUNT(*) FROM `Transactions`")
        total=cursor.fetchone()
        if total[0] == 0 :
            result = "***Empty Database - Cannot complete ReqParamStatisticsReport.loadResults***\n"
            return result
            print (result)
        else:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"'")
            count=cursor.fetchone()
            self.RequestsWithURIParamTrans=100*(float(count[0])/float(total[0]))
            self.NoParamPercent=100-self.RequestsWithURIParamTrans
            
            #Percentage in terms of number of bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
            sum_of_bytes_total=cursor.fetchone()
            cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID=ANY(select Transactions_ID from Requests where Req_ID=ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"'))")
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithURIParamBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
            self.NoParamBytes=100-self.RequestsWithURIParamBytes
                    
            #Percentage only of begin=0, transactions:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"' AND Value='0'")
            count=cursor.fetchone()
            self.RequestsWithParamEqZeroTrans=100*(float(count[0])/float(total[0]))
                
            #Percentage only of begin=0, bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions WHERE ID=ANY(select Transactions_ID from Requests where Req_ID=ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"' and Value='0'))")
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithParamEqZeroBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
            
            #Percentage only of begin!=0, transactions:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"' AND Value!='0'")
            count=cursor.fetchone()
            self.RequestsWithParamNotEqZeroTrans=100*(float(count[0])/float(total[0]))
            
            #Percentage only of begin!=0, bytes:
            cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID= ANY(select Transactions_ID from Requests where Req_ID= ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"' and Value!='0'))")
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithParamNotEqZeroBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
        
            ConnectorPool.ConnectorPool.CloseConnector()
        
    def PrintReportResults(self):  
        print("===== ReqParamStatisticsReport START ======")
          
        print("Percentage of Requests with '"+self.ParamName+"' URI param (all values):")
        print("In terms of number of transactions:")
        print(self.RequestsWithURIParamTrans)
        
        print("In terms of bytes:")
        print(self.RequestsWithURIParamBytes)
        print("\n")
        
        #Non-begin requests:
        print("Percentage of Requests WITHOUT '"+self.ParamName+"' URI param:")
        print("In terms of number of transactions:")
        print(self.NoParamPercent)
        print("In terms of bytes:")
        print(self.NoParamBytes)
        print("\n")
        
        print("Percentage of Requests with '"+self.ParamName+"'=0:")
        print("In terms of number of transactions:")
        print(self.RequestsWithParamEqZeroTrans)
        
        print("In terms of bytes:")
        print(self.RequestsWithParamEqZeroBytes)
        print("\n")
        
        print("Percentage of Requests with '"+self.ParamName+"'!=0:")
        print("In terms of number of transactions:")
        print(self.RequestsWithParamNotEqZeroTrans)
        
        print("In terms of bytes:")
        print(self.RequestsWithParamNotEqZeroBytes)
        
        print("====== ReqParamStatisticsReport END ======\n")
        
#Test - moved to Tests Package        
r=ReqParamStatisticsReport('begin')
r.loadResults()
r.PrintReportResults()       


