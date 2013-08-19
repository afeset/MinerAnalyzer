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
#                                                                                                               
# This module retrieves stats counters data for the display
#                                                                                                                   
########################################################################################################################

import re
import os, sys
import time
import traceback
import subprocess
import sqlite3 as sqlite
from enums import VariableTypes

DB_CONNECTION_OBJECT = 0
DB_CURSOR_OBJECT = 1
DB_COUNTER_ID_IS_RATE = 4
MIN_NUMBER_OF_SAMPLES_IN_RESPONSE = 10
TEN_MINUTES_SECONDS = 600
ONE_MINUTE_SECONDS = 60
ONE_DAY_SECONDS = 86400
FACTOR = 1000
META_COUNTERS_SUPPORTED_OPERATORS = ['+', '-','*','/']
MAX_NUMBER_OF_SAMPLES_TO_RETURN_PER_COUNTER = 5000
RRD_ROOT_RELATIVE_PATH = "rrd"

counterValueRegex = re.compile('([0-9]+:.*?)\n', re.IGNORECASE | re.DOTALL)
rrdFileStepRegex = re.compile('step[ ]*=[ ]*([0-9]+?)\n', re.IGNORECASE | re.DOTALL)

#Assumptions: 
# 1. The requesting script has knowledge of the positions of both the sqlite meta data file and the rrd files
# 2. This module is stateless
# 3. The rrd files are placed relatively to the sqlite file as in the product

########## Help Functions ########

def formatExceptionInfo(level = 6):
    error_type, error_value, trbk = sys.exc_info()
    tb_list = traceback.format_tb(trbk, level)    
    s = "Traceback:%s\nDescription: %s \nError: %s \n" % (error_type.__name__, tb_list, error_value)
    return s

def __connectToDb (sqliteDbFilePath):
        try:
            myCon = sqlite.connect(sqliteDbFilePath)
            myCur = myCon.cursor()
            return (myCon, myCur)
        except:
            print formatExceptionInfo()
            return None


#Close cursor and db connection
def __closeDBConnection (con, cur):
    cur.close()
    con.close()
    cur = None
    con = None

#returns a list of all possible properties
def __getPropertyType (propName, sqliteDbFilePath, logger):
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, __getPropertyType was called with uninitialized dbConObjects")
            return None
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        query = 'SELECT * FROM counterPropertiesInt WHERE propName=?'        
        cur.execute(query, [propName])
        queryResultInt = cur.fetchall()
        query = 'SELECT * FROM counterPropertiesString WHERE propName=?'
        cur.execute(query, [propName])
        queryResultStr = cur.fetchall()
        __closeDBConnection(con, cur)
        if not queryResultStr and not queryResultInt:
            logger.notice("In counter_data_fetcher, __getPropertyType did not find any match for property: %s" % propName)
            return None
        if not queryResultInt:
            return VariableTypes.STRING
        else:
            return VariableTypes.INTEGER
    except:
        logger.error("In counter_data_fetcher, __getPropertyType - UNExpectd exception, details: %s" % formatExceptionInfo())
        return None

#returns the path to this counters rrd file
def getCountersRRDFilePath (counterId, sqliteDbFilePath, logger):
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, getCountersRRDFilePath was called with uninitialized dbConObjects. DB file path is " + str(sqliteDbFilePath))
            return None
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        
        #run select query
        query = 'SELECT filePath FROM rrdFilesMapping WHERE counterID = ?'
        cur.execute(query, [str(counterId)])
        
        queryResult = cur.fetchall()
        __closeDBConnection(con, cur)
        
        if not queryResult:
            logger.error("In counter_data_fetcher, getCountersRRDFilePath did not find any match for counterId: %s" % str(counterId))
            return None

        result = queryResult[0][0]
        
        #return the list
        return result
    except:
        logger.error("In counter_data_fetcher, getCountersRRDFilePath - UNExpectd exception, details: %s" % formatExceptionInfo())
        return None

#returns the counters meta-counter expression if exists
def getCountersMetaCounterArithmeticExpression (counterId, sqliteDbFilePath, logger):
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, getCountersMetaCounterArithmeticExpression was called with uninitialized dbConObjects")
            return None
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        
        #run select query
        query = 'SELECT metaCounterArithmeticExpression FROM counterID WHERE counterID = ?'
        cur.execute(query, [str(counterId)])
        
        queryResult = cur.fetchall()
        __closeDBConnection(con, cur)
        
        if not queryResult:
            logger.error("In counter_data_fetcher, getCountersMetaCounterArithmeticExpression did not find any match for counterId: %s" % str(counterId))
            return None

        result = queryResult[0][0]
        
        #return the list
        return result
    except:
        logger.error("In counter_data_fetcher, getCountersRRDFilePath - UNExpectd exception, details: %s" % formatExceptionInfo())
        return None

######## INTERFACE ##############

# returns a list of all process names
def getAllProcesses (sqliteDbFilePath, logger):
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, getAllProcesses was called with uninitialized dbConObjects")
            return None
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        #run select proccessName command
        query = 'SELECT counterProcessName FROM counterID'
        cur.execute(query)
        queryResult = cur.fetchall()
        __closeDBConnection(con, cur)
        resultList = []
        for proc in queryResult:
            if not proc[0] in resultList:
                resultList.append(str(proc[0]))
        
        #return the list
        return sorted(resultList)
    except:
        logger.error("In counter_data_fetcher, getAllProcesses - UNExpectd exception, details: %s" % formatExceptionInfo())
        return None

#returns a tuple of all the processes counter paths and ids
def getProcessCounters (processName, sqliteDbFilePath, logger):
    connectionOpen = False
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, getProcessCounters was called with uninitialized dbConObjects")
            return None

        connectionOpen = True
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        
        #run select query
        query = 'SELECT counterProcessName, counterPath,counterName, counterID, isRate, counterType FROM counterID WHERE counterProcessName = ?'
        cur.execute(query, [processName])
        queryResult = cur.fetchall()

        resultList = []
        for counter in queryResult:

            #run another query for the counters UI configurations
            query = 'SELECT counterID,counterDevisionValue,counterUnitsStr,counterUnitsTimeSpanStr FROM counterUISettings WHERE counterID = ?'
            cur.execute(query, [counter[3]])
            uiConfigqueryResult = cur.fetchall()

            #Is rate?
            if 1 == counter[DB_COUNTER_ID_IS_RATE]:
                rate_counter_suffix = '-rate'
            else:
                rate_counter_suffix = ''

            #Check for UI config
            if len(uiConfigqueryResult)==0:
                logger.notice("In counter_data_fetcher, getProcessCounters - counter has no UI configurations. Counter process name: %s counterPath: %s counterName: %s counterId: %s" % (str(counter[0]), str(counter[1]), str(counter[2]), str(counter[3])))
                counterUnitsStr = "N/A"
                counterUnitsTimeSpanStr = "N/A"
            else:
                counterUnitsStr = uiConfigqueryResult[0][2]
                counterUnitsTimeSpanStr = uiConfigqueryResult[0][3]
            counterDescriptors = ""
            if counter[5] == "COUNTER":
                counterDescriptors+= "(APS"
                if len(counterUnitsStr)>0:
                    counterDescriptors+= "-"+counterUnitsStr+counterUnitsTimeSpanStr
                counterDescriptors+= ")"
            counterDescriptors+= rate_counter_suffix

            counterPath = os.path.join(counter[0], counter[1], counter[2]+counterDescriptors)

            resultToAppend = [str(counterPath), str(counter[3])]
            resultList.append(resultToAppend)
        #close the db connection
        __closeDBConnection(con, cur)
        connectionOpen = False
        #return the list
        return sorted(resultList)
    except:
        logger.error("In counter_data_fetcher, getProcessCounters - UNExpectd exception, details: %s" % formatExceptionInfo())
        if connectionOpen:
            try:
                __closeDBConnection(con, cur)
            except:
                logger.error("In counter_data_fetcher, getProcessCounters - exception handler tried to close DB connection and failed, details: %s" % formatExceptionInfo())
        return None

#returns a list of all possible properties
def getAllProperties (sqliteDbFilePath, logger):
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, getAllProperties was called with uninitialized dbConObjects")
            return None
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        query = 'SELECT propName FROM counterPropertiesInt'
        cur.execute(query)
        queryResultInt = cur.fetchall()
        query = 'SELECT propName FROM counterPropertiesString'
        cur.execute(query)
        queryResultStr = cur.fetchall()
        __closeDBConnection(con, cur)
        if not queryResultStr or not queryResultInt:
            logger.notice("In counter_data_fetcher, getAllProperties. No properties found")
            return None
        queryResult = []
        for prop in queryResultInt:
            if not prop[0] in queryResult:
                resToAppend = ['int',str(prop[0])]
                if not resToAppend in queryResult:
                    queryResult.append(resToAppend)
        for prop in queryResultStr:
            if not prop[0] in queryResult:
                resToAppend = ['str',str(prop[0])]
                if not resToAppend in queryResult:
                    queryResult.append(resToAppend)
        
        #return the list
        return sorted(queryResult)
    except:
        logger.error("In counter_data_fetcher, getAllProperties - UNExpectd exception, details: %s" % formatExceptionInfo())
        return None


#return a list of tuples containing (counterPath, counterName, counterId)  for the counters specified by their IDs
def __queryCountersByIDs (idsList, sqliteDbFilePath, logger):
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, __queryCountersByIDs was called with uninitialized dbConObjects")
            return None
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        resultList = []

        inString = "("+','.join(idsList)+")"
        query = 'SELECT counterProcessName, counterPath,counterName, counterID FROM counterID WHERE counterID IN ' + inString
        cur.execute(query)
        queryResult = cur.fetchall()
        __closeDBConnection(con, cur)

        for counter in queryResult:
            counterPath = os.path.join(counter[0], counter[1], counter[2])            
            tpl = [str(counterPath), str(counter[3])]
            resultList.append(tpl)
        
        #return the list
        return resultList
    except:
        logger.error("In counter_data_fetcher, __queryCountersByIDs - UNExpectd exception, details: %s" % formatExceptionInfo())
        return None

def __queryCountersByProperties (query, params, sqliteDbFilePath, logger):
    try:
        #Connect to sql db
        dbConObjects = __connectToDb(sqliteDbFilePath)
        if dbConObjects is None:
            logger.error("In counter_data_fetcher, __queryCountersByProperties was called with uninitialized dbConObjects")
            return None
        con = dbConObjects[DB_CONNECTION_OBJECT]
        cur = dbConObjects[DB_CURSOR_OBJECT]
        cur.execute(query, params)
        queryResult = cur.fetchall()
        __closeDBConnection(con, cur)
        if not queryResult:
            return None
        return queryResult
    except:
        logger.error("In counter_data_fetcher, __queryCountersByProperties - UNExpectd exception, details: %s" % formatExceptionInfo())
        return None

def getCountersByProperty (propName, sqliteDbFilePath, logger, propValueMin=None, propValueMax=None, propSubStr=None):
    propType = __getPropertyType(propName, sqliteDbFilePath, logger)
    if not propType:
        logger.error("In counter_data_fetcher, getCountersByProperty. __getPropertyType returned an ilegal value - property type is unknown. PropName:%s" % propName)
        return None
    
    #STRING
    if propType == VariableTypes.STRING:
        if propSubStr is None:
            logger.error("In counter_data_fetcher, getCountersByProperty. propSubStr is None - can't proceed")
            return None
        else:
            query = 'SELECT counterID, propVal FROM counterPropertiesString WHERE propName = ?'
            results = __queryCountersByProperties(query, [propName], sqliteDbFilePath, logger)
            idsList = []
            for result in results:
                if str(result[1]).find(propSubStr) > -1:
                    idsList.append(str(result[0]))

            countersToReturn = __queryCountersByIDs (idsList, sqliteDbFilePath, logger)
            return sorted(countersToReturn)

    #INTEGER
    if propType == VariableTypes.INTEGER:
        if propValueMin is None or propValueMax is None:
            logger.error("In counter_data_fetcher, getCountersByProperty. propvalues are not set - can't proceed")
            return None
        else:
            query = 'SELECT counterID, propVal FROM counterPropertiesInt WHERE propName=?'
            results = __queryCountersByProperties(query, [propName], sqliteDbFilePath, logger)
            idsList = []
            for result in results:
                if int(result[1])>=int(propValueMin) and int(result[1])<=int(propValueMax):
                    idsList.append(str(result[0]))

            countersToReturn = __queryCountersByIDs (idsList, sqliteDbFilePath, logger)

            return sorted(countersToReturn)

    logger.error("In counter_data_fetcher, getCountersByProperty. Unexpected error - an ilegal prop variable type received")
    return None

def __executeRRDCommand (command):
        commandResult = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                         close_fds=True)

        """stderrStr = commandResult.stderr.read()
        if(stderrStr):
            return (False, stderrStr)"""
            #BAD
        stdoutStr = commandResult.stdout.read()
        if(stdoutStr):
            return (True, stdoutStr)
            #OK

        # If we got here it means that no message was presented either in stdout & stderr = BAD - we asked for data
        return None

def __getCountersMetaValue(valueSampled, metaCounterArithmeticExpression, logger):
    result = valueSampled
    if not metaCounterArithmeticExpression:
        return result
    j=0
    while j<len(metaCounterArithmeticExpression):
        operand = ''
        if metaCounterArithmeticExpression[j] in META_COUNTERS_SUPPORTED_OPERATORS:
            operator = metaCounterArithmeticExpression[j]
            j+=1
            while j<len(metaCounterArithmeticExpression) and not metaCounterArithmeticExpression[j] in META_COUNTERS_SUPPORTED_OPERATORS:
                operand+= metaCounterArithmeticExpression[j]
                j+=1
            operandInt = int(operand)
            if '+' == operator:
                result += operandInt
            if '*' == operator:
                result *= operandInt
            if '-' == operator:
                result -= operandInt
            if '/' == operator:
                if operand != 0:
                    result /= operandInt
        else:
            logger.error("Error in meta-counter arithmetic expression - arithmetic expression ignored: %s" % (str(metaCounterArithmeticExpression)))
            return valueSampled
            
    return result

def __parseValue (countersShellOutput, metaCounterArithmeticExpression, logger):

    # TODO(amiry) - DO not compile every time
    # counterValueRegex = re.compile('([0-9]+:.*?)\n', re.IGNORECASE | re.DOTALL)
    counterValues = re.findall(counterValueRegex, countersShellOutput)
    foundFirstVal = False
    #Needed to convert to highcharts long epoch representation
    if len(counterValues) > 0:            
        result = []
        for sample in counterValues:
            indexForSeperation = sample.find(':')
            timeStamp=float(sample[:indexForSeperation])
            if sample[indexForSeperation+1:].find('nan') > -1:
                #Don't need this - output -1
                if not foundFirstVal:
                    continue
                valueSampled=-1
            else:
                valueSampled=float(sample[indexForSeperation+1:])
                foundFirstVal = True
            valueSampled=__getCountersMetaValue(valueSampled, metaCounterArithmeticExpression, logger)
            timeStampLocal=_convertToLocalTime(float(timeStamp))
            timeStampLocal = timeStampLocal*FACTOR
            result.append([timeStampLocal,valueSampled])
        logger.debug1("Received %s, result is %s" % (countersShellOutput, str(result)))
        return result
    else:
        logger.error("In counter_data_fetcher, __parseValue - UNExpectd error, Counter Shell Output: %s" % (countersShellOutput))
        return None

def _convertToLocalTime(timeStampToConvert):
    if time.localtime(timeStampToConvert).tm_isdst and time.daylight:
        return timeStampToConvert-time.altzone
    else:
        return timeStampToConvert-time.timezone

def __parseStep (rrdInfoShellOutput, logger):

    # TODO(amiry) - DO not compile every time
    # rrdFileStepRegex = re.compile('step[ ]*=[ ]*([0-9]+?)\n', re.IGNORECASE | re.DOTALL)
    rrdStep = re.findall(rrdFileStepRegex, rrdInfoShellOutput)
    logger.debug1("In counter_data_fetcher, __parseStep - rrdStep result is: %s" % rrdStep)
    if len(rrdStep) >0:            
        return int(rrdStep[0])
    else:
        logger.error("In counter_data_fetcher, __parseStep - UNExpectd error, Counter Shell Output: %s" % (rrdInfoShellOutput))
        return None

#returns a dictionary where key=timestamp value=counterSampledValue
def getCountersValues (counterId, maxNumOfSamples, startingEpoch, endEpoch, dbRootDir, sqliteDbFilePath, daysBack, rrdtoolExePath, logger):
    try:
        if daysBack or endEpoch or maxNumOfSamples or startingEpoch:
            pass # shut pychecker

        daysBack = int(daysBack)

        rrdSourceFolder = os.path.join(dbRootDir, RRD_ROOT_RELATIVE_PATH)
        #get counters rrd file path
        rrdFilePath = getCountersRRDFilePath (counterId, sqliteDbFilePath, logger)
        metaCounterArithmeticExpression = getCountersMetaCounterArithmeticExpression (counterId, sqliteDbFilePath, logger)

        startTime = int(time.time() - 3600*24*daysBack)
        command = '%s --command \" fetch %s AVERAGE -s %s\"' % (rrdtoolExePath, os.path.join(rrdSourceFolder,rrdFilePath), startTime)
        logger.info("EXECUTE: %s [%d days back]" % (command, daysBack))
        result = __executeRRDCommand(command)
        if result:
            return __parseValue(result[1], metaCounterArithmeticExpression, logger)
        else:
            logger.error("In counter_data_fetcher, getCountersValues. Error while trying to retrieve values of counterId:%s startTime:%d" % (str(counterId), startTime))
            return None

        """
        command = '%s --command \" info %s \"\n' % (rrdtoolExePath, os.path.join(rrdSourceFolder,rrdFilePath))
        startTime = time.time()
        result = __executeRRDCommand(command)
        if result:
            step = __parseStep(result[1], logger)
        else:
            logger.error("In counter_data_fetcher, getCountersValues. Error while trying to retrieve step of counterId:%s endEpoch:%s" % (str(counterId), endEpoch))
            return None

        logger.info("EXECUTE INFO COMMAND: %s. Span %d" % (command, time.time()-startTime))
    
        if not daysBack:
            daysBackEvaluated = 0
        else:
            daysBackEvaluated = eval(daysBack)
        endEpoch -= ONE_DAY_SECONDS*daysBackEvaluated
    
        if endEpoch<startingEpoch:
            logger.error("In counter_data_fetcher, getCountersValues. The specified number of days backward was too big: %s" % (str(daysBackEvaluated)))
            return None

        maxTimeSpan = step*maxNumOfSamples
        newEndEpoch = startingEpoch + maxTimeSpan
        returnedValues = []
        newEndEpoch -= maxTimeSpan
        startingEpoch -= maxTimeSpan
    
        while newEndEpoch <= endEpoch:
            newEndEpoch += maxTimeSpan
            startingEpoch += maxTimeSpan
            if newEndEpoch > endEpoch and startingEpoch<endEpoch:
                newEndEpoch = endEpoch
            
            #Gets the lowest resolution
            command = '%s --command \" fetch %s AVERAGE -s %s -e %s\"' % (rrdtoolExePath, os.path.join(rrdSourceFolder,rrdFilePath), startingEpoch, newEndEpoch)
            logger.info("EXECUTE: %s. Start %d Span %d" % (command, startingEpoch, newEndEpoch-startingEpoch))
            result = __executeRRDCommand(command)
            if result:
                returnedValues.extend(__parseValue(result[1], metaCounterArithmeticExpression, logger))
            else:
                logger.error("In counter_data_fetcher, getCountersValues. Error while trying to retrieve values of counterId:%s startEpoch:%s endEpoch:%s" % (str(counterId), startingEpoch, newEndEpoch))
                return None
    
#       return returnedValues[len(returnedValues)-MAX_NUMBER_OF_SAMPLES_TO_RETURN_PER_COUNTER:]
        logger.info("RESULT: %d samples" % len(returnedValues))
        return returnedValues
        """

    except:
        logger.error("In counter_data_fetcher, getCountersValues. Unexpected error: %s" % __formatExceptionInfo())
        return None

def __formatExceptionInfo(level = 6):
    error_type, error_value, trbk = sys.exc_info()
    tb_list = traceback.format_tb(trbk, level)    
    s = "Error: %s \nDescription: %s \nTraceback: %s" % (error_type.__name__, error_value, str(tb_list))
    return s

#returns events that happened between the two timestamps - to be presented as tags
def getCountersEvents (counterProccess, counterPath, startingEpoch, endEpoch):
    #Next version
    pass
