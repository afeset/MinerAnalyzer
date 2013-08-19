'''
Created on Aug 10, 2013

@author: asaf
'''
'''
#from Configuration.Config import Config
#import sys
#sys.path.append("/home/asaf/jython2.2/src/java/src/com/ziclix/python/sql")
from com.ziclix.python.sql import zxJDBC 


#db = zxJDBC.connect("jdbc:mysql://localhost/Project", "root", "1234", "org.gjt.mm.mysql.Driver")
#from DAL import ConnectorPool
#import mysql.connector
class Test1():
    def __init__(self, i):
        self.i=i

    def Run(self):
        connection=zxJDBC.connect("jdbc:mysql://localhost/Project", "root", "1234", "org.gjt.mm.mysql.Driver")
        cursor=connection.cursor()
        cursor.execute("select * from Requests")
        count=cursor.fetchall()
        print(count)
      


class TestRunner:
    
        
    def establishConnection(self):
        
  db = zxJDBC.connect("jdbc:mysql://localhost:3306/testingDB", "root", "password", "org.gjt.mm.mysql.Driver")
        cursor = db.cursor()
        cursor.execute("select * from testcase_peanutsdata")
        nRecords = cursor.fetchall()'''