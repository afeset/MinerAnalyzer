
import utils
import ux_module

# === DataProvider ====================================================================================================

class DataProvider():
    def __init__(self, topperReportsDir, uxParameters, apiLogger = None, topperLogger = None):
        from a.sys.sys_web.server.log import NullLogger
        self.topperReportsDir = topperReportsDir
        self.uxParameters = uxParameters
        self.topperLogger = topperLogger if topperLogger is not None else NullLogger()
        self.apiLogger    = apiLogger    if apiLogger    is not None else NullLogger()

# --- Over time reprots -----------------------------------------------------------------------------------------------
    def reportOverTimeBW(self, startTime, endTime, interval, intervalUnit, aggregationType):
        return self._reportOverTime(startTime, endTime, interval, ux_module.VOLUME, intervalUnit, aggregationType)

    def reportOverTimeSessions(self, startTime, endTime, interval, intervalUnit, aggregationType):
        return self._reportOverTime(startTime, endTime, interval, ux_module.SESSIONS, intervalUnit, aggregationType)

    def reportOverTimeViewTime(self, startTime, endTime, interval, intervalUnit, aggregationType):
        return self._reportOverTime(startTime, endTime, interval, ux_module.VIEW_TIME, intervalUnit, aggregationType)

    def reportOverTimeL2BW(self, startTime, endTime, interval, intervalUnit, aggregationType):
        self.apiLogger.debug("startTime=%s endTime=%s interval=%s uInterval=%s dataType=%s" % (startTime ,endTime,interval,intervalUnit,ux_module.L2_BW) )
    
        result = {}
        videoServedPoints = []
        videoPoints = []
        totalPoints = []

        if startTime == 0 and endTime == 0 and interval == 0:
            oldestTime = self.getOldestDataTime()
            debugDate = utils.formatUtcTimeAsIsoLocalTime(oldestTime)
            videoServedPoints.append({ 'date': oldestTime, 'value': 0 , 'debugDate': debugDate }) 
            videoPoints.append(      { 'date': oldestTime, 'value': 0 , 'debugDate': debugDate }) 
            totalPoints.append(      { 'date': oldestTime, 'value': 0 , 'debugDate': debugDate }) 
        else:
            if intervalUnit == 'month':
                uInterval = ux_module.MONTH
            else:
                # assume that in all other cases it is seconds
                uInterval = 's'
            
            self.apiLogger.debug("startTime=%s endTime=%s interval=%s uInterval=%s dataType=%s" % (startTime ,endTime,interval,uInterval,ux_module.L2_BW) )

            responder = ux_module.ReportsProcessor(self.topperReportsDir,self.uxParameters,self.topperLogger)
            data      = responder.l2BWOverTime(startTime ,endTime,interval,uInterval, aggregationType)
            for entry in data:
                entryDate = entry['date']
                debugDate = utils.formatUtcTimeAsIsoLocalTime(entryDate)
                videoServedPoints.append({ 'date': entryDate , 'value': entry[ux_module.VIDEO_DELIVERED], 'debugDate1': debugDate } )
                videoPoints.append(      { 'date': entryDate , 'value': entry[ux_module.VIDEO]          , 'debugDate1': debugDate } )
                totalPoints.append(      { 'date': entryDate , 'value': entry[ux_module.TOTAL]          , 'debugDate1': debugDate } )

        result['videoServed'] = { 'points': videoServedPoints }
        result['video']       = { 'points': videoPoints }
        result['total']       = { 'points': totalPoints }
        return result

    def getOldestDataTime(self):
        """Returns oldest data point available"""
        reportsInfo = ux_module.getReportsInfo(self.topperReportsDir)
        return reportsInfo['startTime']

    def _reportOverTime(self, startTime, endTime, interval, dataType, intervalUnit, aggregationType):
    
        potentialPoints = [] 
        servedPoints = [] 
        totalPoints = [] 
    
        if startTime == 0 and endTime == 0 and interval == 0:
            oldestTime = self.getOldestDataTime()
            servedPoints.append(   { 'date': oldestTime, 'value': 0 }) 
            potentialPoints.append({ 'date': oldestTime, 'value': 0 }) 
            totalPoints.append(    { 'date': oldestTime, 'value': 0 }) 
        else:
            if intervalUnit == 'month':
                uInterval = ux_module.MONTH
            else:
                # assume that in all other cases it is seconds
                uInterval = 's'
            
            self.apiLogger.debug("startTime=%s endTime=%s interval=%s uInterval=%s dataType=%s" % (startTime ,endTime,interval,uInterval,dataType) )

            responder = ux_module.ReportsProcessor(self.topperReportsDir,self.uxParameters,self.topperLogger)
            data      = responder.overTime(startTime ,endTime,interval,uInterval,dataType, aggregationType)

            for entry in data:
                entryDate = entry['date']
                debugDate = utils.formatUtcTimeAsIsoLocalTime(entryDate)
                servedPoints.append(    { 'date': entryDate , 'value': entry['delivered'] , 'debugDate1': debugDate } )
                potentialPoints.append( { 'date': entryDate , 'value': entry['cachable']  , 'debugDate1': debugDate } )
                totalPoints.append(     { 'date': entryDate , 'value': entry['total']     , 'debugDate1': debugDate } )
            
        result = {}
        result['debug']     = { 'from'  : utils.formatUtcTimeAsIsoLocalTime(startTime), 'to' : utils.formatUtcTimeAsIsoLocalTime(endTime), 'interval' : interval }
        result['potential'] = { 'points': potentialPoints }
        result['served']    = { 'points': servedPoints }
        result['total']     = { 'points': totalPoints }
    
        return result

# --- Top sites -------------------------------------------------------------------------------------------------------

    # --- reports top sites

    def reportTopSitesSortByVolume(self, startTime, endTime, count_):
        return self._reportTopSites(startTime, endTime, count_,  ux_module.VOLUME)

    def reportTopSitesSortBySessions(self, startTime, endTime, count_):
        return self._reportTopSites(startTime, endTime, count_, ux_module.SESSIONS)

    def reportTopSitesSortByViewTime(self, startTime, endTime, count_):
        return self._reportTopSites(startTime, endTime, count_, ux_module.VIEW_TIME)

    def _reportTopSites(self, startTime, endTime, count_, dataType):
      
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)
        data       = responder.top(startTime, endTime, ux_module.SITES, dataType, count_)

        entries = [] 
        dataEntries = data[ux_module.ENTRIES]
        for index, values in enumerate(dataEntries):
            entry = {}
            entry['siteId']    = values['key'] # "youtube"   
            entry['served']    = values['delivered']
            entry['potential'] = values['cachable']
            entry['total']     = values['total']
            entry['rank']      = index + 1
            #entry['debug']     = { 'key': values['key'] }
            entries.append( entry )
                   
        result = {}
        result['entries'] = entries

        grandTotalData = data[ux_module.GRAND_TOTAL]
        result['grandTotal'] = { 'total':     grandTotalData['total'],
                                 'potential': grandTotalData['cachable'],
                                 'served':    grandTotalData['delivered']
                               }
        result['debug']     = { 'from'  : utils.formatUtcTimeAsIsoLocalTime(startTime), 
                                'to'    : utils.formatUtcTimeAsIsoLocalTime(endTime),
                                'count' : count_ ,
                                'len(dataEntries)' : len(dataEntries) }
    
        return result

# --- Top titles ------------------------------------------------------------------------------------------------------

    # --- reports top titles

    def reportTopTitlesSortByVolume(self, startTime, endTime, count_, startRank):
        return self._reportTopTitles(startTime, endTime, count_, startRank,  ux_module.VOLUME)

    def reportTopTitlesSortBySessions(self, startTime, endTime, count_, startRank):
        return self._reportTopTitles(startTime, endTime, count_, startRank, ux_module.SESSIONS)

    def reportTopTitlesSortByViewTime(self, startTime, endTime, count_, startRank):
        return self._reportTopTitles(startTime, endTime, count_, startRank, ux_module.VIEW_TIME)

    def _reportTopTitles(self, startTime, endTime, count_, startRank, dataType):
       
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)   
        data       = responder.top(startTime, endTime, ux_module.TITLES, dataType, startRank + count_)
         
        firstIndex =  startRank
        dataEntries = data[ux_module.ENTRIES]
        lastIndex  = min( len(dataEntries), startRank + count_ )

        entries = [] 
        for index, values in enumerate( dataEntries[ firstIndex : lastIndex ] ):

            entry = {}
            entry['name']      = values['key']
            entry['rank']      = firstIndex + index + 1

            entry['siteId']        = values[ux_module.SITE_ID]

            entry['totalVolume']   = values[ux_module.VOLUME]
            entry['totalViewTime'] = values[ux_module.VIEW_TIME]
            entry['sessionNumber'] = values[ux_module.SESSIONS]
            entries.append( entry )
                   
        result = {}
        result['entries'] = entries
        result['debug']     = { 'from'      : utils.formatUtcTimeAsIsoLocalTime(startTime), 
                                'to'        : utils.formatUtcTimeAsIsoLocalTime(endTime), 
                                'startRank' : startRank,
                                'count'     : count_ ,
                                'len(dataEntries)' : len(dataEntries) }
    
        return result

# --- Top subscribers -------------------------------------------------------------------------------------------------

    # --- reports top subscribers

    def reportTopSubscribersSortByVolume(self, startTime, endTime, count_, startRank):
        return self._reportTopSubscribers(startTime, endTime, count_, startRank,  ux_module.VOLUME)

    def reportTopSubscribersSortBySessions(self, startTime, endTime, count_, startRank):
        return self._reportTopSubscribers(startTime, endTime, count_, startRank, ux_module.SESSIONS)

    def reportTopSubscribersSortByViewTime(self, startTime, endTime, count_, startRank):
        return self._reportTopSubscribers(startTime, endTime, count_, startRank, ux_module.VIEW_TIME)

    def _reportTopSubscribers(self, startTime, endTime, count_, startRank, dataType):
       
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)   
        data       = responder.top(startTime, endTime, ux_module.CLIENTS, dataType, startRank + count_)
         
        firstIndex =  startRank
        dataEntries = data[ux_module.ENTRIES]
        lastIndex  = min( len(dataEntries), startRank + count_ )

        entries = [] 
        for index, values in enumerate( dataEntries[ firstIndex : lastIndex ] ):

            entry = {}
            entry['subscriberId']  = values['key']
            entry['value']         = values['total']
            entry['rank']          = firstIndex + index + 1
            entries.append( entry )
                   
        result = {}
        result['entries'] = entries
        result['debug']     = { 'from'      : utils.formatUtcTimeAsIsoLocalTime(startTime), 
                                'to'        : utils.formatUtcTimeAsIsoLocalTime(endTime), 
                                'startRank' : startRank,
                                'count'     : count_ ,
                                'len(dataEntries)' : len(dataEntries) }
    
        return result

# --- Recent titles ---------------------------------------------------------------------------------------------------

    def reportRecentTitles(self, count_):
         
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)
        data       = responder.recentTitles(count_)

        entries = [] 
        for dataEntry in data:

            entry = {}
            entry['name']      = dataEntry['contentId']
            entry['served']    = dataEntry['delivered']
            entry['size']      = dataEntry['contentLength']
            entry['siteId']    = dataEntry['siteId']
            entry['time']      = dataEntry['timestamp']
            entry['subscriberId'] = dataEntry['client']
    
            entries.append( entry )
                   
        result = {}
        result['entries'] = entries
        result['_debug']     = { 'count'     : count_ ,
                                 'len(data)' : len(data) }
                          
        return result

    # --- pareto
    def _reportPareto(self, from_, to_, category, dataType):
        __pychecker__ = 'no-argsused' # from_ & to_ is not used

        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)
        
        paretoData = responder.pareto(category, dataType)

        uxEntries = paretoData['entries']
        entries = []
        for e in uxEntries:
            entries.append({'cumItems': int(e['cumItems']), 'cumValue': int(e['cumValue'])})

        result = { 'debug': {},
                   'entries': entries,
                   'grandTotal': { 'items': int(paretoData['grandTotal']['items']), 'value': int(paretoData['grandTotal']['value']) }
                 }
        return result

    def reportParetoBySubscribersVolume(self, from_, to_):
        return self._reportPareto(from_, to_, 'clients', 'volume')

    def reportParetoByTitlesVolume(self, from_, to_):
        return self._reportPareto(from_, to_, 'titles', 'volume')

# ----- Distribution ----------
    def _reportTimeDistributionFull(self, from_, to_, count_, interval, dataType):
        result = {}
        # only hourly distribution is supported
        if count_ != 24 or interval != 3600:
            return result
        potentialPoints = []
        servedPoints    = []
        totalPoints     = []
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)
        hourlyData = responder.hourlyDistribution(from_, to_, dataType)
        for data in hourlyData:
            totalPoints.append({"time": int(data["hourOfDay"])*3600, "value": int(data["total"])})
            potentialPoints.append({"time": int(data["hourOfDay"])*3600, "value": int(data["cachable"])})
            servedPoints.append({"time": int(data["hourOfDay"])*3600, "value": int(data["delivered"])})
        result["total"]     = {'points': totalPoints}
        result["potential"] = {'points': potentialPoints}
        result["served"]    = {'points': servedPoints}
        return result

    def reportTimeDistributionBW(self, from_, to_, count_, interval):
        return self._reportTimeDistributionFull(from_, to_, count_, interval, ux_module.VOLUME)
    
    def reportTimeDistributionSessions(self, from_, to_, count_, interval):
        return self._reportTimeDistributionFull(from_, to_, count_, interval, ux_module.SESSIONS)
    
    def reportTimeDistributionViewTime(self, from_, to_, count_, interval):
        return self._reportTimeDistributionFull(from_, to_, count_, interval, ux_module.VIEW_TIME)
    
    def reportTimeDistributionSubscribers(self, from_, to_, count_, interval):
        result = {}
        # only hourly distribution is supported
        if count_ != 24 or interval != 3600:
            return result
        totalPoints     = []
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)
        hourlyData = responder.hourlySubscriberDistribution(from_, to_)
        for data in hourlyData:
            totalPoints.append({"time": int(data["hourOfDay"])*3600, "value": int(data["value"])})
        result["total"] = {'points': totalPoints}
        return result

    def reportOverTimeParetoByTitles(self, startTime, endTime, interval, intervalUnit, percentilesValues):
        return self._reportOverTimePareto(startTime, endTime, interval, intervalUnit, percentilesValues, ux_module.TITLES)
    def reportOverTimeParetoBySubscribers(self, startTime, endTime, interval, intervalUnit, percentilesValues):
        return self._reportOverTimePareto(startTime, endTime, interval, intervalUnit, percentilesValues, ux_module.CLIENTS)

    def _reportOverTimePareto(self, startTime, endTime, interval, intervalUnit, percentilesValues, category):
        __pychecker__ = 'no-argsused'
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)
        requestedPercentilesValues = percentilesValues
        if 100 not in requestedPercentilesValues:
            requestedPercentilesValues.append(100)
        paretoValues = responder.paretoOverTime(startTime, endTime, interval, category, ux_module.VOLUME, requestedPercentilesValues)
        self.apiLogger.debug("start=%d end=%d percentiles=%s result:\n%s" % (startTime, endTime, requestedPercentilesValues, paretoValues))
        percentiles = []
        for p in percentilesValues:
            percentiles.append( { 'value': p , 'points': [] } )
        totalPoints = []
        for value in paretoValues:
            index = 0
            for p in percentilesValues:
                percentiles[index]['points'].append( {"date": value["date"], "value": int(value[p]) } )
                index += 1
            totalPoints.append( {"date": value["date"], "value": int(value[100]), "entities": value["items"]})
        return { "percentiles": percentiles, "total": { "points": totalPoints }}

    def reportOverTimeBitRate(self, subType, from_, to_, interval, intervalUnit, \
                                    siteList, dataSeries):
        uxDataSubType = ux_module.BITRATE__TRANSACTIONS if subType=="perTransaction" else ux_module.BITRATE__SESSIONS
        uxGranularityUnit = ux_module.MONTH if intervalUnit == 'month' else ux_module.SECOND
        responder  = ux_module.ReportsProcessor(self.topperReportsDir, self.uxParameters, self.topperLogger)
        bitRateUnits = responder.bitrateOverTime(uxDataSubType, siteList, from_, to_, interval, uxGranularityUnit)
        result = {}

        def point(value, unit):
            debugDate = utils.formatUtcTimeAsIsoLocalTime(unit.unitTime)
            return {'value': value, 'date': unit.unitTime, 'debugDate': debugDate }

        dataSeriesList = set(dataSeries.split(",")) if dataSeries else None
        for site in siteList.split(","):
            siteData = {}
            analyzedAverageSeries = []
            servedAverageSeries = []
            analyzedMaxSeries = []
            servedMaxSeries = []
            analyzedSampleSeries = []
            servedSampleSeries = []
            totalSampleSeries = []
            for unit in bitRateUnits:
                siteUnit = unit.siteDict.get(site, None)
                if not siteUnit:
                    continue
                bitRateLine = siteUnit.interfaceDict["line"]
                bitRateDelivery = siteUnit.interfaceDict["delivery"]
                servedAverage = 0
                if not dataSeriesList or 'servedAverage' in dataSeriesList:
                    servedAverage = 0 if bitRateDelivery.totalTime==0 else max(1,(bitRateDelivery.totalVolume*8*1000/bitRateDelivery.totalTime))
                    servedAverageSeries.append( point(servedAverage, unit) )
                analyzedAverage = 0
                if not dataSeriesList or 'analyzedAverage' in dataSeriesList:
                    analyzedAverage = 0 if bitRateLine.totalTime==0 else max(1,(bitRateLine.totalVolume*8*1000/bitRateLine.totalTime))
                    analyzedAverageSeries.append( point(analyzedAverage, unit) )
            
                linePeakBitrate = 0
                deliveryPeakBitrate = 0
                lineAvgUnits = 0
                deliveryAvgUnits = 0
                totalAvgUnits = 0

                numUnits = max(1, unit.numUnits)

                if bitRateDelivery.totalTime != 0:
                    deliveryPeakBitrate = max(1,bitRateDelivery.peakBitRate)
                    deliveryAvgUnits = max(1,bitRateDelivery.numCurrent/numUnits)

                if bitRateLine.totalTime != 0:
                    linePeakBitrate = max(1,bitRateLine.peakBitRate)
                    lineAvgUnits = max(1,bitRateLine.numCurrent/numUnits)

                if bitRateLine.totalTime != 0 or bitRateDelivery.totalTime != 0:
                    value = bitRateDelivery.numCurrent + bitRateLine.numCurrent
                    totalAvgUnits = max(1,value/numUnits)

                if not dataSeriesList or 'servedMax' in dataSeriesList:
                    servedMaxSeries.append(point(deliveryPeakBitrate, unit))
                if not dataSeriesList or 'analyzedMax' in dataSeriesList:
                    analyzedMaxSeries.append(point(linePeakBitrate, unit))
                
                if not dataSeriesList or 'servedAverageConcurrentSamples' in dataSeriesList:
                    servedSampleSeries.append(point(deliveryAvgUnits, unit))
                if not dataSeriesList or 'analyzedAverageConcurrentSamples' in dataSeriesList:
                    analyzedSampleSeries.append(point(lineAvgUnits, unit))

                if not dataSeriesList or 'totalAverageConcurrentSamples' in dataSeriesList:
                    
                    totalSampleSeries.append(point(totalAvgUnits, unit))

            if not dataSeriesList or 'servedAverage' in dataSeriesList:
                siteData['servedAverage'] = servedAverageSeries
            if not dataSeriesList or 'analyzedAverage' in dataSeriesList:
                siteData['analyzedAverage'] = analyzedAverageSeries

            if not dataSeriesList or 'servedMax' in dataSeriesList:
                siteData['servedMax'] = servedMaxSeries
            if not dataSeriesList or 'analyzedMax' in dataSeriesList:
                siteData['analyzedMax'] = analyzedMaxSeries

            if not dataSeriesList or 'servedAverageConcurrentSamples' in dataSeriesList:
                siteData['servedAverageConcurrentSamples'] = servedSampleSeries
            if not dataSeriesList or 'analyzedAverageConcurrentSamples' in dataSeriesList:
                siteData['analyzedAverageConcurrentSamples'] = analyzedSampleSeries

            if not dataSeriesList or 'totalAverageConcurrentSamples' in dataSeriesList:
                siteData['totalAverageConcurrentSamples'] = totalSampleSeries
            
            result[site] = siteData

        return result

