'''
Created on Mar 13, 2013

@author: asaf
'''
from DAL import ConnectorPool

#This function truncates the DB. This means that it deletes all data and resets the auto-incremented ID's.
#Useful for cases where one needs to reset DB for tests and such.
#The function works in automatic mode (truncating all tables), or in manual mode, where one can choose which
#table will be deleted.
#By default, the method will run on automatic mode. If called with "MAN", manual mode will be enabled.

def TruncateDB(mode="AUTO"):
    cursor=ConnectorPool.ConnectorPool.GetConnector()
    all_tables=["Flow","Transactions", "Requests", "Requests-Params", "Requests-Headers", "Requests-PathSeg", "Responses", "Responses-Headers"]
    if mode == "MAN" :
        table=raw_input("Choose a table to truncate.\nNote: You can also type All to truncate all tables")
        yn=raw_input("are you sure??? This will delete all data in the table and its children (Y/N)")
        if(yn=="Y"):
            if (table=="All"):
                for i in range (0,8):
                    cursor.execute("TRUNCATE `"+str(all_tables[i])+"`")
                print("All tables have been truncated!")
            else:
                cursor.execute("TRUNCATE `"+str(table)+"`")
                print(str(table)+" has been truncated!")
    else :
        for i in range (0,8):
            cursor.execute("TRUNCATE `"+str(all_tables[i])+"`")
    ConnectorPool.ConnectorPool.CloseConnector()

#TruncateDB("MAN")
TruncateDB()