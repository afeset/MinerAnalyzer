
import os
import sys
import socket
import re
import json

import time
import email.utils  # for formatdate
import datetime

import pprint
import traceback

import django
import django.http
import django.conf
import django.template
import django.template.loader
import django.conf

import topperData
import systemStatusData
import siteListData
import fakeData
import loggers

import a.sys.sys_web.parameters
import auth_conf
from   a.sys.sys_web.server.authentication.views import redirectIfNotAuthenticated

@loggers.viewLogging
@redirectIfNotAuthenticated(auth_conf.env)
def try1(request):


    s  = "<pre>"
    s += "Django says: the time is " + email.utils.formatdate(timeval=None, localtime=True) + ".\n";
    s += "os.getcwd()=%s\n" % os.getcwd() ;
    s += "sys.path()=%s\n" % str(sys.path) ;
    s += "sys.modules['django'].__file__=%s\n" % str(sys.modules['django'].__file__) ;
    s += "time.daylight=%s\n" % time.daylight


    s += "\n"

    envKeys = os.environ.keys()
    envKeys.sort();
    for x in envKeys:
        s += "%-10s = '%s'\n" % (x , os.environ[x])
    s += "\n"

    s += "ROOT_DIR=%s\n" % str( django.conf.settings.A_APPLICATION_ROOT_DIR)
    s += "TEMPLATE_DIRS=%s\n" % str( django.conf.settings.TEMPLATE_DIRS)
    s += "</pre>"

    response = django.http.HttpResponse(s) 

    return response

def getCommonContextVars(request):

    contextVars = {}
    contextVars['hostName'] = socket.gethostname()
    contextVars['userName'] = auth_conf.engine.getUsernameFromRequest(request)
    contextVars['sessionId'] = auth_conf.engine.getSessionIdFromRequest(request)
    # TODO: change to true when Peak functionality will be implemented
    contextVars['showPeak'] = "true"

    debugVars = {}
    debugVars['disableServerPolling'] = django.conf.settings.A_PARAMETERS.getBooleanParameterAsStr("disable-server-polling", False)
    debugVars['enable'] = django.conf.settings.A_PARAMETERS.getBooleanParameterAsStr("debug-client-app", False)

    contextVars['debug'] = debugVars

    return { 'a' : contextVars }

@loggers.viewLogging
@redirectIfNotAuthenticated(auth_conf.env)
def system(request):
    # Build template context 
    contextVars = getCommonContextVars(request) 
    context = django.template.RequestContext( request, contextVars )
    a.sys.sys_web.server.log.logContextVars(loggers.accessLogger, contextVars)

    # Calc the response 
    template = django.template.loader.get_template('mng_web_client_app/system.html')
    response = django.http.HttpResponse(template.render(context)) 

    return response

def getInvalidSessionResponse():
    response = { "always": {
                     "result": {
                         "value": -1,
                         "message": "Invalid session ID"
                     }
                 }
               }
    s = json.dumps(response, indent=4)
    httpResponse = django.http.HttpResponse(s)
    httpResponse['Cache-Control']  = 'no-cache'
    httpResponse['Content-Type']   = 'application/json'
    
    return httpResponse

@loggers.viewLogging
def apiSystem(request):

    if not auth_conf.engine.isRequestAuthenticated(request):
        loggers.mainLogger.warning("Accessing apiSystem without authorized user")
        return getInvalidSessionResponse()

    loggers.accessLogger.info("\n")

    # Log the request 
    loggers.apiLogger.info("-" * 80)
    loggers.apiLogger.info("-" * 80)
    loggers.apiLogger.info("REQUEST: [%s] '%s'" % (request.method , request.get_full_path() ))
    loggers.apiLogger.info("REQUEST: is_secure=%s  is_ajax=%s"   % ( request.is_secure(), request.is_ajax() ) )

    # Log GET parameters (POST method is not used)
    for item in sorted( request.GET.items(), key=lambda t: t[0]):
        loggers.apiLogger.info("REQUEST: GET: '%s' = '%s'" % (item[0], item[1]) )

    loggers.apiLogger.info("\n")

    # Get request paramaters dictionary 
    requestParamsDict = request.GET;

    # Decode request params into sections params
    sectionsParams = decodeSystemApiSectionsParams(requestParamsDict) 
        
    resultAlways = apiSystemProcessAlways(request, sectionsParams)

    resultSections = []
    for (sectionIndex, sectionParams) in enumerate(sectionsParams):
        resultSections.append ( apiSystemProcessSection(sectionIndex, sectionParams) )
        
    result = { 
        'always' : resultAlways,
        'sections' : resultSections,
    }    
                
    s = ""                
    s += json.dumps(result, sort_keys=True, indent=4)
    
    # Log the result
    loggers.apiLogger.info("RESULT: %s" % s )

    loggers.apiLogger.info("RESULT: --- END ---\n")

    # Build the response 
    response = django.http.HttpResponse(s)
    response['Content-Length'] = str( len(s) )
    response['Cache-Control']  = 'no-cache'
    response['Content-Type']   = 'application/json'
    
    return response


def decodeSystemApiSectionsParams(requestParamsDict):

    # Use sorted request keys to ensure consistet behaviour in case of duplicate params 
    requestKeys = requestParamsDict.keys()
    requestKeys.sort()

    # Convert the request dictionary to request param list
    # Conisider only values that have section and 
    sectionIndex = 0
    sectionsParams = []
    while True:

        # Calc section name
        sectionName = "section%s" % sectionIndex

        # If section name does not exist in the request params, we are done
        if not (sectionName in requestParamsDict):
            break;

        # Section exists, scan all paramaters and gather all this section params into a list
        # Append empty dictionary at the end of the section params list
        sectionsParams.append ( { } )
        for key in requestKeys:
            # Look for paramters that have <name><number> and number equals section number
            match = re.match(r"^(.*\D)(\d+)$", key)
            if match:
                name   = match.group(1)
                index  = int( match.group(2) )
                if index == sectionIndex:
                    # Paramaters belongs to this section, add it to the last dictionary
                    sectionsParams[-1][name] = requestParamsDict[key]
                
         
        sectionIndex += 1

    # Done
    return sectionsParams

class systemApiSectionParamsDecoder():
    def __init__(self, sectionParams):
        self.sectionParams = sectionParams;

    def getParam(self, paramName):
        return self.sectionParams[paramName]

    def setParam(self, paramName, paramValue):
        self.sectionParams[paramName] = str(paramValue)

    def getIntParam(self, paramName):
        # return int(self.sectionParams[paramName])
        return  int( float (self.sectionParams[paramName]) ) # workaround - sometimes we get floats here. yak

    def isParamExist(self, paramName):
        return paramName in self.sectionParams

    def getReportType(self):
        return self.getParam('reportType')

    def getDataType(self):
        return self.getParam('dataType')

    def getDataSubType(self):
        return self.getParam('dataSubType')

    def getSiteList(self):
        return self.getParam('siteList')

    def getDataSeriesList(self):
        if self.isParamExist('dataSeriesList'):
            return self.getParam('dataSeriesList')
        else:
            return None

    def getGroupBy(self):
        return self.getParam('groupBy')

    def getCount(self):
        #topCountName = 'topCount'                   ### disable 'topCount' workaround
        #if self.isParamExist(topCountName):
        #    return self.getIntParam(topCountName)

        return self.getIntParam('count')

    def getTimeParam(self, paramName):
        paramVal = self.getIntParam(paramName)
        return paramVal

    def getFromTime(self): 
        return self.getTimeParam('from')

    def getToTime(self): 
        return self.getTimeParam('to')

    def getInterval(self):
        return self.getIntParam('interval')

    def getIntervalUnit(self):
        '''Returns inteval units seconds or month seconds is default'''
        if self.isParamExist('intervalUnit'):
            return self.getParam('intervalUnit')
        else:
            return "seconds"

    def getStartRank(self):       
        return self.getIntParam('startRank') if self.isParamExist('startRank') else 0

    def getCurrentListVersion(self):
        return self.getIntParam('currentListVersion') if self.isParamExist('currentListVersion') else -1

    def getPercentiles(self):
        '''Get list of percentiles used in pareto over time report'''
        percentilesStr = self.getParam("percentiles")
        percentiles = map(int, percentilesStr.split(","))
        return percentiles

    def getParetoDataType(self):
        if self.isParamExist('paretoDataType'):
            return self.getParam('paretoDataType')
        else:
            return "volume"

    def getDistributionType(self):
        return self.getParam("distributionType")

    def getAggregationType(self):
        if self.isParamExist("aggregationType"):
            return self.getParam("aggregationType")
        else:
            return None
def getCurrentTime():
    if django.conf.settings.A_PARAMETERS.hasParameter("fake-current-time"):
        currentTime = django.conf.settings.A_PARAMETERS.getIntParameter("fake-current-time", 0)
    else:
        currentTime = int(time.time())

    if django.conf.settings.A_PARAMETERS.hasParameter("current-time-delta"):
        currentTime += django.conf.settings.A_PARAMETERS.getIntParameter("current-time-delta", 0)
    return currentTime

def apiSystemProcessAlways(request, sectionsParams):

    resultResult = {
        'message' : 'fine',
        'value'   : 0,
    }

    parameters = django.conf.settings.A_PARAMETERS.getDictionary().copy()
    try:
        del parameters['secret_key']
    except:
        pass
    resultSectionDebug = {
        'message' : "debug msgs",
        'parameters' : parameters,
        'sessionId' : auth_conf.engine.getSessionIdFromRequest(request),
        'URL' : request.build_absolute_uri(),
        'clientIP': request.META['REMOTE_ADDR']
    }

    resultSystemTime = { }

    currentTime = getCurrentTime()

    resultSystemTime['currentTime'] = currentTime
    
    if django.conf.settings.A_PARAMETERS.hasParameter("timezone-name") and django.conf.settings.A_PARAMETERS.hasParameter("timezone-offset"):
        resultSystemTime['timeZone']       = django.conf.settings.A_PARAMETERS.getParameter("timezone-name", "")
        resultSystemTime['timeZoneOffset'] = django.conf.settings.A_PARAMETERS.getIntParameter("timezone-offset", 0)
    else:
        # Make sure time module tz data is updated, in case tz was changed recently
        time.tzset()
        if time.localtime(currentTime).tm_isdst and time.daylight:
            # Summer time
            resultSystemTime['timeZone']       = time.tzname[1]
            resultSystemTime['timeZoneOffset'] = -time.altzone
        else:
            # Standard time time
            resultSystemTime['timeZone']       = time.tzname[0]
            resultSystemTime['timeZoneOffset'] = -time.timezone

    resultSystemTime['timeFormat'] = 'US'
    
    resultSystem = { 
        'time' : resultSystemTime,
    }
        
    result = {
        'result'       : resultResult,
        'sectionDebug' : resultSectionDebug,
        'system'       : resultSystem,
    }

    return result


def apiSystemProcessSection(sectionIndex, sectionParams):
    result = { }

    resultSectionDebug = { }
    resultSectionDebug['message'] = "debug message"
    resultSectionDebug['params']  = sectionParams
    
    loggers.apiLogger.info("SECTION[%d] PARAMS: %s\n" % (sectionIndex, json.dumps(sectionParams, sectionParams, sort_keys=True, indent=4) ) )

    try:
        section = sectionParams['section']
        if section == 'report' or section == 'reports':
            result['reports'] = apiSystemProcessSectionReport(sectionParams)
        elif section == 'system':
            result['system'] = apiSystemProcessSectionSystem(sectionParams)
        elif section == 'siteList':
            result['siteList'] = apiSystemProcessSectionSiteList(sectionParams)
    
    except:
        loggers.mainLogger.exception("Exception occurred")    
        loggers.accessLogger.exception("Exception occurred")    
        loggers.apiLogger.exception("Exception occurred")    
        resultSectionDebug['traceback'] = traceback.format_exc().split("\n")

    result['sectionDebug'] = resultSectionDebug
    return result

def apiSystemProcessSectionReport(sectionParams):

    paramsDecoder = systemApiSectionParamsDecoder(sectionParams)

    result = { }

    reportType = paramsDecoder.getReportType()
    if reportType == 'overTime':
        result['overTime'] = apiSystemProcessSectionReportOverTime(paramsDecoder)
    elif reportType == 'top':
        result['top'] = apiSystemProcessSectionReportTop(paramsDecoder)
    elif reportType == 'recent':
        result['recent'] = apiSystemProcessSectionReportRecent(paramsDecoder)
    elif reportType == 'pareto':
        result['pareto'] = apiSystemProcessSectionReportPareto(paramsDecoder)
    elif reportType == 'distribution':
        result['distribution'] = apiSystemProcessSectionReportDistribution(paramsDecoder)
        

    return result

# === Overtime reports ================================================================================================

def apiSystemProcessSectionReportOverTime(paramsDecoder):
    result = { }

    dataType = paramsDecoder.getDataType()
    if dataType == 'BW':
        result['BW'] = apiSystemProcessSectionReportOverTimeBW(paramsDecoder)
    elif dataType == 'sessions':
        result['sessions'] = apiSystemProcessSectionReportOverTimeSessions(paramsDecoder)
    elif dataType == 'viewTime':
        result['viewTime'] = apiSystemProcessSectionReportOverTimeViewTime(paramsDecoder)
    elif dataType == 'L2BW':
        result['L2BW'] = apiSystemProcessSectionReportOverTimeL2BW(paramsDecoder)
    elif dataType == 'pareto':
        result['pareto'] = apiSystemProcessSectionReportOverTimePareto(paramsDecoder)
    elif dataType == 'bitRate':
        result['bitRate'] = apiSystemProcessSectionReportOverTimeBitRate(paramsDecoder)

    return result

def apiSystemProcessSectionReportOverTimeBW(paramsDecoder):
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()

    interval = paramsDecoder.getInterval()
    intervalUnit = paramsDecoder.getIntervalUnit()
    aggregationType = paramsDecoder.getAggregationType()

    return getDataProviderFunction('reportOverTimeBW')(from_, to_, interval, intervalUnit, aggregationType) 
  
def apiSystemProcessSectionReportOverTimeSessions(paramsDecoder):
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()

    interval = paramsDecoder.getInterval()
    intervalUnit = paramsDecoder.getIntervalUnit()
    aggregationType = paramsDecoder.getAggregationType()

    return getDataProviderFunction('reportOverTimeSessions')(from_, to_, interval, intervalUnit, aggregationType) 

def apiSystemProcessSectionReportOverTimeViewTime(paramsDecoder):
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()

    interval = paramsDecoder.getInterval()
    intervalUnit = paramsDecoder.getIntervalUnit()
    aggregationType = paramsDecoder.getAggregationType()

    retVal = getDataProviderFunction('reportOverTimeViewTime')(from_, to_, interval, intervalUnit, aggregationType)
    return retVal 

def apiSystemProcessSectionReportOverTimeL2BW(paramsDecoder):
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()

    interval = paramsDecoder.getInterval()
    intervalUnit = paramsDecoder.getIntervalUnit()
    aggregationType = paramsDecoder.getAggregationType()

    retVal = getDataProviderFunction('reportOverTimeL2BW')(from_, to_, interval, intervalUnit, aggregationType)
    return retVal 

def apiSystemProcessSectionReportOverTimePareto(paramsDecoder):
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()

    interval = paramsDecoder.getInterval()
    intervalUnit = paramsDecoder.getIntervalUnit()

    percentiles = paramsDecoder.getPercentiles()

    groupBy = paramsDecoder.getGroupBy()
    result = {}
    if groupBy == "subscribers":
        result['subscribers'] = getDataProviderFunction('reportOverTimeParetoBySubscribers')(from_, to_, interval, intervalUnit, percentiles)
    elif groupBy == "titles":
        result['titles'] = getDataProviderFunction('reportOverTimeParetoByTitles')(from_, to_, interval, intervalUnit, percentiles)
    return result 

def apiSystemProcessSectionReportOverTimeBitRate(paramsDecoder):
    dataSubType = paramsDecoder.getDataSubType()
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()

    interval = paramsDecoder.getInterval()
    intervalUnit = paramsDecoder.getIntervalUnit()

    result = {
        dataSubType: getDataProviderFunction('reportOverTimeBitRate')(dataSubType, from_, to_, interval, intervalUnit,\
            paramsDecoder.getSiteList(), paramsDecoder.getDataSeriesList())
    }
    return result

# === top reports =====================================================================================================
def apiSystemProcessSectionReportTop(paramsDecoder):
    result = { }

    groupBy    = paramsDecoder.getGroupBy()
    if groupBy == 'sites':
        result['sites'] = apiSystemProcessSectionReportTopSites(paramsDecoder)
    elif groupBy == 'titles':
        result['titles'] = apiSystemProcessSectionReportTopTitles(paramsDecoder)
    elif groupBy == 'subscribers':
        result['subscribers'] = apiSystemProcessSectionReportTopSubscribers(paramsDecoder)

    return result

# Top sites
def apiSystemProcessSectionReportTopSites(paramsDecoder):

    from_ =  paramsDecoder.getFromTime()
    to_   =  paramsDecoder.getToTime()

    result = { }
    count_   = paramsDecoder.getCount()

    dataType = paramsDecoder.getDataType()
    if dataType == 'volume':
        result['volume'] = apiSystemProcessSectionReportTopSitesSortByVolume(from_, to_, count_, paramsDecoder)
    elif dataType == 'sessions':
        result['sessions'] = apiSystemProcessSectionReportTopSitesSortBySessions(from_, to_, count_, paramsDecoder)
    elif dataType == 'viewTime':
        result['viewTime'] = apiSystemProcessSectionReportTopSitesSortByViewTime(from_, to_, count_, paramsDecoder)

    return result

def apiSystemProcessSectionReportTopSitesSortByVolume(from_, to_, count_, paramsDecoder):

    # Get data from data provider 
    result =  getDataProviderFunction('reportTopSitesSortByVolume')(from_, to_, count_) 

    # Done
    return result

def apiSystemProcessSectionReportTopSitesSortBySessions(from_, to_, count_, paramsDecoder):

    # Get data from data provider 
    result = getDataProviderFunction('reportTopSitesSortBySessions')(from_, to_, count_) 
    
    # Done
    return result

def apiSystemProcessSectionReportTopSitesSortByViewTime(from_, to_, count_, paramsDecoder):

    # Get data from data provider 
    result =  getDataProviderFunction('reportTopSitesSortByViewTime')(from_, to_, count_) 

    # Done
    return result

# Top titles
def apiSystemProcessSectionReportTopTitles(paramsDecoder):

    from_ =  paramsDecoder.getFromTime()
    to_   =  paramsDecoder.getToTime()

    count_    = paramsDecoder.getCount()
    startRank = paramsDecoder.getStartRank()

    result = { }
    dataType = paramsDecoder.getDataType()
    if dataType == 'volume':
        result['volume'] = apiSystemProcessSectionReportTopTitlesSortByVolume(from_, to_, count_, startRank, paramsDecoder)
    elif dataType == 'sessions':
        result['sessions'] = apiSystemProcessSectionReportTopTitlesSortBySessions(from_, to_, count_, startRank, paramsDecoder)
    elif dataType == 'viewTime':
        result['viewTime'] = apiSystemProcessSectionReportTopTitlesSortByViewTime(from_, to_, count_, startRank, paramsDecoder)

    return result

def apiSystemProcessSectionReportTopTitlesSortByVolume(from_, to_, count_, startRank, paramsDecoder):

    # Get data from data provider 
    result =  getDataProviderFunction('reportTopTitlesSortByVolume')(from_, to_, count_, startRank) 
    
    # Done
    return result

def apiSystemProcessSectionReportTopTitlesSortBySessions(from_, to_, count_, startRank, paramsDecoder):

    # Get data from data provider 
    result = getDataProviderFunction('reportTopTitlesSortBySessions')(from_, to_, count_, startRank) 

    # Done
    return result

def apiSystemProcessSectionReportTopTitlesSortByViewTime(from_, to_, count_, startRank, paramsDecoder):

    # Get data from data provider 
    result = getDataProviderFunction('reportTopTitlesSortByViewTime')(from_, to_, count_, startRank) 

    # Done
    return result

# Top subscribers
def apiSystemProcessSectionReportTopSubscribers(paramsDecoder):

    from_ =  paramsDecoder.getFromTime()
    to_   =  paramsDecoder.getToTime()

    count_    = paramsDecoder.getCount()
    startRank = paramsDecoder.getStartRank()

    result = { }
    dataType = paramsDecoder.getDataType()
    if dataType == 'volume':
        result['volume'] = apiSystemProcessSectionReportTopSubscribersSortByVolume(from_, to_, count_, startRank, paramsDecoder)
    elif dataType == 'sessions':
        result['sessions'] = apiSystemProcessSectionReportTopSubscribersSortBySessions(from_, to_, count_, startRank, paramsDecoder)
    elif dataType == 'viewTime':
        result['viewTime'] = apiSystemProcessSectionReportTopSubscribersSortByViewTime(from_, to_, count_, startRank, paramsDecoder)

    return result

def apiSystemProcessSectionReportTopSubscribersSortByVolume(from_, to_, count_, startRank, paramsDecoder):

    # Get data from data provider 
    result =  getDataProviderFunction('reportTopSubscribersSortByVolume')(from_, to_, count_, startRank) 

    # Done
    return result

def apiSystemProcessSectionReportTopSubscribersSortBySessions(from_, to_, count_, startRank, paramsDecoder):

    # Get data from data provider 
    result = getDataProviderFunction('reportTopSubscribersSortBySessions')(from_, to_, count_, startRank) 

    # Done
    return result

def apiSystemProcessSectionReportTopSubscribersSortByViewTime(from_, to_, count_, startRank, paramsDecoder):

    # Get data from data provider 
    result = getDataProviderFunction('reportTopSubscribersSortByViewTime')(from_, to_, count_, startRank) 
    
    # Done
    return result




# -- recent reports
def apiSystemProcessSectionReportRecent(paramsDecoder):
    result = { }

    dataType = paramsDecoder.getDataType()
    if dataType == 'titles':
        result['titles'] = apiSystemProcessSectionReportRecentTitles(paramsDecoder)

    return result

# Recent titles
def apiSystemProcessSectionReportRecentTitles(paramsDecoder):
    count_   = paramsDecoder.getCount()

    # Get data from data provider 
    result = getDataProviderFunction('reportRecentTitles')(count_) 

    # Done
    return result
   
# === Pareto reports =================================================================================================
def apiSystemProcessSectionReportPareto(paramsDecoder):
    groupBy = paramsDecoder.getGroupBy()
    result = {}
    if groupBy == 'subscribers':
        result['subscribers'] = apiSystemProcessSectionReportParetoBySubscribers(paramsDecoder)
    elif groupBy == 'titles':
        result['titles'] = apiSystemProcessSectionReportParetoByTitles(paramsDecoder)
    return result

def apiSystemProcessSectionReportParetoBySubscribers(paramsDecoder):
    dataType = paramsDecoder.getDataType()
    result = {}
    if dataType == 'volume':
        result['volume'] = apiSystemProcessSectionReportParetoBySubscribersVolume(paramsDecoder)
    return result


def apiSystemProcessSectionReportParetoByTitles(paramsDecoder):
    dataType = paramsDecoder.getDataType()
    result = {}
    if dataType == 'volume':
        result['volume'] = apiSystemProcessSectionReportParetoByTitlesVolume(paramsDecoder)
    return result

def apiSystemProcessSectionReportParetoBySubscribersVolume(paramsDecoder):
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()
    result = getDataProviderFunction('paretoBySubscribersVolume')(from_, to_)
    return result
    
def apiSystemProcessSectionReportParetoByTitlesVolume(paramsDecoder):
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()
    result = getDataProviderFunction('paretoByTitlesVolume')(from_, to_)
    return result
    
# ==== Distribution Reports ======
def apiSystemProcessSectionReportDistribution(paramsDecoder):
    distributionType = paramsDecoder.getDistributionType()
    result = {}
    if distributionType == "time":
        result["time"] = apiSystemProcessSectionReportTimeDistribution(paramsDecoder)
    return result

def apiSystemProcessSectionReportTimeDistribution(paramsDecoder):
    dataType =  paramsDecoder.getDataType()
    from_    =  paramsDecoder.getFromTime()
    to_      =  paramsDecoder.getToTime()
    count_   =  paramsDecoder.getCount()
    interval =  paramsDecoder.getInterval()
    result = {}
    if dataType == "BW":
        result["BW"] = getDataProviderFunction('timeDistributionBW')(from_, to_, count_, interval)
    elif dataType == "sessions":
        result["sessions"] = getDataProviderFunction('timeDistributionSessions')(from_, to_, count_, interval)
    elif dataType == "viewTime":
        result["viewTime"] = getDataProviderFunction('timeDistributionViewTime')(from_, to_, count_, interval)
    elif dataType == "subscribers":
        result["subscribers"] = getDataProviderFunction('timeDistributionSubscribers')(from_, to_, count_, interval)
    return result

# --- system

def apiSystemProcessSectionSystem(sectionParams):
    result = { }

    section = sectionParams['type']
    if section == 'shortStatus':
        result['status'] = apiSystemProcessSectionSystemStatus(sectionParams, short = True)

    return result

def apiSystemProcessSectionSystemStatus(sectionParams, short = False):
    result = { }

    # Get health status and append them to data, if not empty 
    resultHealth = getDataProviderFunction('systemStatusHealth')()
    if resultHealth:
        result['health'] = resultHealth

    # Get cache status and append it to data, if not empty 
    resultCache = getDataProviderFunction('systemStatusCache')() 
    if resultCache:
        result['cache'] = resultCache

    # Get network status and append them to data, if not empty 
    resultNetwork = getDataProviderFunction('systemStatusNetwork')()
    if resultNetwork:
        result['networking'] = resultNetwork

    # Get software status and append them to data, if not empty 
    resultSoftware = getDataProviderFunction('systemStatusSoftware')()
    if resultSoftware:
        result['software'] = resultSoftware

    # Get media signature pack version and append them to data, if not empty 
    resultMSP = getDataProviderFunction('systemStatusMediaSignaturePack')()
    if resultMSP:
        result['mediaSignaturePack'] = resultMSP
    
    # Get general system information (e.g. hostname)
    resultSystem = getDataProviderFunction('systemStatusSystem')()
    if resultSystem:
        result['system'] = resultSystem

    return result

    # Get alerts and append them to data, if not empty 
    resultAlerts = getDataProviderFunction('systemStatusAlerts')() 
    if resultAlerts:
        result['alerts'] = resultAlerts

# --- site list

def apiSystemProcessSectionSiteList(sectionParams):

    paramsDecoder = systemApiSectionParamsDecoder(sectionParams)

    clientListVersion = paramsDecoder.getCurrentListVersion() 

    # Get data from data provider 
    result = getDataProviderFunction('siteList')(clientListVersion) 

    # Done
    return result

# === data providers map ==============================================================================================

def initDataProvidersMap(fakeList):

    # Map real data provider
    global dataProviderMap
    dataProviderMap = { }
    
    # True over time data providers 
    dataProviderMap['reportOverTimeBW']        = topperDataProvider.reportOverTimeBW
    dataProviderMap['reportOverTimeSessions']  = topperDataProvider.reportOverTimeSessions
    dataProviderMap['reportOverTimeViewTime']  = topperDataProvider.reportOverTimeViewTime
    dataProviderMap['reportOverTimeL2BW']      = topperDataProvider.reportOverTimeL2BW

    dataProviderMap['reportOverTimeParetoBySubscribers'] = topperDataProvider.reportOverTimeParetoBySubscribers
    dataProviderMap['reportOverTimeParetoByTitles']      = topperDataProvider.reportOverTimeParetoByTitles

    dataProviderMap['reportOverTimeBitRate'] = topperDataProvider.reportOverTimeBitRate

    # True top sites data providers 
    dataProviderMap['reportTopSitesSortByVolume']   = topperDataProvider.reportTopSitesSortByVolume
    dataProviderMap['reportTopSitesSortBySessions'] = topperDataProvider.reportTopSitesSortBySessions
    dataProviderMap['reportTopSitesSortByViewTime'] = topperDataProvider.reportTopSitesSortByViewTime

    # True top titles data providers 
    dataProviderMap['reportTopTitlesSortByVolume']   = topperDataProvider.reportTopTitlesSortByVolume
    dataProviderMap['reportTopTitlesSortBySessions'] = topperDataProvider.reportTopTitlesSortBySessions
    dataProviderMap['reportTopTitlesSortByViewTime'] = topperDataProvider.reportTopTitlesSortByViewTime

    # True top subscribers data providers 
    dataProviderMap['reportTopSubscribersSortByVolume']   = topperDataProvider.reportTopSubscribersSortByVolume  
    dataProviderMap['reportTopSubscribersSortBySessions'] = topperDataProvider.reportTopSubscribersSortBySessions
    dataProviderMap['reportTopSubscribersSortByViewTime'] = topperDataProvider.reportTopSubscribersSortByViewTime

    # True recent titles data provider
    dataProviderMap['reportRecentTitles']   = topperDataProvider.reportRecentTitles  
    
    # Pareto reports
    dataProviderMap['paretoBySubscribersVolume'] = topperDataProvider.reportParetoBySubscribersVolume
    dataProviderMap['paretoByTitlesVolume']      = topperDataProvider.reportParetoByTitlesVolume

    # True time distribution
    dataProviderMap['timeDistributionBW']          = topperDataProvider.reportTimeDistributionBW
    dataProviderMap['timeDistributionSessions']    = topperDataProvider.reportTimeDistributionSessions
    dataProviderMap['timeDistributionViewTime']    = topperDataProvider.reportTimeDistributionViewTime
    dataProviderMap['timeDistributionSubscribers'] = topperDataProvider.reportTimeDistributionSubscribers

    # True system status
    dataProviderMap['systemStatusHealth']   = systemStatusDataProvider.systemStatusHealth
    dataProviderMap['systemStatusCache']    = systemStatusDataProvider.systemStatusCache
    dataProviderMap['systemStatusNetwork']  = systemStatusDataProvider.systemStatusNetwork
    dataProviderMap['systemStatusSoftware'] = systemStatusDataProvider.systemStatusSoftware
    dataProviderMap['systemStatusAlerts']   = systemStatusDataProvider.systemStatusAlerts
    dataProviderMap['systemStatusMediaSignaturePack'] = systemStatusDataProvider.systemStatusMediaSignaturePack
    dataProviderMap['systemStatusSystem']   = systemStatusDataProvider.systemStatusSystem

    # True site list
    dataProviderMap['siteList']   = siteListDataProvider.siteList

    # Fake over time reports    
    if 'reportOverTime' in fakeList:
        dataProviderMap['reportOverTimeBW']       = fakeDataProvider.reportOverTimeBW
        dataProviderMap['reportOverTimeSessions'] = fakeDataProvider.reportOverTimeSessions
        dataProviderMap['reportOverTimeViewTime'] = fakeDataProvider.reportOverTimeViewTime
        dataProviderMap['reportOverTimeL2BW']     = fakeDataProvider.reportOverTimeL2BW
    if 'reportParetoOverTime' in fakeList:
        dataProviderMap['reportOverTimeParetoBySubscribers'] = fakeDataProvider.reportOverTimeParetoBySubscribers
        dataProviderMap['reportOverTimeParetoByTitles']      = fakeDataProvider.reportOverTimeParetoByTitles

    if 'reportBitRateOverTime' in fakeList:
        dataProviderMap['reportOverTimeBitRate'] = fakeDataProvider.reportOverTimeBitRate

    # Fake top sites
    if 'reportTopSites' in fakeList:
        dataProviderMap['reportTopSitesSortByVolume']   = fakeDataProvider.reportTopSitesSortByVolume
        dataProviderMap['reportTopSitesSortBySessions'] = fakeDataProvider.reportTopSitesSortBySessions
        dataProviderMap['reportTopSitesSortByViewTime'] = fakeDataProvider.reportTopSitesSortByViewTime
    
    # Fake top titles
    if 'reportTopTitles' in fakeList:
        dataProviderMap['reportTopTitlesSortByVolume']   = fakeDataProvider.reportTopTitlesSortByVolume
        dataProviderMap['reportTopTitlesSortBySessions'] = fakeDataProvider.reportTopTitlesSortBySessions
        dataProviderMap['reportTopTitlesSortByViewTime'] = fakeDataProvider.reportTopTitlesSortByViewTime
            
    # Fake top subscribers
    if 'reportTopSubscribers' in fakeList:
        dataProviderMap['reportTopSubscribersSortByVolume']   = fakeDataProvider.reportTopSubscribersSortByVolume
        dataProviderMap['reportTopSubscribersSortBySessions'] = fakeDataProvider.reportTopSubscribersSortBySessions
        dataProviderMap['reportTopSubscribersSortByViewTime'] = fakeDataProvider.reportTopSubscribersSortByViewTime

    # Fake recent titles data provider
    if 'reportRecentTitles' in fakeList:
        dataProviderMap['reportRecentTitles']   = fakeDataProvider.reportRecentTitles  

    # Fake pareto distribution
    if 'reportPareto' in fakeList:
        dataProviderMap['paretoBySubscribersVolume'] = fakeDataProvider.reportParetoBySubscribersVolume
        dataProviderMap['paretoByTitlesVolume']      = fakeDataProvider.reportParetoByTitlesVolume

    # Fake time distribution
    if 'reportDistribution' in fakeList:
        dataProviderMap['timeDistributionBW']          = fakeDataProvider.reportTimeDistributionBW
        dataProviderMap['timeDistributionSessions']    = fakeDataProvider.reportTimeDistributionSessions
        dataProviderMap['timeDistributionViewTime']    = fakeDataProvider.reportTimeDistributionViewTime
        dataProviderMap['timeDistributionSubscribers'] = fakeDataProvider.reportTimeDistributionSubscribers

    # Fake system status
    if 'systemStatus' in fakeList:
        dataProviderMap['systemStatusHealth']   = fakeDataProvider.systemStatusHealth
        dataProviderMap['systemStatusCache']    = fakeDataProvider.systemStatusCache
        dataProviderMap['systemStatusNetwork']  = fakeDataProvider.systemStatusNetwork
        dataProviderMap['systemStatusSoftware'] = fakeDataProvider.systemStatusSoftware
        dataProviderMap['systemStatusAlerts']   = fakeDataProvider.systemStatusAlerts
        dataProviderMap['systemStatusMediaSignaturePack'] = fakeDataProvider.systemStatusMediaSignaturePack
        dataProviderMap['systemStatusSystem']   = fakeDataProvider.systemStatusSystem

    # Fake system status zero
    if 'systemStatusZero' in fakeList:
        dataProviderMap['systemStatusHealth']   = fakeDataProvider.systemStatusHealthZero
        dataProviderMap['systemStatusCache']    = fakeDataProvider.systemStatusCacheZero
        dataProviderMap['systemStatusNetwork']  = fakeDataProvider.systemStatusNetworkZero
        dataProviderMap['systemStatusSoftware'] = fakeDataProvider.systemStatusSoftwareZero
        dataProviderMap['systemStatusAlerts']   = fakeDataProvider.systemStatusAlertsZero
        dataProviderMap['systemStatusMediaSignaturePack'] = fakeDataProvider.systemStatusMediaSignaturePackZero
        dataProviderMap['systemStatusSystem']   = fakeDataProvider.systemStatusSystemZero

    # Fake site list
    if 'siteList' in fakeList:
        dataProviderMap['siteList']   = fakeDataProvider.siteList


def getDataProviderFunction(dataProviderName):
    global dataProviderMap
    rv =  dataProviderMap[dataProviderName]
    return rv

# === main ============================================================================================================


fakeList = []
#fakeList.append('reportOverTime')
#fakeList.append('reportTopSites')
#fakeList.append('reportTopTitles')
#fakeList.append('reportTopSubscribers')
#fakeList.append('reportRecentTitles')
#fakeList.append('reportPareto')
#fakeList.append('systemStatus')
#fakeList.append('systemStatusZero')
#fakeList.append('siteList')

fakeList.extend(django.conf.settings.A_PARAMETERS.getParameter("fake-list", "").split(" "))

# Init dirs
logsDir          = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "logs")
topperReportsDir = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "topper_reports", "reports")
systemStatusDir  = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "sys_status")

# Init logger

a.sys.sys_web.server.log.logStartData(loggers.mainLogger)

# Init Data providers
uxParameters = a.sys.sys_web.parameters.Parameters(fileName = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "ux-parameters.json"))
topperDataProvider = topperData.DataProvider(topperReportsDir , uxParameters, loggers.apiLogger, loggers.uxLogger) 

systemStatusDataProvider = systemStatusData.DataProvider(systemStatusDir , loggers.apiLogger, loggers.mainLogger) 
siteListDataProvider     = siteListData.DataProvider(loggers.apiLogger, loggers.mainLogger) 

fakeDataProvider   = fakeData.DataProvider()

# Init data providers mapping
initDataProvidersMap(fakeList)


