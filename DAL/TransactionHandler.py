'''
Created on May 1, 2013

@author: asaf
'''
from DAL import ConnectorPool
import datetime
from time import strftime
from datetime import datetime
from HttpObjects import *
       
class TransactionHandler:
    
    def insertTransaction(self,trans):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        #Handle Transactions table:
        add_transactions=("INSERT INTO Transactions "
                   "(Transaction_time, cgid, cid, site_signature_name, duration, Client_IP, Client_Dest_Port, Server_IP, Server_Dest_Port, checksum, Flow_ID, NumDownloadedBytes) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_transactions=(trans.Transaction_time, trans.cgid, trans.cid, trans.site_signature_name, trans.duration, trans.Client_IP, trans.Client_Dest_Port, trans.Server_IP, trans.Server_Dest_Port, trans.checksum, trans.Flow_ID, trans.NumDownloadedBytes)
        cursor.execute(add_transactions, data_transactions)
        ConnectorPool.ConnectorPool.CloseConnector()
    
    def insertTransactionsList(self, transList):
        cursor = ConnectorPool.ConnectorPool.GetConnector()
        #Handle Transactions table:
        for i in range(0, len(transList)) :
            add_transactions=("INSERT INTO Transactions "
                       "(Transaction_time, cgid, cid, site_signature_name, duration, Client_IP, Client_Dest_Port, Server_IP, Server_Dest_Port, checksum, Flow_ID, NumDownloadedBytes) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            data_transactions=(transList[i].Transaction_time, transList[i].cgid, transList[i].cid, transList[i].site_signature_name, transList[i].duration, transList[i].Client_IP, transList[i].Client_Dest_Port, transList[i].Server_IP, transList[i].Server_Dest_Port, transList[i].checksum, transList[i].Flow_ID, transList[i].NumDownloadedBytes)
            cursor.execute(add_transactions, data_transactions)
        ConnectorPool.ConnectorPool.CloseConnector()

    