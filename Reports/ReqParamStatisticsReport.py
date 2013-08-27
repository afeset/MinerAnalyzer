'''
Created on Jun 1, 2013

@author: asaf
'''
#This report returns the percentage of requests with a certain uri_param, out of all transactions in the chosen coal files.
#Note that as for now it is utilized for 'begin' param. Try with 'ipbits' param as well.
#IMPORTANT NOTE #1: when supplying lists to class instance, they should be bounded with '()', not '[]'.
#IMPORTANT NOTE #2: Class instance should be called with 'ParamName' string (with ''). Default value is 'begin'
from DAL import ConnectorPool

class ReqParamStatisticsReport:
    
    def __init__(self, ParamName='begin', Flow_ID=0):
        self.ParamName=ParamName
        self.Flow_ID=Flow_ID
        self.RequestsWithURIParamTrans=0
        self.RequestsWithURIParamBytes=0
        self.NoParamBytes=0
        self.NoParamPercent=0
        self.RequestsWithParamEqZeroTrans=0
        self.RequestsWithParamEqZeroBytes=0
        self.RequestsWithParamNotEqZeroTrans=0
        self.RequestsWithParamNotEqZeroBytes=0
    
    #This method executes the queries when no Flow_ID is supplied, i.e. all DB is queried.
    def GetAllResults(self):
        
        cursor=ConnectorPool.ConnectorPool.GetConnector()
        
        cursor.execute("SELECT COUNT(*) FROM `Transactions`")
        total=cursor.fetchone()
        if total[0] == 0 or total[0] == None :
            result = "***Empty Database - Cannot complete ReqParamStatisticsReport.loadResults***\n"
            print (result)
            return result
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
                    
            #Percentage only of param=0, transactions:            
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"' AND Value='0'")
            count=cursor.fetchone()
            self.RequestsWithParamEqZeroTrans=100*(float(count[0])/float(total[0]))
                
            #Percentage only of param=0, bytes:            
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions WHERE ID=ANY(select Transactions_ID from Requests where Req_ID=ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"' and Value='0'))")
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithParamEqZeroBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
            
            #Percentage only of param!=0, transactions:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"' AND Value!='0'")
            count=cursor.fetchone()
            self.RequestsWithParamNotEqZeroTrans=100*(float(count[0])/float(total[0]))
            
            #Percentage only of param!=0, bytes:
            cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID= ANY(select Transactions_ID from Requests where Req_ID= ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"' and Value!='0'))")
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithParamNotEqZeroBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
            
        ConnectorPool.ConnectorPool.CloseConnector()
    
    #This method executes the queries when Flow_ID/Flow_ID's are supplied 
    def GetFlowResults(self):
        
        cursor=ConnectorPool.ConnectorPool.GetConnector()
        
        # Assign "multi" variable with the relevant string.
        # If Flow_ID list has only one element, use '=' in query, else use 'IN' in query:
        if str(type(self.Flow_ID)) == "<type 'int'>" :
            multi = '='
        else :
            multi = 'IN'
        
        #Percentage in terms of number of transactions:
        cursor.execute("SELECT COUNT(*) FROM Transactions WHERE Flow_ID "+str(multi)+" "+str(self.Flow_ID))
        total=cursor.fetchone()
        if total[0] == 0 or total[0] == None :
            result = "***Empty Database - Cannot complete ReqParamStatisticsReport.loadResults***\n"
            print (result)
            return result
        else:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"' AND Request_ID = any(select Req_ID from Requests where Transactions_ID = any(select ID from Transactions where Flow_ID "+str(multi)+" "+str(self.Flow_ID)+"))")
            count=cursor.fetchone()
            self.RequestsWithURIParamTrans=100*(float(count[0])/float(total[0]))
            self.NoParamPercent=100-self.RequestsWithURIParamTrans
            
            #Percentage in terms of number of bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) From Transactions WHERE Flow_ID "+str(multi)+" "+str(self.Flow_ID))
            sum_of_bytes_total=cursor.fetchone()
            cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID=ANY(select Transactions_ID from Requests where Req_ID=ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"')) AND Flow_ID "+str(multi)+" "+str(self.Flow_ID))            
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithURIParamBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
            self.NoParamBytes=100-self.RequestsWithURIParamBytes
                    
            #Percentage only of param=0, transactions:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"' AND Value='0' AND Request_ID = any(select Req_ID from Requests where Transactions_ID = any(select ID from Transactions where Flow_ID "+str(multi)+" "+str(self.Flow_ID)+"))")        
            count=cursor.fetchone()
            self.RequestsWithParamEqZeroTrans=100*(float(count[0])/float(total[0]))
                
            #Percentage only of param=0, bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions WHERE ID=ANY(select Transactions_ID from Requests where Req_ID=ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"' and Value='0')) and Flow_ID "+str(multi)+" "+str(self.Flow_ID))            
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithParamEqZeroBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
            
            #Percentage only of param!=0, transactions:
            cursor.execute("SELECT COUNT(*) FROM `Requests-Params` WHERE Name_request_param='"+self.ParamName+"' AND Value!='0' AND Request_ID = any(select Req_ID from Requests where Transactions_ID = any(select ID from Transactions where Flow_ID "+str(multi)+" "+str(self.Flow_ID)+"))")
            count=cursor.fetchone()
            self.RequestsWithParamNotEqZeroTrans=100*(float(count[0])/float(total[0]))
            
            #Percentage only of param!=0, bytes:
            ###MODIFY HERE:
            cursor.execute("select SUM(NumDownloadedBytes) from Transactions where ID= ANY(select Transactions_ID from Requests where Req_ID= ANY(select Request_ID from `Requests-Params` where Name_request_param='"+self.ParamName+"' and Value!='0')) AND Flow_ID "+str(multi)+" "+str(self.Flow_ID))
            sum_of_bytes_param=cursor.fetchone()
            self.RequestsWithParamNotEqZeroBytes=100*float(int(sum_of_bytes_param[0] or 0))/float(sum_of_bytes_total[0])
            
        ConnectorPool.ConnectorPool.CloseConnector()

    #Load results from whole DB or specific Flow_ID's:
    def loadResults(self):
        
        if self.Flow_ID != 0 :
            self.GetFlowResults()
        else :
            self.GetAllResults()
    
    #Print all results:
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
        
#Test:      
r=ReqParamStatisticsReport('ipbits', (1,2))
r.loadResults()
r.PrintReportResults()       


