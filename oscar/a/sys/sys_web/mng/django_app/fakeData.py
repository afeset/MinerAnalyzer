import utils
import time
import math
import siteListData
import loggers
import socket

class DataProvider():
    def __init__(self):
        # Use site list data from the siteListData data provider since it is fully static
        self.siteListDataProvider = siteListData.DataProvider()

    # --- Reports over time     

    def reportOverTimeBW(self, startTime, endTime, interval, intervalUnit, aggregationType=None):
        return self._reportOverTime(startTime, endTime, interval, 5000 * 1000 * 1000, intervalUnit, "avg", aggregationType)

    def reportOverTimeSessions(self, startTime, endTime, interval, intervalUnit, aggregationType=None):
        return self._reportOverTime(startTime, endTime, interval, 1000./300, intervalUnit, "sum", aggregationType)

    def reportOverTimeViewTime(self, startTime, endTime, interval, intervalUnit, aggregationType=None):
        return self._reportOverTime(startTime, endTime, interval, 1000., intervalUnit, "sum", aggregationType)

    def _reportOverTime(self, startTime, endTime, interval, factor, intervalUnit, normalizationType, aggregationType=None, dateFieldName = 'date'):

        potentialPoints = [] 
        servedPoints = [] 
        totalPoints = [] 

        if intervalUnit == 'month':
            # just make it fast
            interval = interval * 30 * 24 * 60 * 60

        if startTime == 0 and endTime == 0 and interval == 0:
            oldestTime = self.getOldestDataTime()
            debugDate = utils.formatUtcTimeAsIsoLocalTime(oldestTime)
            servedPoints.append(   { dateFieldName: oldestTime, 'value': 0 , 'debugDate': debugDate }) 
            potentialPoints.append({ dateFieldName: oldestTime, 'value': 0 , 'debugDate': debugDate }) 
            totalPoints.append(    { dateFieldName: oldestTime, 'value': 0 , 'debugDate': debugDate }) 
        else:
            k = 1
            count_ = 1.0 * (endTime - startTime) / interval
            step   = 0.5 * factor / count_
            val    = 0.5 * factor

            for entryDate in range(startTime, endTime, interval):
                if aggregationType == "max":
                    # we will generate some offset to simulate peak time values
                    # offset is in round minutes
                    offset = (entryDate/24/3600*60) % 3600 + 18 * 3600 + time.timezone
                    date = entryDate + offset
                    calcInterval = 60
                else:
                    date = entryDate
                    calcInterval = interval

                if normalizationType == "avg":
                    norm = calcInterval
                else:
                    norm = 1
                debugDate = utils.formatUtcTimeAsIsoLocalTime(date)
                # add some 24 hours distribution
                # Consider it is sin^2 (no use at night)
                radF = math.pi/24./60./60. # convert seconds to radians
                # Integrate over distribution and normalize to get result at any value of interval parameter
                dist24 = (0.5 * calcInterval * radF - (math.sin(2. * (date + calcInterval) * radF ) -  math.sin(2 * date * radF ))/ 4.) / radF / norm
                servedPoints.append(    { dateFieldName: date * k, 'value': int(dist24 * val *  .2) , 'debugDate': debugDate } )
                potentialPoints.append( { dateFieldName: date * k, 'value': int(dist24 * val *  .6) , 'debugDate': debugDate } )
                totalPoints.append(     { dateFieldName: date * k, 'value': int(dist24 * val * 1.0) , 'debugDate': debugDate  } )
                val += step
        
        result = {}
        result['debug']     = { 'from'  : utils.formatUtcTimeAsIsoLocalTime(startTime), 'to' : utils.formatUtcTimeAsIsoLocalTime(endTime), 'interval' : interval }
        result['potential'] = { 'points': potentialPoints }
        result['served']    = { 'points': servedPoints }
        result['total']     = { 'points': totalPoints }
        return result

    def getOldestDataTime(self):
        # Return 5 years back
        curGmtTime = int(time.time()) + time.timezone
        oldestTime = curGmtTime - 5 * 365 * 24 * 60 * 60
        return oldestTime
        
    def reportOverTimeL2BW(self, startTime, endTime, interval, intervalUnit, aggregationType):
    
        totalPoints = [] 
        videoPoints = [] 
        videoServedPoints = [] 
    
        if startTime == 0 and endTime == 0 and interval == 0:
            oldestTime = self.getOldestDataTime()
            debugDate = utils.formatUtcTimeAsIsoLocalTime(oldestTime)
            videoPoints.append(      { 'date': oldestTime, 'value': 0 , 'debugDate': debugDate }) 
            videoServedPoints.append({ 'date': oldestTime, 'value': 0 , 'debugDate': debugDate }) 
            totalPoints.append(      { 'date': oldestTime, 'value': 0 , 'debugDate': debugDate }) 
        else:
            factor = 5e9
            layer2Overhead = 1.2

            k = 1
            count_ = 1.0 * (endTime - startTime) / interval
            step   = 0.5 * factor / count_
            val    = 0.5 * factor * layer2Overhead

            for entryDate in range(startTime, endTime, interval):
                if aggregationType == "max":
                    # we will generate some offset to simulate peak time values
                    # offset is in round minutes
                    offset = (entryDate/24/3600*60) % 3600 + 18 * 3600 + time.timezone
                    date = entryDate + offset
                    calcInterval = 60
                else:
                    date = entryDate
                    calcInterval = interval
                debugDate = utils.formatUtcTimeAsIsoLocalTime(date)
                # add some 24 hours distribution
                # Consider it is sin^2 (no use at night max use at day time)
                radF = math.pi/24./60./60. # convert seconds to radians
                # Integrate over distribution and normalize to get result at any value of interval parameter
                dist24 = 0.5 - (math.sin(2. * (date + calcInterval) * radF ) -  math.sin(2 * (date) * radF ))/ calcInterval / radF / 4.

                videoServedPoints.append({ 'date': date * k, 'value': int(dist24 * val *  .4) , 'debugDate': debugDate } )
                videoPoints.append(      { 'date': date * k, 'value': int(dist24 * val *  .6) , 'debugDate': debugDate } )
                totalPoints.append(      { 'date': date * k, 'value': int(dist24 * val * 2.0 + val * .2), 'debugDate': debugDate  } )
                val += step
        
        result = {}
        result['debug']     = { 'from'  : utils.formatUtcTimeAsIsoLocalTime(startTime), 'to' : utils.formatUtcTimeAsIsoLocalTime(endTime), 'interval' : interval }
        result['videoServed'] = { 'points': videoServedPoints }
        result['video']       = { 'points': videoPoints }
        result['total']       = { 'points': totalPoints }
        return result

    def reportOverTimeParetoByTitles(self, startTime, endTime, interval, intervalUnit, percentilesValues):
        return self._reportOverTimePareto(startTime, endTime, interval, intervalUnit, percentilesValues, 717125000, 10000)
    def reportOverTimeParetoBySubscribers(self, startTime, endTime, interval, intervalUnit, percentilesValues):
        return self._reportOverTimePareto(startTime, endTime, interval, intervalUnit, percentilesValues, 717125000, 312540)
        
    def _reportOverTimePareto(self, startTime, endTime, interval, intervalUnit, percentilesValues, maxVolume, maxEntities):
        # we will distribute each percentile equaly
        percentileScale = 0.4/len(percentilesValues)
        percentiles = []
        radF = math.pi/24./60./60.
        i = 0
        for p in percentilesValues:
            points = []
            for date in range(startTime, endTime, interval):
                value = maxVolume * (0.5*math.sin(radF * date)**2 + i*percentileScale)
                points.append( {"date": date, "value": int(value) } )
            percentile = { "value": p, "points": points }
            percentiles.append(percentile)
            i += 1
        points = []
        for date in range(startTime, endTime, interval):
            value = maxVolume
            entities = maxEntities
            points.append( {"date": date, "value": int(value), "entities": entities})
        loggers.accessLogger.info("Finish pareto over time")
        return { "percentiles": percentiles, "total": { "points": points }}

    # --- reports top sites

    def reportTopSitesSortByVolume(self, startTime, endTime, count_):
        return self._reportTopSites(startTime, endTime, count_, 20, 1e9)

    def reportTopSitesSortBySessions(self, startTime, endTime, count_):
        return self._reportTopSites(startTime, endTime, count_, 40, 30)

    def reportTopSitesSortByViewTime(self, startTime, endTime, count_):
        return self._reportTopSites(startTime, endTime, count_, 60, 1000)

    def _reportTopSites(self, startTime, endTime, count_, offset, factor):

        entries = [] 
        for index in range(0, min(count_, 201-offset)): # Return maximum 201 sites
            entry = {}
            vol = max(100 - 3 * index, 15 ) * factor / 200. * (endTime-startTime)
            entry['served']    = int(vol * 0.5)
            entry['potential'] = int(vol * 0.7)
            entry['total']     = int(vol * 1.0)
            entry['rank']      = index + 1
            siteId = self.getSite(offset + index)
            entry['siteId'] = siteId
    
            entries.append( entry )
        
        result = {}
        result['entries'] = entries
        # accumulate grandTotal
        sumServed = sum(e['served'] for e in entries)
        sumPotential = sum(e['potential'] for e in entries)
        sumTotal = sum(e['total'] for e in entries)
        result['grandTotal'] = {'total' : int(sumTotal * 1.3),
                                'potential': int(sumPotential * 1.3),
                                'served': int(sumServed * 1.3)
                               }
        result['debug']     = { 'from'  : utils.formatUtcTimeAsIsoLocalTime(startTime), 
                                'to'    : utils.formatUtcTimeAsIsoLocalTime(endTime), 
                                'count' : count_,
                                'len(entries)' : len(entries) 
                              }
    
        return result

    # --- reports top titles

    def reportTopTitlesSortByVolume(self, startTime, endTime, count_, startRank):
        return self._reportTopTitles(startTime, endTime, count_, startRank, 'v', 50 * 1400*1000*1000, 50 * 2*3600, 50)

    def reportTopTitlesSortBySessions(self, startTime, endTime, count_, startRank):
        return self._reportTopTitles(startTime, endTime, count_, startRank, 's', 1000 * 5*1000*1000, 1000*300, 1000)

    def reportTopTitlesSortByViewTime(self, startTime, endTime, count_, startRank):
        return self._reportTopTitles(startTime, endTime, count_, startRank, 'vt', 400*350*1000*1000, 400*1800, 400)

    def _reportTopTitles(self, startTime, endTime, count_, startRank, namePrefix, volumeScale, viewTimeScale, sessionScale):

        entries = [] 
        for index in range(startRank, min(startRank + count_, 31) ): # don't return more than 201 titles
            entry = {}
            entry['name']          = "title-%s%03d" % (namePrefix, index)
            entry['rank']          = index + 1
            entry['siteId']        = self.getSite(index+50)

            titleValue = 2./(1.+index)
            entry['totalVolume']   = int(volumeScale*titleValue)
            entry['totalViewTime'] = int(viewTimeScale*titleValue)
            entry['sessionNumber'] = int(sessionScale*titleValue)
    
            entries.append( entry )
        
        result = {}
        result['entries'] = entries
        result['debug']     = { 'from'  : utils.formatUtcTimeAsIsoLocalTime(startTime),
                                'to'    : utils.formatUtcTimeAsIsoLocalTime(endTime), 
                                'count' : count_, 'startRank' : startRank, 
                                'len(entries)' : len(entries)
                              }
    
        return result

    # --- reports top subscribers

    def reportTopSubscribersSortByVolume(self, startTime, endTime, count_, startRank):
        return self._reportTopSubscribers(startTime, endTime, count_, startRank, 10, 1e9)

    def reportTopSubscribersSortBySessions(self, startTime, endTime, count_, startRank):
        return self._reportTopSubscribers(startTime, endTime, count_, startRank, 20, 1000)

    def reportTopSubscribersSortByViewTime(self, startTime, endTime, count_, startRank):
        return self._reportTopSubscribers(startTime, endTime, count_, startRank, 30, 3600)

    def _reportTopSubscribers(self, startTime, endTime, count_, startRank, magic, scale):

        entries = [] 
        for index in range(startRank, min(startRank + count_, 24) ): # don't return more than 24 titles
            entry = {}
            entry['subscriberId']  = "333.444.%03d.%03d" % (magic, index * 2)
            entry['value']         = int(magic * max( 30 - index, 4) / 30.0 * 10 * scale)
            entry['rank']          = index + 1
            entries.append( entry )
        
        result = {}
        result['entries'] = entries
        result['debug']     = { 'from'  : utils.formatUtcTimeAsIsoLocalTime(startTime),
                                'to'    : utils.formatUtcTimeAsIsoLocalTime(endTime), 
                                'count' : count_, 'startRank' : startRank, 
                                'len(entries)' : len(entries)
                              }
    
        return result


    # --- Report recent titles
    def reportRecentTitles(self, count_):
         
        entries = [] 
        for index in range(0, count_):
            entry = {}
            vol = (100 - 3 * index) * 1000 * 1000
            entry['name']      = "title%03d" % index
            entry['served']    = (index % 2 == 0)
            entry['size']      = (index + 10) * 5000 * 1000
            entry['siteId']    = self.getSite(12 + index)
            entry['time']      =  int( int(time.time() ) - index * 3600 * .075 )
            entry['subscriberId'] =  "10.1.1.%d" % index
    
            entries.append( entry )
        
        result = {}
        result['entries'] = entries
    
        return result


    # --- Report Time Distribution
    def reportTimeDistributionBW(self, from_, to_, count_, interval):
        return self._reportOverTime(0, count_*interval, interval, 5000*1000*1000, "s", "avg", dateFieldName = "time")

    def reportTimeDistributionSessions(self, from_, to_, count_, interval):
        return self._reportOverTime(0, count_*interval, interval, 1000./300, "s", "sum", dateFieldName = "time")

    def reportTimeDistributionViewTime(self, from_, to_, count_, interval):
        return self._reportOverTime(0, count_*interval, interval, 1000, "s", "sum", dateFieldName = "time")

    def reportTimeDistributionSubscribers(self, from_, to_, count_, interval):
        result = self._reportOverTime(0, count_*interval, interval, 50*1000, "s", "avg", dateFieldName = "time")
        # only total data available
        del result["served"]
        del result["potential"]
        return result

    # --- System status

    def systemStatusHealth(self):
        result = {}
        result['overallStatus']     = { 'severity': 'info',  'value': 'OK' }
        #result['cpuUtilization']    = { 'severity': 'info',  'value': 0.25 }
        #result['memoryUtilization'] = { 'severity': 'info',  'value': 0.3 }
        #result['storageStatus']     = { 'severity': 'error', 'value': 'Almost full' }
        return result

    def systemStatusCache(self):
        result = {}
        #result['hitRatio']  = 0.76124
        result['acquired']  = 8000
        result['delivered'] = 6000
        result['stored']    = 12000
        return result

    def systemStatusNetwork(self):
        result = {}
        return result

    def systemStatusSoftware(self):
        result = {}
        result['version']  = "0.0.0.0.00000"
        result['license']  = "to kill"
        return result

    def systemStatusAlerts(self):
        result = []
        #result.append( { "severity" : "warning",  "text" : "Raining",     "time" :   int( time.time() ) - 3600 * 1.6 } )
        #result.append( { "severity" : "critical", "text" : "Out of snow", "time" :   int( time.time() ) - 3600 * 2.5 } )
        return result

    # --- System status zero    

    def systemStatusHealthZero(self):
        result = {}
        result['overallStatus']     = { 'severity': 'info',  'value': 'OK' }
        #result['cpuUtilization']    = { 'severity': 'info',  'value': 0 }
        #result['memoryUtilization'] = { 'severity': 'info',  'value': 0 }
        #result['storageStatus']     = { 'severity': 'info',  'value': 'N/A' }
        return result

    def systemStatusCacheZero(self):
        result = {}
        #result['hitRatio']  = 0
        result['acquired']  = 0
        result['delivered'] = 0
        result['stored']    = 0
        return result

    def systemStatusNetworkZero(self):
        result = {}
        return result

    def systemStatusSoftwareZero(self):
        result = {}
        result['version']  = "0.0.0.0"
        result['license']  = "none"
        #result['sitePack'] = "0.0"
        return result

    def systemStatusAlertsZero(self):
        result = []
        return result

    def systemStatusMediaSignaturePack(self):
        result = {}
        result['version'] = "0.0.0 G00"
        return result

    def systemStatusSystem(self):
        result = {}
        result['hostname'] = socket.gethostname()
        return result

    def systemStatusMediaSignaturePackZero(self):
        result = {}
        result['version'] = "0.0.0 G00"
        return result

    def systemStatusSystemZero(self):
        result = {}
        result['hostname'] = "hostname0000"
        return result


    # --- site list
    def siteList(self, clientListVersion):
        result = self.siteListDataProvider.siteList(clientListVersion)
        return result

    def getSite(self, index):
        sitesList = self.siteList(-1)['entries']
        return sitesList[index%len(sitesList)]['siteId']

    # --- pareto
    def _reportPareto(self, itemScale, valueScale, alpha):
        # We use normalized Lorenz function L(F) = 1 - (1 - F) ** (1 - 1/alpha)
        # and return 21 points of such
        
        entries = []
        numOfSamples = 20
        for i in range(numOfSamples+1):
            F = (1./numOfSamples) * i
            L = 1 - (1 - F) ** (1 - 1./alpha)
            entries.append({'cumItems': int(F*itemScale), 'cumValue': int(L*valueScale)})

        result = { 'debug': { 'alpha': alpha},
                   'entries': entries,
                   'grandTotal': { 'items': itemScale, 'value': valueScale }
                 }
        return result

    def reportParetoBySubscribersVolume(self, from_, to_):
        return self._reportPareto(100*1000, 5*1000*1000*1000, -1.5)

    def reportParetoByTitlesVolume(self, from_, to_):
        return self._reportPareto(10*1000, 5*1000*1000*1000, -2)

    def reportOverTimeBitRate(self, subType, from_, to_, interval, intervalUnit, \
                                    siteList, dataSeries):
        countFactor = 100 if subType=="perTransaction" else 1
        result = {}
        if intervalUnit == 'month':
            # just make it fast
            interval = interval * 30 * 24 * 60 * 60

        datePoints = range(from_, to_, interval)

        dataSeriesList = dataSeries.split(",") if dataSeries else None
        siteFactor = 10 # This is used to differentiate data between different sites
        for site in siteList.split(","):
            siteData = {}
            if not dataSeriesList or 'servedAverage' in dataSeriesList:
                series = [{'value' : 1000000*siteFactor, 'date': date} for date in datePoints]
                siteData['servedAverage'] = series
            if not dataSeriesList or 'servedMax' in dataSeriesList:
                series = [{'value' : 1500000*siteFactor, 'date': date} for date in datePoints]
                siteData['servedMax'] = series
            if not dataSeriesList or 'servedAverageConcurrentSamples' in dataSeriesList:
                series = [{'value' : 10*siteFactor, 'date': date} for date in datePoints]
                siteData['servedAverageConcurrentSamples'] = series
            if not dataSeriesList or 'analyzedAverage' in dataSeriesList:
                series = [{'value' : 800000*siteFactor, 'date': date} for date in datePoints]
                siteData['analyzedAverage'] = series
            if not dataSeriesList or 'analyzedMax' in dataSeriesList:
                series = [{'value' : 1300000*siteFactor, 'date': date} for date in datePoints]
                siteData['analyzedMax'] = series
            if not dataSeriesList or 'analyzedAverageConcurrentSamples' in dataSeriesList:
                series = [{'value' : 10*siteFactor, 'date': date} for date in datePoints]
                siteData['analyzedAverageConcurrentSamples'] = series
            if not dataSeriesList or 'totalAverageConcurrentSamples' in dataSeriesList:
                series = [{'value' : 20*siteFactor, 'date': date} for date in datePoints]
                siteData['totalAverageConcurrentSamples'] = series
            siteFactor += 1
            result[site] = siteData
        return result
