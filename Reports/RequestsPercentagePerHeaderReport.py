'''
Created on Jun 1, 2013

@author: asaf
'''
#This query returns the percentage of requests with uri_param "begin", out of all requests in that coal file
from DAL import UIConnectorPool

class RequestsPercentagePerHeaderReport:
    
    def __init__(self, HeaderName, StartDate, EndDate):
        self.HeaderName=HeaderName
        self.StartDate=StartDate
        self.EndDate=EndDate
        self.RequestsWithBeginURIParamTrans=0
        self.RequestsWithBeginURIParamBytes=0
        self.NoBeginBytes=0
        self.NoBeginPercent=0
        self.RequestsWithBeginEqZeroTrans=0
        self.RequestsWithBeginEqZeroBytes=0
        self.RequestsWithBeginNotEqZeroTrans=0
        self.RequestsWithBeginNotEqZeroBytes=0
        
    def loadResults(self):
        
        cursor=UIConnectorPool.ConnectorPool.GetConnector()
        #print("execute DB")
        #Percentage in terms of number of transactions:
        cursor.execute("SELECT COUNT(*) FROM `Transactions`")
        total=cursor.fetchone()
        if total[0] == 0 :
            result = "***Empty Database - Cannot complete RequestsPercentagePerHeaderReport.loadResults***\n"
            return result
            print (result)
        else:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='begin'")
            count=cursor.fetchone()
            self.RequestsWithBeginURIParamTrans=100*(float(count[0])/float(total[0]))
            self.NoBeginPercent=100-self.RequestsWithBeginURIParamTrans
            
            #Percentage in terms of number of bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
            sum_of_bytes_total=cursor.fetchone()
            cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID=ANY(select Transactions_ID from Requests where Req_ID=ANY(select Request_ID from `Requests-Params` where Name_request_param='begin'))")
            sum_of_bytes_begin=cursor.fetchone()
            self.RequestsWithBeginURIParamBytes=100*float(int(sum_of_bytes_begin[0] or 0))/float(sum_of_bytes_total[0])
            self.NoBeginBytes=100-self.RequestsWithBeginURIParamBytes
                    
            #Percentage only of begin=0, transactions:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='begin' AND Value='0'")
            count=cursor.fetchone()
            self.RequestsWithBeginEqZeroTrans=100*(float(count[0])/float(total[0]))
                
            #Percentage only of begin=0, bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions WHERE ID=(select Transactions_ID from Requests where Req_ID=(select Request_ID from `Requests-Params` where Name_request_param='begin' and Value='0'))")
            sum_of_bytes_begin=cursor.fetchone()
            self.RequestsWithBeginEqZeroBytes=100*float(int(sum_of_bytes_begin[0] or 0))/float(sum_of_bytes_total[0])
            
            #Percentage only of begin!=0, transactions:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='begin' AND Value!='0'")
            count=cursor.fetchone()
            self.RequestsWithBeginNotEqZeroTrans=100*(float(count[0])/float(total[0]))
            
            #Percentage only of begin!=0, bytes:
            cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID= ANY(select Transactions_ID from Requests where Req_ID= ANY(select Request_ID from `Requests-Params` where Name_request_param='begin' and Value!='0'))")
            sum_of_bytes_begin=cursor.fetchone()
            self.RequestsWithBeginNotEqZeroBytes=100*float(int(sum_of_bytes_begin[0] or 0))/float(sum_of_bytes_total[0])
        
            UIConnectorPool.ConnectorPool.CloseConnector()
            self.PrintReportResults()
        
    def PrintReportResults(self):  
        print("===== RequestsPercentagePerHeaderReport START ======")
          
        print("Percentage of Requests with 'begin' URI param (all values):")
        print("In terms of number of transactions:")
        print(self.RequestsWithBeginURIParamTrans)
        
        print("In terms of bytes:")
        print(self.RequestsWithBeginURIParamBytes)
        print("\n")
        
        #Non-begin requests:
        print("Percentage of Requests WITHOUT 'begin' URI param:")
        print("In terms of number of transactions:")
        print(self.NoBeginPercent)
        print("In terms of bytes:")
        print(self.NoBeginBytes)
        print("\n")
        
        print("Percentage of Requests with 'begin'=0:")
        print("In terms of number of transactions:")
        print(self.RequestsWithBeginEqZeroTrans)
        
        print("In terms of bytes:")
        print(self.RequestsWithBeginEqZeroBytes)
        print("\n")
        
        print("Percentage of Requests with 'begin'!=0:")
        print("In terms of number of transactions:")
        print(self.RequestsWithBeginNotEqZeroTrans)
        
        print("In terms of bytes:")
        print(self.RequestsWithBeginNotEqZeroBytes)
        
        print("====== RequestPercentagePerHeaderReport END ======\n")
        
#Test - moved to Tests Package        
#r=RequestsPercentagePerHeaderReport(1,1,1)
#r.loadResults()
#r.PrintReportResults()       


