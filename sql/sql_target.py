#import json
#import tempfile
#import os.path
import sys
import subprocess
import mysql.connector
import datetime
from time import strftime
from datetime import datetime
from HttpObjects import  *
#from sql.HttpObjects import *   #, ReqParam
#from sql.HttpObjects.ReqParam import ReqParam
#from sql.HttpObjects import ReqParam



class sqlDump:
    def __init__(self, fileName, variableNames, **moreParams):
        #At some point make the option to connect to a specific DB with specific username and password such as 
        #self.login=moreParams["login"]
        self.filename=fileName
        #self.password
        #Set Object's indexes in varableNames
        self.coalIndex = variableNames.index("coal")
        self.requestIndex = variableNames.index("request")
        self.responseIndex = variableNames.index("response")     
        #Set Connection info            
        self.cnx = mysql.connector.connect(user='root', password='1234',host='127.0.0.1',database='Project')
        #Run one sql query at init stage
        cursor = self.cnx.cursor()
        cursor.execute("SELECT max(ID) FROM Transactions")
        max_trans_id=cursor.fetchone()
        self.max_trans_id=max_trans_id[0]
        self.transCount=1
        if self.max_trans_id==None:
            self.max_trans_id=1;
            self.transCount=0;
        cursor.execute("SELECT max(ID) FROM Flow")
        max_flow_id=cursor.fetchone()
        self.max_flow_id=max_flow_id[0]
        if self.max_flow_id==None:
            self.max_flow_id=0
        #self.requestID=0
        #Lists creation
        self.transList=[]
        
       
        # ID's settings=>If needed we can create count indexes for object's ID's
       
        print ("self.transCount", self.transCount)
    def save(self,record):
        #cnx = mysql.connector.connect(user='root', password='1234',host='127.0.0.1',database='Project')
        
        print("Max FLOW", self.max_flow_id)
        #Retreive objects;
        if self.coalIndex!=-1:
            coal=record[self.coalIndex]
        else:
            coal='None'
        if self.requestIndex!=-1:
            request=record[self.requestIndex]
        else:
            request='None'
        if self.responseIndex!=-1:
            response=record[self.responseIndex]
        else:
            response='None'
        
        #Create Objects:
    
        #Transactions object ('trans'):
        trans_time=datetime.fromtimestamp(int(coal.unixTime)).strftime('%Y-%m-%d %H:%M:%S')
        cgid=coal.decoding.cgid
        cid=coal.decoding.cid
        sitename='Static-YOUTUBE'
        duration=coal.DurationMili
        client_ip=coal.flow.clientIP.text
        client_dest_port=coal.flow.clientPort
        server_ip=coal.flow.serverIP.text
        server_dest_port=coal.flow.serverPort
        checksum=coal.decoding.checksum1k10k
        
        #flows=Flow.Flow(self.max_flow_id+1,d)
        #flowlist.append(flows)
        
        trans=Transaction.Transaction((),trans_time,cgid, cid, sitename, duration, client_ip, client_dest_port, server_ip, server_dest_port, checksum, self.max_flow_id+1, coal.numDownloadedBytes)
        
   
        #Requests object:
       # requests=Request.Request((),self.max_trans_id,request.httpVersion,request.method)
        Req_Trans_ID=self.max_trans_id+self.transCount #This will change when using pipline
        #self.requestID=Req_Trans_ID
        trans.requests=Request.Request((),request.httpVersion,Req_Trans_ID,request.method) #When pipeline is added use len(self.transList)+1 instead of transcount
        print("max Trans_ID:", self.max_trans_id)
        print("Trans_ID: ", self.max_trans_id+len(self.transList))
        #trans.requestList.append(req) ----might be needed with pipline

#       ReqParam Dictonary creation:
        #dic={}
        
        for (name,value) in request.params.iteritems ():
            #dic[name]= value
            trans.requests.params.append(ReqParam.ReqParam((),Req_Trans_ID,name,value))

        #trans.requests.params=ReqParam.ReqParam((),Req_Trans_ID,dic)
           
        #for (name,value) in dic.items (): print (name,value) 
        #print ("lenth dic: ",len(dic))
        
#       Create Requests PathSeg list 
        segments=request.path.split("?")
        pathsegments1=segments[0]
        pathsegments2=pathsegments1.split("/")

        for i in range (1,len(pathsegments2)):
            trans.requests.pathsegs.append(ReqPathSeg.ReqPathSeg((),Req_Trans_ID,pathsegments2[i],i))

    
#       Create Requests Headers list 
        
        
        for (name,value) in request.headers.dict.iteritems ():
            trans.requests.headers.append(ReqHeader.ReqHeader((),Req_Trans_ID,name,value))
            #print("name,Value: ",name,value)
#--------------------       RESPONSE-------------------------------------------------------- 
        trans.responses=Response.Response((),self.max_trans_id+self.transCount,response.statusCode)
        #self.reponseList.append(object)
        
        
        #       Create Response Headers list 
        
        
        for (name,value) in response.headers.dict.iteritems ():
            trans.responses.headers.append(ResHeader.ResHeader((),self.max_trans_id+self.transCount,name,value))
        
        
        
        
        
        
        #    APPEND Transaction List
        self.transList.append(trans)    
        print(self.transCount)
        self.transCount=self.transCount+1
              


    def close(self):
        cursor = self.cnx.cursor()
        add_flow_dummy=("INSERT INTO Flow "
                "(ID, System_date) "
                 "VALUES (%s,%s)")
        flow_data=(self.max_flow_id+1, datetime.now()) 
        cursor.execute(add_flow_dummy,flow_data)
        #self.cnx.commit()
        for i in range(0, len(self.transList)):
            add_transactions=("INSERT INTO Transactions "
               "(Transaction_time, cgid, cid, site_signature_name, duration, Client_IP, Client_Dest_Port, Server_IP, Server_Dest_Port, checksum, Flow_ID, NumDownloadedBytes) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            data_transactions=( self.transList[i].Transaction_time, self.transList[i].cgid, self.transList[i].cid, self.transList[i].site_signature_name, self.transList[i].duration, self.transList[i].Client_IP, self.transList[i].Client_Dest_Port, self.transList[i].Server_IP, self.transList[i].Server_Dest_Port, self.transList[i].checksum, self.transList[i].Flow_ID, self.transList[i].NumDownloadedBytes)
            cursor.execute(add_transactions, data_transactions)
            ###TEMP
            cursor.execute("SELECT max(ID) FROM Transactions")
            max_trans_id_temp=cursor.fetchone()
            max_trans_id_temp=max_trans_id_temp[0]
            print("Transaction-ID from sql", max_trans_id_temp)
            ###END TEMP
            #Handle Requests Table insertion
            add_requests=("INSERT INTO Requests "
                   "(Transactions_ID, http_version, method) "
                   "VALUES (%s, %s, %s)")
            print("Requests-Trans_ID in list:" ,(self.transList[i].requests.Transactions_ID))
            data_requests=( self.transList[i].requests.Transactions_ID,self.transList[i].requests.http_version,self.transList[i].requests.method)
            cursor.execute(add_requests, data_requests)

            #Handle requests-params table:
            add_req_params=("INSERT INTO `Requests-Params` "
               "(Request_ID, Value, Name_request_param) "
               "VALUES (%s, %s, %s)")
            
            for j in range (0,len(self.transList[i].requests.params)):
                data_req_params=(self.transList[i].requests.params[j].Request_ID, self.transList[i].requests.params[j].Value, self.transList[i].requests.params[j].Name_request_param)
                cursor.execute(add_req_params, data_req_params)
            
            #Handle requests-PathSeg table:
            add_req_pathseg=("INSERT INTO `Requests-PathSeg` "
               "(Request_ID, Value,Relative_path_location) "
               "VALUES (%s, %s, %s)")
            print("self.transList[i].requests.pathsegs",len(self.transList[i].requests.pathsegs))
            for j in range (0,len(self.transList[i].requests.pathsegs)):
                #trans.requests.pathsegs[i]=ReqPathSeg.ReqPathSeg((),Req_Trans_ID,pathsegments2[i],i)
                data_req_pathseg=(self.transList[i].requests.pathsegs[j].Request_ID, self.transList[i].requests.pathsegs[j].Value,self.transList[i].requests.pathsegs[j].Relative_path_location)
                cursor.execute(add_req_pathseg, data_req_pathseg)  
            
            #Handle requests-Headers table:
            add_req_headers=("INSERT INTO `Requests-Headers` "
               "(Request_ID, Header_Name, Value) "
               "VALUES (%s, %s, %s)")
            for j in range (0,len(self.transList[i].requests.headers)):
                data_req_headers=(self.transList[i].requests.headers[j].Request_ID,self.transList[i].requests.headers[j].Header_Name, self.transList[i].requests.headers[j].Value)
                cursor.execute(add_req_headers, data_req_headers)  
#      --------------------------------------------------------------------------

            #Handle Responses insertion
            add_responses=("INSERT INTO Responses "
                   "(Transactions_ID, Response_Code) "
                   "VALUES (%s, %s)")
            data_responses=(self.transList[i].responses.Transactions_ID, self.transList[i].responses.Response_Code)
            cursor.execute(add_responses, data_responses)
                    
            #Handle response-Headers table:
            add_resp_headers=("INSERT INTO `Responses-Headers` "
               "(Response_ID, Name_response_header, Value) "
               "VALUES (%s, %s, %s)")
            for j in range (0,len(self.transList[i].responses.headers)):
                data_resp_headers=(self.transList[i].responses.headers[j].Response_ID,self.transList[i].responses.headers[j].Name_response_header, self.transList[i].responses.headers[j].Value)
                cursor.execute(add_resp_headers, data_resp_headers)  
        self.cnx.commit()
        cursor.close()
        self.cnx.close()
        
         
