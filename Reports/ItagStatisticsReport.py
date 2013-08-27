'''
Created on Jun 1, 2013

@author: asaf
'''
#This report returns the percentage of itag values from all transactions.
#It first queries all the distinct values, and counts their appearances.
#Then, it calculates their percentage in terms of transactions and in terms of bytes.
#GetAllResults method queries the whole DB.
#GetFlowResults method queries selected Flow_ID's.
#loadResults method loads the result.
#GetCount, GetTransPer and GetBytesPer all return lists of the report results, accordingly.
#PrintReportResults prints all results

from DAL import ConnectorPool
from DAL import Pair

class ItagStatisticsReport:
    
    def __init__(self, Flow_ID=0):
        self.Flow_ID=Flow_ID
        self.distinct=[]
        self.count=[]
        self.bytes=[]
        self.percent_trans=[]
        self.percent_bytes=[]

    #This method executes the queries when no Flow_ID is supplied, i.e. all DB is queried.    
    def GetAllResults(self):
        
        cursor=ConnectorPool.ConnectorPool.GetConnector()
        
        #Get only distinct values of itag:
        cursor.execute("SELECT DISTINCT(Value) FROM `Requests-Params` WHERE Name_request_param='itag'")
        self.distinct=cursor.fetchall()
        #self.count=[]
        
        #Omit redundant characters from results and count occurrences of each distinct itag value:
        for i in range (0, len(self.distinct)):
            self.distinct[i]=(str(self.distinct[i]))[3:-3]
            self.distinct[i]=int(self.distinct[i]) #Need to find out how to recognize relevant characters
            cursor.execute("SELECT COUNT(*) from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i]))
            temp=cursor.fetchone()
            self.count.append(temp[0])
            
        #Calculate percentage in terms of transactions:
        cursor.execute("SELECT Count(*) FROM Transactions")
        total=cursor.fetchone()
        self.percent_trans=[]
        if total[0] == 0 :
            result ="***Empty Database - Cannot complete ItagStatisticsReport.loadResults***\n"
            return result
            print (result)
        else : 
            for i in range (0, len(self.count)):
                temp=100*float(self.count[i])/float(total[0])
                self.percent_trans.append(temp)
            
            #Calculate percentage in terms of bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions")
            sum_of_bytes_total=cursor.fetchone()
            self.percent_bytes=[]
            for i in range (0, len(self.distinct)):
                cursor.execute("SELECT SUM(NumDownloadedBytes) from Transactions where ID=ANY (SELECT Transactions_ID FROM Requests where Req_ID=ANY (SELECT Request_ID from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i])+"))")
                temp1=cursor.fetchone()
                if temp1[0] == None :
                    temp2 = 0
                else :
                    temp2 = temp1[0]
                temp3=100*float(temp2)/float(sum_of_bytes_total[0])
                self.percent_bytes.append(temp3)
 
        #Disconnect from Database:
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
        
        #Get only distinct values of itag:
        cursor.execute("SELECT DISTINCT(Value) FROM `Requests-Params` WHERE Name_request_param='itag' AND Request_ID= any(select Req_ID from Requests where Transactions_ID= any(select ID from Transactions where Flow_ID "+str(multi)+" "+str(self.Flow_ID)+"))")
        self.distinct=cursor.fetchall()
        #self.count=[]
        
        #Omit redundant characters from results and count occurrences of each distinct itag value:
        for i in range (0, len(self.distinct)):
            self.distinct[i]=(str(self.distinct[i]))[3:-3]
            self.distinct[i]=int(self.distinct[i]) #Need to find out how to recognize relevant characters
            cursor.execute("SELECT COUNT(*) from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i])+" AND Request_ID = any(select Req_ID from Requests where Transactions_ID = any(select ID from Transactions where Flow_ID "+str(multi)+" "+str(self.Flow_ID)+"))")
            temp=cursor.fetchone()
            self.count.append(temp[0])
            
        #Calculate percentage in terms of transactions:
        cursor.execute("SELECT Count(*) FROM Transactions where Flow_ID "+str(multi)+" "+str(self.Flow_ID))
        total=cursor.fetchone()
        self.percent_trans=[]
        if total[0] == 0 or total[0] == None :
            result ="***Empty Database - Cannot complete ItagStatisticsReport.loadResults***\n"
            return result
            print (result)
        else : 
            for i in range (0, len(self.count)):
                temp=100*float(self.count[i])/float(total[0])
                self.percent_trans.append(temp)
            
            #Calculate percentage in terms of bytes:
            cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions where Flow_ID "+str(multi)+" "+str(self.Flow_ID))
            sum_of_bytes_total=cursor.fetchone()
            self.percent_bytes=[]
            for i in range (0, len(self.distinct)):
                cursor.execute("SELECT SUM(NumDownloadedBytes) from Transactions where ID=ANY (SELECT Transactions_ID FROM Requests where Req_ID=ANY (SELECT Request_ID from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i])+")) and Flow_ID "+str(multi)+" "+str(self.Flow_ID))
                temp1=cursor.fetchone()
                if temp1[0] == None :
                    temp2 = 0
                else :
                    temp2 = temp1[0]
                temp3=100*float(temp2)/float(sum_of_bytes_total[0])
                self.percent_bytes.append(temp3)
        
        ConnectorPool.ConnectorPool.CloseConnector()
        
    #Load results from whole DB or specific Flow_ID's:
    def loadResults(self):
        
        if self.Flow_ID != 0 :
            self.GetFlowResults()
        else :
            self.GetAllResults()

        
    #This method returns the count of distinct itag appearances in DB        
    def GetCount(self) :
        countlist=[] #Will store count results
        for i in range (0, len(self.distinct)):
            countlist.append(Pair.Pair(self.distinct[i], self.count[i]))
        if countlist == [] :
            return [Pair.Pair(None, 0)]
        else :
            return countlist
    
    #This method returns the percentage of trans. with distinct itag values, out of all trans.
    def GetTransPer(self) :
        trans_per=[] #Will store percentage results in terms of transaction
        for i in range (0, len(self.distinct)) :
            trans_per.append(Pair.Pair(self.distinct[i], self.percent_trans[i]))
        if trans_per == [] :
            return [Pair.Pair(None, 0)]
        else :
            return trans_per
    
    #This method returns the percentage of bytes with distinc itag values, out of all trans.
    def GetBytesPer(self) :
        bytes_per=[] #Will store percentage results in terms of transaction
        for i in range (0, len(self.distinct)) :
            bytes_per.append(Pair.Pair(self.distinct[i], self.percent_bytes[i]))
        if bytes_per == [] :
            return [Pair.Pair(None, 0)]
        else :
            return bytes_per
    
    '''def DiffResults(self, Flow_IDs):'''
        
        
    
    #This method simply prints all of the report results    
    def PrintReportResults(self):
        print("====== ItagStatisticsReport START ======")
        print("itag Statistics:\n")
        print("The distinct values of itag in coal are:")
        print(self.distinct)
        print("\n")
        print("Their matching count is:")
        print(self.count)
        print("\n")
        print("Percentage in terms of transactions (indices match the distinct itag vector):")
        print(self.percent_trans)
        print("\n")
        print("Percentage in terms of bytes (indices match the distinct itag vector):")
        print(self.percent_bytes)
        print("====== ItagStatisticsReport END ======\n")
        
#Test:
r=ItagStatisticsReport((1,2))
r.loadResults()
r1=r.GetCount()
for i in range (0, len(r1)) :
    print ("Key_"+str(i)+": "+str(r1[i].key)+"    Value_"+str(i)+": "+str(r1[i].value))
r1=r.GetTransPer()
for i in range (0, len(r1)) :
    print ("Key_"+str(i)+": "+str(r1[i].key)+"    Value_"+str(i)+": "+str(r1[i].value))
r1=r.GetBytesPer()
for i in range (0, len(r1)) :
    print ("Key_"+str(i)+": "+str(r1[i].key)+"    Value_"+str(i)+": "+str(r1[i].value))

r.PrintReportResults()