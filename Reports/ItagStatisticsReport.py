'''
Created on Jun 1, 2013

@author: asaf
'''
#This Report returns the percentage of itag values from all transactions.
#It first queries all the distinct values, and counts their appearances.
#Then, it calculates their percentage in terms of transactions and in terms of bytes.
#loadResults method runs the report.
#GetCount, GetTransPer and GetBytesPer all return lists of the report results, accordingly.
#PrintReportResults prints all results

from DAL import ConnectorPool
from Utils import Pair

class ItagStatisticsReport:
    
    def __init__(self, StartDate, EndDate):
        self.StartDate=StartDate
        self.EndDate=EndDate
        self.distinct=0
        self.count=0
        self.percent_trans=0
        self.percent_bytes=0
        
    #This method executes the actual report, i.e. sends query to DB and stores the results in self fields.
    def loadResults(self, Flow_ID=0):
        #Connect:
        cursor=ConnectorPool.ConnectorPool.GetConnector()
        
        self.count=[]
        self.percent_trans=[]
        self.percent_bytes=[]
        self.distinct = []
        i=0
        max1_i=-1
        max2_i=-1
        max3_i=-1
        
        FlowList = []
        if str(type(Flow_ID)) == "<type 'int'>" :
            FlowList.append(Flow_ID)
        else :
            FlowList.extend(Flow_ID)


        #Query according to Flow_ID. IF not supplied, run on whole DB. IF supplied, Query from Flow_ID list only.
        if Flow_ID != 0:
            for k in range (0, len(FlowList)) :
                #Get only distinct values of itag:
                cursor.execute("SELECT DISTINCT(Value) FROM `Requests-Params` WHERE (Name_request_param='itag') AND (Request_ID = any(select Req_ID from Requests WHERE Transactions_ID = any(select ID from Transactions WHERE Flow_ID="+str(FlowList[k])+")))")
                self.distinct.extend(cursor.fetchall())
                
                #Omit redundant characters from results and count occurrences of each distinct itag value:
                for i in range (max1_i+1, len(self.distinct)):
                    self.distinct[i]=(str(self.distinct[i]))[3:-3]
                    self.distinct[i]=int(self.distinct[i]) #Need to find out how to recognize relevant characters
                    cursor.execute("SELECT COUNT(*) from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i])+" AND Request_ID = any(select Req_ID from Requests WHERE Transactions_ID = any(select ID from Transactions WHERE Flow_ID="+str(FlowList[k])+"))")
                    temp=cursor.fetchone()
                    if temp[0] !=0 :
                        self.count.append(temp[0])
                max1_i = i
                    
                #Calculate percentage in terms of transactions:
                cursor.execute("SELECT Count(*) FROM Transactions WHERE Flow_ID = "+str(FlowList[k]))
                total=cursor.fetchone()
                if total[0] == 0 :
                    result ="***Empty Database - Cannot complete ItagStatisticsReport.loadResults***\n"
                    return result
                    print (result)
                else : 
                    for i in range (max2_i+1, len(self.count)):
                        temp=100*float(self.count[i])/float(total[0])
                        self.percent_trans.append(temp)
                    max2_i = i
                    
                    #Calculate percentage in terms of bytes:
                    cursor.execute("SELECT SUM(NumDownloadedBytes) FROM Transactions where Flow_ID = "+str(FlowList[k]))
                    sum_of_bytes_total=cursor.fetchone()
                    for i in range (max3_i+1, len(self.distinct)):
                        cursor.execute("SELECT SUM(NumDownloadedBytes) from Transactions where Flow_ID = "+str(FlowList[k])+" AND ID=ANY (SELECT Transactions_ID FROM Requests where Req_ID=ANY (SELECT Request_ID from `Requests-Params` where Name_request_param='itag' AND Value="+str(self.distinct[i])+"))")
                        temp1=cursor.fetchone()
                        if temp1[0] == None :
                            temp2 = 0;
                        else :
                            temp2 = temp1[0]
                        temp3=100*float(temp2)/float(sum_of_bytes_total[0])
                        self.percent_bytes.append(temp3)
                    max3_i = i
                    
            
        else : #All Flow_ID's
            #Get only distinct values of itag:
            cursor.execute("SELECT DISTINCT(Value) FROM `Requests-Params` WHERE Name_request_param='itag'")
            self.distinct=cursor.fetchall()
            self.count=[]
            
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
                    temp2=100*float(temp1[0])/float(sum_of_bytes_total[0])
                    self.percent_bytes.append(temp2)
 
        ConnectorPool.ConnectorPool.CloseConnector()
        
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
r=ItagStatisticsReport(1,1)
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

#r.PrintReportResults()