'''
Created on Aug 14, 2013

@author: asaf
'''
import sys
sys.path.append("/home/asaf/miner2.0")
import miner_globals 
sys.path.append("/home/asaf/miner2-tools")
from sql import sql_target

miner_globals.addTargetToClassMapping("sql",None,"sql_target.sqlDump","Write To SQL DB")
