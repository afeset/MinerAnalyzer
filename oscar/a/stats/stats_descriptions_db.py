#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: galm
#
########################################################################################################################
#                                                                                                                      #
# This module defines the stats aggregator text DB interface (Currently SQLite) and implements it
#                                                                                                                      #
########################################################################################################################

import sqlite3 as sqlite
from stats_queue_objects import formatExceptionInfo
from enums import AggregationConsolidationFunctionType, VariableTypes, AggregationCounterType
from counter_descriptor import CounterDescriptor, CounterProperty, DataSetArchaive
import os


# === Globals =====================================================================================

FILE_NAME_TIMESTAMP_FORMAT = "%A-%d%B%Y-%H%M-%s"
SQLITE_EXTENTION = ".sqlite"
FILE_NAME_PREFIX = ""
PER_SECOND_STR = "ps"

# === Help Classes =====================================================================================

class DBQuery(object):
    """
    A class that contains both a query and parameters
    """
    def __init__ (self, queryStr, paramsList):
        self.myQueryStr = queryStr
        self.myParamsList = paramsList

# === Implementations =====================================================================================

class SQLiteDescriptorsDB(object):

    #logger - dah
    #dbFilesOutputPath - the output directory for the db files
    #dbFilesBaseName - the prefix of the dbs' file names
    def __init__ (self):
        pass

    #logger - dah
    #dbFilesOutputPath - the output directory for the db files
    #dbFilesBaseName - the prefix of the dbs' file names
    def init (self, logger, dbFilesOutputPath, dbFilesBaseName):
        #Initialize member functions
        self.myDbFilesOutputPath = dbFilesOutputPath
        self.mySqliteDbFilesBaseName = FILE_NAME_PREFIX+dbFilesBaseName
        self.myLogger = logger
        self.myCreatedStatus = False
        self.myLogger.debug2("SQLiteDescriptorsDB initialized")

    #Close cursor and db connection
    def closeDBConnection (self):
        self.myCur.close()
        self.myCon.close()
        self.myCur = None
        self.myCon = None
        self.myLogger.debug2("SQLiteDescriptorsDB connection is closed")

    # newCounters contains the diff between the previous run and this one
    # countersDBInfo contains all the counters
    def createDB (self, countersDBInfo, timeStamp, newCounters, previousCountersDB=None):
        #Check that the DB isn't already created
        if self.myCreatedStatus:
            self.myLogger.error("SQLiteDescriptorsDB.createDB() was called twice for one instance - ilegal")
            return 6885196
        else:
            self.myCreatedStatus = True

        self.myLogger.debug2("SQLiteDescriptorsDB createDB was called")
        self.myCountersDBInfo = countersDBInfo

        # If this is true there aren't any previously known counters - the tables must be created
        #createNewDB = (len(newCounters) == len(countersDBInfo))
        if not previousCountersDB:
            #Format the db's file path/name
            self.myTimeStampString = timeStamp.strftime(FILE_NAME_TIMESTAMP_FORMAT)
            self.myFileName = os.path.join(self.myDbFilesOutputPath,self.mySqliteDbFilesBaseName+self.myTimeStampString+SQLITE_EXTENTION)
        else:
            self.myFileName = previousCountersDB
    
        #Connect to the db - not in the 'if' scope
        #Connect to the db - creates it
        if not self.connectToDb():
            self.myLogger.error("SQLite Connect to DB failed")
            return 152348
        else:
            self.myLogger.debug2("SQLiteDescriptorsDB connected")
        
        queryCreate9 = 'CREATE TABLE counterUISettings (counterID INTEGER PRIMARY KEY, counterDevisionValue INTEGER, counterUnitsStr VARCHAR(20), counterUnitsTimeSpanStr VARCHAR(20))'
        #Table columns were changed - drop the old table and re create it
        if previousCountersDB:
            isTableExistQuery = "SELECT name FROM sqlite_master WHERE type='table' AND name='counterUISettings'"
            ################# Check if the table exist #######################
            self.myCur.execute(isTableExistQuery)
            checkTableResult = self.myCur.fetchall()
            if 0!=len(checkTableResult):
                ################# If it exists drop it #######################
                queryDropUITable = "DROP TABLE counterUISettings"
                queries = [DBQuery(queryDropUITable,[])]
                #Execute the query
                if not self.__executeSQLiteQueryArray(queries):
                    self.myLogger.error("Descriptos db creation failed. Couldn't drop table counterUISettings")
                    return 57562157
            ################# Recreate the table #######################
            queries = [DBQuery(queryCreate9,[])]
            #Execute the query
            if not self.__executeSQLiteQueryArray(queries):
                self.myLogger.error("Descriptos db creation failed. Couldn't re create table counterUISettings")
                return 57562158
        # Create tables if needed
        if not previousCountersDB:
            #Defaults are not saved since we have the counters real configurations in the DB
            #Create DB tables
            queryCreate1 = 'CREATE TABLE counterID (counterID INTEGER PRIMARY KEY, counterPath VARCHAR(250), counterName VARCHAR(100), counterProcessName VARCHAR(50), counterVariableType VARCHAR(25), counterType VARCHAR(25), isRate INTEGER, metaCounterArithmeticExpression VARCHAR(50), commMethod VARCHAR(20))'
            queryCreate2 = 'CREATE TABLE counterDescriptions (counterID INTEGER PRIMARY KEY, counterShortDesc VARCHAR(1000), isOverride INTEGER)'
            queryCreate3 = 'CREATE TABLE counterSamplingRate (counterID INTEGER PRIMARY KEY, counterSamplingRate INTEGER)'
    
            #queryCreate4 = 'CREATE TABLE properties (counterID INTEGER, propName VARCHAR(100), propType VARCHAR(25),  PRIMARY KEY (propName, counterID))' 
            queryCreate5 = 'CREATE TABLE counterPropertiesInt (counterID INTEGER, propName VARCHAR(100), propVal INTEGER, PRIMARY KEY (propName, counterID))' 
            queryCreate6 = 'CREATE TABLE counterPropertiesString (counterID INTEGER, propName VARCHAR(100), propVal VARCHAR(500), PRIMARY KEY (propName, counterID))' 
            queryCreate7 = 'CREATE TABLE rrdFilesMapping (counterID INTEGER, filePath VARCHAR(500), PRIMARY KEY (counterID))' 
            queryCreate8 = 'CREATE TABLE counterArchaives (counterID INTEGER, consolidationFunction VARCHAR(10), errorsAllowed NUMERIC, consolidationSpan INTEGER, numberOfRowsToKeep INTEGER)' 
            queries = [DBQuery(queryCreate1,[]), DBQuery(queryCreate2,[]), DBQuery(queryCreate3,[]), DBQuery(queryCreate5,[]), DBQuery(queryCreate6,[]), DBQuery(queryCreate7,[]), DBQuery(queryCreate8,[]), DBQuery(queryCreate9,[])]

            #Execute the queries - create the DB
            if not self.__executeSQLiteQueryArray(queries):
                self.myLogger.error("Descriptos db creation failed. Couldn't execute create sql commands")
                return 57562154

        self.myLogger.debug2("SQLiteDescriptorsDB tables created successfully")

        #log this following command - the structure of the DB
        query = "SELECT * FROM sqlite_master"
        self.myCur.execute(query)
        dbInfo = self.myCur.fetchall()
        self.myLogger.debug2("SQLiteDescriptorsDB tables created. Running SELECT * FROM sqlite_master -> %s" % str(dbInfo))
      
        #Template DB queris for each counter
        queryInsert1 = 'INSERT INTO counterID (counterID, counterPath, counterName, counterProcessName, counterVariableType, counterType, isRate, metaCounterArithmeticExpression, commMethod) VALUES(?, ?, ?, ?, ?,?, ?, ?, ?)'
        queryInsert2 = 'INSERT INTO counterDescriptions (counterID , counterShortDesc, isOverride) VALUES(?, ?, ?)'
        queryInsert3 = 'INSERT INTO counterSamplingRate (counterID , counterSamplingRate) VALUES(?, ?)'
        #queryInsert4 = 'INSERT INTO properties (counterID, propName, propType) VALUES(?, ?, ?)'
        queryInsert5 = 'INSERT INTO counterPropertiesInt (counterID, propName, propVal) VALUES(?, ?, ?)' 
        queryInsert6 = 'INSERT INTO counterPropertiesString (counterID, propName, propVal) VALUES(?, ?, ?)' 
        queryInsert8 = 'INSERT INTO counterArchaives (counterID, consolidationFunction, errorsAllowed, consolidationSpan, numberOfRowsToKeep) VALUES(?, ?, ?,?,?)' 
        queryInsert9 = 'INSERT INTO counterUISettings (counterID, counterDevisionValue, counterUnitsStr, counterUnitsTimeSpanStr) VALUES(?,?,?,?)'
        queries = []

        #Use the templated DB queris for each new counter (Other counters are already in the DB)
        for counter in newCounters.values():
            if counter.myIsRate:
                isRateVal = 1
            else:
                isRateVal = 0
            queries.append(DBQuery(queryInsert1, [counter.myCounterId, counter.myCounterPath, counter.myCounterSamplingName, counter.myCounterProcess, counter.myVariableType, counter.myCounterType, isRateVal, counter.myMetaCounterExpression, counter.myCommMethod]))
            if counter.myCounterShortDescriptionString:
                #If the string is different than "" it means it had a value before any sampling occured - hence it came as an override from the counters list file
                counter.myCounterDescriptionIsOverride = 1 #1 - True, 0 - False
            else:
                counter.myCounterDescriptionIsOverride = 0

            queries.append(DBQuery(queryInsert2, [counter.myCounterId, counter.myCounterShortDescriptionString, counter.myCounterDescriptionIsOverride]))
            queries.append(DBQuery(queryInsert3, [counter.myCounterId, counter.mySamplingRate]))
            if counter.myPresentCounterPerSecond:
                #Devide by Sampling Rate
                queries.append(DBQuery(queryInsert9, [counter.myCounterId, counter.mySamplingRate, counter.myMeasuredUnits, PER_SECOND_STR]))
            else:
                #Devide by 1
                queries.append(DBQuery(queryInsert9, [counter.myCounterId, 1, counter.myMeasuredUnits, '']))
            
            #Properties - Prop Id is chosen using python's hash
            for prop in counter.myProperties:
                #queries.append(DBQuery(queryInsert4, [counter.myCounterId, property.myName, property.myVariableType]))
                if prop.myVariableType == VariableTypes.INTEGER: 
                    queries.append(DBQuery(queryInsert5, [counter.myCounterId, prop.myName, prop.myValue]))
                elif prop.myVariableType == VariableTypes.STRING: 
                    queries.append(DBQuery(queryInsert6, [counter.myCounterId, prop.myName, prop.myValue]))

            #Insert all archaives
            for archaive in counter.myArchaives:
                queries.append(DBQuery(queryInsert8, [counter.myCounterId, archaive.myArchaiveType, archaive.myErrorsAllowed, archaive.myConsolidationSpan, archaive.myRowsToKeep]))


        if not self.__executeSQLiteQueryArray(queries):
            self.myLogger.error("Descriptos db creation failed. Couldn't execute insert sql commands")
            return 72954
        self.myLogger.debug2("SQLiteDescriptorsDB data saved successfully")

        return 0

    #Finds previous sqlite files
    def getPreviousDbPath (self):
        #Search for an old DB file 
        list_of_files = [f for f in os.listdir(self.myDbFilesOutputPath) if f.lower().endswith(SQLITE_EXTENTION)]
        return list_of_files

    #Reads the counters meta-data from the DB and returns a dictionary of counter descriptors
    def getConfigurationsFromDB(self):
        """
            Only loads relevant data i.e. don't care about counterUISettings
        """
        list_of_files = self.getPreviousDbPath()
        if len(list_of_files)>0:
            if len(list_of_files)>1:
                self.myLogger.error("Too many sqlite files in the output directory. There should be one or none")
                return None
            else:
                #This is the file to work with
                self.myFileName = os.path.join(self.myDbFilesOutputPath,list_of_files[0])
        else:
            self.myLogger.debug2("No sqlite files found - no previous configurations")
            cleanConfigurations = {}
            return cleanConfigurations

        if not self.connectToDb():
            self.myLogger.error("SQLite Connect to DB failed")
            return None
        else:
            self.myLogger.debug2("SQLiteDescriptorsDB connected")
        
        #Template DB queris for each counter
        queryGet0 = 'SELECT * FROM sqlite_master'
        queryGet1 = 'SELECT * FROM counterID'
        queryGet2 = 'SELECT * FROM counterDescriptions'
        queryGet3 = 'SELECT * FROM counterSamplingRate'
        #queryGet4 = 'SELECT * FROM properties'
        queryGet5 = 'SELECT * FROM counterPropertiesInt'
        queryGet6 = 'SELECT * FROM counterPropertiesString' 
        queryGet8 = 'SELECT * FROM counterArchaives' 
        #queryGet9 = 'SELECT * FROM counterUISettings' 

        #Create the counter descriptor objects
        resultDictionary = {}      
        query = ""      
        try:
            #Log
            query = queryGet0
            self.myCur.execute(query)
            countersTuplesList = self.myCur.fetchall()
            self.myLogger.debug2("sqlite_master query = %s" % str(countersTuplesList))
            
            #Get all counters
            query = queryGet1
            self.myCur.execute(query)
            countersTuplesList = self.myCur.fetchall()
            #Create objects
            for counter in countersTuplesList:
                counterObj = CounterDescriptor()
                isRateValue = counter[6] >0 #booleans represented as integers
                counterObj.init(-1, counter[1], counter[3], counter[2], counter[5], counter[4], isRateValue, "", [],[], counter[7], counter[8], False, "", None)
                resultDictionary[counter[0]]  = counterObj

            #Get Descriptions
            query = queryGet2
            self.myCur.execute(query)
            descriptionsTuplesList = self.myCur.fetchall()
            for desc in descriptionsTuplesList:
                if desc[1] is None:
                    description = ""
                else:
                    description = desc[1]
                resultDictionary[desc[0]].myCounterShortDescriptionString = description
                resultDictionary[desc[0]].myCounterDescriptionIsOverride = desc[2]
            
            #Get Sampling Rate
            query = queryGet3
            self.myCur.execute(query)
            counterSampleClassTuplesList = self.myCur.fetchall()

            for counterSample in counterSampleClassTuplesList:
                resultDictionary[counterSample[0]].mySamplingRate = counterSample[1]
            
            #Get Properties
            """query = queryGet4
            self.myCur.execute(query)
            counterPropertiesTuplesList = self.myCur.fetchall()
            for prop in counterPropertiesTuplesList:
                propObj = CounterProperty()
                propObj.init(prop[1], prop[2], 0)
                resultDictionary[prop[0]].myProperties.append(propObj)"""

            #Get Properties' values
            #integers
            query = queryGet5
            self.myCur.execute(query)
            counterPropertiesIntTuplesList = self.myCur.fetchall()
            for val in counterPropertiesIntTuplesList:
                counterProperties = resultDictionary[val[0]].myProperties
                propObj = CounterProperty()
                propObj.init(val[1], VariableTypes.INTEGER, val[2])
                counterProperties.append(propObj)

                    
            #strings
            query = queryGet6
            self.myCur.execute(query)
            counterPropertiesStringTuplesList = self.myCur.fetchall()
            for val in counterPropertiesStringTuplesList:
                counterProperties = resultDictionary[val[0]].myProperties
                propObj = CounterProperty()
                propObj.init(val[1], VariableTypes.STRING, val[2])
                counterProperties.append(propObj)

            #Archaives
            query = queryGet8
            self.myCur.execute(query)
            counterArchaivesTuplesList = self.myCur.fetchall()
            for archaive in counterArchaivesTuplesList:
                archObj = DataSetArchaive()
                archObj.init(archaive[1], archaive[2], archaive[3], archaive[4])
                resultDictionary[archaive[0]].myArchaives.append(archObj)

            self.closeDBConnection()

            return resultDictionary
        except:
            self.closeDBConnection()
            self.myLogger.error("UNExpected exception was raised during sqlite query execution. Query: %s. Exception info: %s" % (query, formatExceptionInfo()))
            return None

    def updateDB(self, countersToUpdate):
        if not self.myCreatedStatus:
            self.myLogger.error("Descriptors update db failed. Bad state - function update called before create")
            return 927731
        
        queryInsert1 = 'UPDATE counterID SET metaCounterArithmeticExpression=? WHERE counterID=?'
        queryCheckForExistance = 'SELECT * FROM counterUISettings WHERE counterID=%s'
        
        queries = []
        for counter in countersToUpdate.values():
            self.myCur.execute(queryCheckForExistance % str(counter.myCounterId))
            checkCounterResult = self.myCur.fetchall()
            if 0!=len(checkCounterResult):
                queryInsert9 = 'UPDATE counterUISettings SET counterDevisionValue=?, counterUnitsStr=?, counterUnitsTimeSpanStr=? WHERE counterID=?'
            else:
                #NOTICE the parameters order is different
                queryInsert9 = 'INSERT INTO counterUISettings (counterDevisionValue, counterUnitsStr, counterUnitsTimeSpanStr, counterID) VALUES(?,?,?,?)'
            queries.append(DBQuery(queryInsert1, [counter.myMetaCounterExpression, counter.myCounterId]))
            if counter.myPresentCounterPerSecond:
                #Devide by Sampling Rate
                queries.append(DBQuery(queryInsert9, [counter.mySamplingRate, counter.myMeasuredUnits, PER_SECOND_STR, counter.myCounterId]))
            else:
                #Devide by 1
                queries.append(DBQuery(queryInsert9, [1, counter.myMeasuredUnits, "", counter.myCounterId]))

        if not self.__executeSQLiteQueryArray(queries):
            self.myLogger.error("Descriptors update db failed. Couldn't execute create sql commands")
            return 154
        self.myLogger.debug2("Descriptors update db succeeded")
        return 0


    def setCounterRRDFileMapping(self, counterId, counterRRDFilePath):
        query = 'INSERT INTO rrdFilesMapping (counterID, filePath) VALUES(?, ?)'
        queries = [DBQuery(query, [counterId, counterRRDFilePath])]
        if not self.__executeSQLiteQueryArray(queries):
            self.myLogger.error("Descriptos db - setCounterRRDFileMapping failed. Couldn't execute insert sql command. CounterID = %d CounterRRDFilePath=%s" % (counterId, counterRRDFilePath))
            return 208264
        self.myLogger.debug2("Descriptos db - setCounterRRDFileMapping succeeded. CounterID = %d CounterRRDFilePath=%s" % (counterId, counterRRDFilePath))
        return 0

    def getRRDFilesMapping (self):
        queryGet1 = 'Select counterID, filePath FROM rrdFilesMapping'
        try:
            self.myCur.execute(queryGet1)
            tuplesList = self.myCur.fetchall()
            resultDictionary = {}            
            for counterMapping in tuplesList:
                resultDictionary[counterMapping[0]]  = counterMapping[1]

            return resultDictionary
        except:
            self.myLogger.error("UNExpected exception was raised during sqlite query execution. Query: %s. Exception info: %s" % (queryGet1, formatExceptionInfo()))
            return None


    def connectToDb (self):
        try:
            if hasattr(self, 'myCon'): 
                if self.myCon: 
                    self.myLogger.error("SQLite connectToDB. An attempt to connect to the DB was made twice")
                    return False

            self.myLogger.debug1("Connecting to " + self.myFileName)
            self.myCon = sqlite.connect(self.myFileName)
            self.myCur = self.myCon.cursor()
            return True
        except:
            self.myLogger.error("UNExpected exception during SQLite connectToDB. Exception info: %s" % formatExceptionInfo())
            return False

    #Updates the counters description in the DB. Once every run. If and only if it wasn't overriden
    def updateDescriptions (self, counterID, counterDescription):
        # 0 - means it wasn't overriden by configurations
        if 0 == self.myCountersDBInfo[counterID].myCounterDescriptionIsOverride:
            queryUpdate = 'UPDATE counterDescriptions SET counterShortDesc=? where counterID=?'
            if not self.__executeSQLiteQueryArray([DBQuery(queryUpdate, [counterID, counterDescription])]):
                self.myLogger.error("Error updating counter's description. Couldn't execute insert sql command")
                return 72954

            #Mark it as updated - this won't change in the DB
            self.myCountersDBInfo[counterID].myCounterDescriptionIsOverride = 1
        return 0

    def setLogger (self, logger):
        self.myLogger = None
        self.myLogger = logger

    def __executeSQLiteQueryArray (self, queries):
        
        try:
            for queryObj in queries:
                queryExecuted = queryObj
                #If params list length = 0 it still executes OK
                self.myCur.execute(queryObj.myQueryStr, queryObj.myParamsList)
            self.myCon.commit()
            return True
        except:
            self.myLogger.error("UNExpected exception was raised during sqlite query execution. Exception info: %s" % (formatExceptionInfo()))
            self.myLogger.error("Query: %s Num of params: %d" % (queryExecuted.myQueryStr, len(queryExecuted.myParamsList)))
            #self.myCon.rollback() - dangerous and uneccessary since the file will be thrown. It might help debugging
            return False
