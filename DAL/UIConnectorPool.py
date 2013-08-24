'''
Created on Aug 18, 2013

@author: asaf
'''

from com.ziclix.python.sql import zxJDBC 
from Configuration.Config import Config

_name_ = 'ConnectorPool'
#git test12
class ConnectorPool:
    #cnx = mysql.connector.connect(user=Config.USER, password=Config.PASSWORD, host=Config.HOST, database=Config.DATABASE)
    #cursor = cnx.cursor()
    connection=0
    cursor=0
    
    @staticmethod
    def GetConnector():
        if(ConnectorPool.cursor==0):
            ConnectorPool.connection=zxJDBC.connect("jdbc:mysql://localhost/Project", "root", "1234", "org.gjt.mm.mysql.Driver")
            ConnectorPool.cursor=ConnectorPool.connection.cursor()
        return ConnectorPool.cursor
        
    
    
                  
    @staticmethod
    def CloseConnector():
        if(ConnectorPool.cursor != 0):
            ConnectorPool.cursor.close()
            ConnectorPool.cursor=0
        if(ConnectorPool.connection!=0):
            ConnectorPool.connection.commit()
            ConnectorPool.connection.close()
            ConnectorPool.connection=0   

