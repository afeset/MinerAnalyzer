import a.sys.sys_web.mng.django_app as api
import time
import loggers
import datetime
import time
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    #jpype module uses deprecated sets module
    import jpype
import os
import socket

DAY = 24*3600
GB = 1024*1024*1024
Gbps = 1e9
MB = 1024*1024

# For week, month and 3 months intervals we take one day spare
RANGE_PARAMETERS = [
    { 'limit': 2*3600,  'col-interval': 300, 'point-interval': 60, 'tick-interval': 300 },
    { 'limit': 12*3600, 'col-interval': 30*60, 'point-interval': 300, 'tick-interval': 30*60 },
    { 'limit': 24*3600, 'col-interval': 3600, 'point-interval': 600, 'tick-interval': 3600 },
    { 'limit': 48*3600, 'col-interval': 2*3600, 'point-interval': 20*60, 'tick-interval': 2*3600 },
    { 'limit': 5*DAY,   'col-interval': 12*3600, 'point-interval': 30*60, 'tick-interval': 12*3600 },
    { 'limit': 8*DAY,   'col-interval': 12*3600, 'point-interval': 60*60, 'tick-interval': 12*3600 },
    { 'limit': 32*DAY,  'col-interval': DAY, 'point-interval': 4*3600, 'tick-interval': DAY },
    { 'limit': 93*DAY,  'col-interval': 7*DAY, 'point-interval': DAY, 'tick-interval': 7*DAY },
    ]

def getRangeParameter(from_, to_, paramName):
    delta = to_ - from_
    for e in RANGE_PARAMETERS:
        if delta <= e['limit']:
            return e[paramName]
    return RANGE_PARAMETERS[-1][paramName]

def getPointInterval(from_, to_):
    return getRangeParameter(from_, to_, 'point-interval')

def getColInterval(from_, to_):
    return getRangeParameter(from_, to_, 'col-interval')

def getIntervalUnit(from_, to_, intervalType="point-interval"):
    val= getRangeParameter(from_, to_, 'tick-interval') / getRangeParameter(from_, to_, intervalType)
    loggers.accessLogger.debug("from_=%d, to_=%d delta=%d intervalUnit=%d" % (from_, to_, to_-from_, val))
    return val

def time2excel(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    dt1900 = datetime.datetime(1900,1,1)
    delta = dt - dt1900

    # Excel handles time in number of days since 1, January 1900
    # Where 1, Jan 1900 itself is 1
    # Additional +1 is fix to bug in Excel that treats 1900 as a leap year
    value = delta.days + 2 + delta.seconds/24./3600.
    return value

def colName(col):
    return chr(col+ord('A'))
def cellName(col, row):
    return "%s%d" % (colName(col), row+1)

def navigate(root, path):
    pathElements = path.split("/")
    component = root
    for e in pathElements:
        if isinstance(component, list):
            key = int(e)
        else:
            key = e
        component = component[key]
    return component

def navigateOrDefault(root, path, default):
    pathElements = path.split("/")
    component = root
    try:
        for e in pathElements:
            if isinstance(component, list):
                key = int(e)
            else:
                key = e
            component = component[key]
    except:
        return default
    return component

def floorVal(val, interval):
    """
    Gets closest round value in the multiplications of intervals smaller than val
    Example:
        floorTime(3700, 3600) = 3600
    """
    return val/interval*interval

def ceilVal(val, interval):
    """
    Gets closest round value in the multiplications of intervals bigger than val
    Example:
        ceilTime(3700, 3600) = 7200
    """
    return (val+interval-1)/interval*interval

def getTimezone(val):
    if time.daylight and time.localtime(val).tm_isdst:
        return time.altzone
    else:
        return time.timezone

def getCurrentTimezone():
    return getTimezone(time.time())

def floorDay(val):
    """Returns closest day start in local timezone before val"""
    timezone = getTimezone(val)
    return (val - timezone) / DAY * DAY + timezone

def ceilDay(val):
    """Returns closest day end in local timezone before val"""
    timezone = getTimezone(val)
    return (val - timezone +DAY-1) / DAY * DAY + timezone

def floorTime(t, interval):
    if interval >= DAY:
        return floorDay(t)
    elif interval >= 3600:
        return floorVal(t, 3600)
    else:
        return floorVal(t, interval)

def ceilTime(t, interval):
    if interval >= DAY:
        return ceilDay(t)
    elif interval >= 3600:
        return ceilVal(t, 3600)
    else:
        return ceilVal(t, interval)

class ExcelRange:
    def __init__(self):
        self.startRow = 0
        self.endRow = 1
        self.startCol = 0
        self.endCol = 1
        self.sheetName = None
    def setRange(self, rangeStr):
        if '!' in rangeStr:
            (sheetName,rangeStr) = rangeStr.split('!', 2)
            sheetName.strip("'")
            self.sheetName = sheetName

        (startCell, lastCell) = rangeStr.split(':')
        self.startRow = int(startCell[1:])-1
        self.endRow = int(lastCell[1:])
        self.startCol = ord(startCell[0].lower()) - ord('a')
        self.endCol = ord(lastCell[0].lower()) - ord('a') + 1
    def setRegion(self, startRow, startCol, endRow, endCol):
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol

    def setColRegion(self, col, startRow, endRow):
        self.startRow = startRow
        self.startCol = col
        self.endRow = endRow
        self.endCol = col+1
    def __str__(self):
        rangeStr = "$%s$%d:$%s$%d" %(colName(self.startCol), self.startRow+1, colName(self.endCol), self.endRow)
        return rangeStr if not self.sheetName else "'%s'!%s" % (self.sheetName, rangeStr)


class Requestor:
    def __init__(self):
        self.cache = {}

    _instance = None

    @staticmethod
    def instance():
        if not Requestor._instance:
            Requestor._instance = Requestor()
        return Requestor._instance

    def getResponse(self, request):
        response = self.cache.get(str(request), None)
        if response is None:
            response = api.apiSystemProcessSection(0, request)
            self.cache[str(request)] = response
        return response

    def clearCache(self):
        self.cache.clear()

class Writer:
    def __init__(self, sheetName, linkRange):
        """
        Initialize writer sheet and cell range
        linkRange - should be of style 'A10:C20'
        """
        parsedRange = ExcelRange()
        parsedRange.setRange(linkRange)

        self.sheetName = sheetName
        self.startRow = parsedRange.startRow
        self.endRow = parsedRange.endRow
        self.startCol = parsedRange.startCol
        self.endCol = parsedRange.endCol
        self.shouldUpdateDayFormat = True

    def createFullRange(self, startCol, startRow, endCol, endRow):
        """
        Gets Excel range
        """
        rangeStr = "$%s$%d:$%s$%d" %(colName(startCol), startRow+1, colName(endCol), endRow)
        return "'%s'!%s" % (self.sheetName, rangeStr)        
    
    def getFullRange(self):
        """
        Gets Excel range with for current link range
        """
        return self.createFullRange(self.startCol, self.startRow, self.endCol-1, self.endRow)

    def copyCellFormat(self, workbook, fromCol, fromRow, toCol, toRow):
        rangeStyle = workbook.getRangeStyle(fromRow, fromCol, fromRow, fromCol)
        fontColor = rangeStyle.getFontColor()
        isLocked = rangeStyle.isLocked()
        loggers.accessLogger.debug("rangeStyle=%06x %06x isLocked=%d" % (rangeStyle.getFontColor(), rangeStyle.getPatternBG(), rangeStyle.isLocked()) )
        rangeStyle.useAllFormat()
        # do this explicitly since useAllFormat doesn't apply font color
        rangeStyle.setFontColor(fontColor)
        rangeStyle.setLocked(True)
        workbook.setRangeStyle(rangeStyle, toRow, toCol, toRow, toCol)

        loggers.accessLogger.debug("copied rangeStyle=%06x %06x" % (rangeStyle.getFontColor(), rangeStyle.getPatternBG()) )

    def copyRowFormat(self, workbook, fromRow, toRow):
        if fromRow == toRow:
            return
        for col in range(self.startCol, self.endCol):
            self.copyCellFormat(workbook, col, fromRow, col, toRow)

    def getRequest(self, paramsDecoder):
        """returns request parameters to api"""
        raise NotImplementedError

    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        raise NotImplementedError

    def extendRows(self, workbook, newRowNumber):
        """
        This function extends number of rows in the range to the newRowNumber
        New last row is formatted according to the old last row
        Intermidiate rows are formatted according to the (old last row -1)
        """
        if newRowNumber == self.endRow - self.startRow:
            return
        WorkBook = jpype.JClass('com.smartxls.WorkBook')
        # copy last row format
        prevLastRow = self.endRow - 1
        self.endRow = self.startRow + newRowNumber
        newLastRow = self.endRow - 1
        if self.endRow > self.startRow+2:
            # copy endRow format only if there is more than  2 rows in the range
            self.copyRowFormat(workbook, prevLastRow, newLastRow)
        if newLastRow < prevLastRow:
            # delete extra cells
            workbook.deleteRange(newLastRow+1, self.startCol, prevLastRow, self.endCol-1, WorkBook.ShiftVertical)
            return
        # Copy intermidiate rows
        for i in range(prevLastRow,newLastRow):
            self.copyRowFormat(workbook, prevLastRow-1, i)

    def updateChartIntervalUnit(self, chart, intervalUnit):
        if intervalUnit <= 1:
            return
        chart.setAxisScaleType(0, 0, 2)
        chart.setScaleMajorUnitAuto(0, 0, False)
        try:
            chart.setTimeScaleMajorUnit(0, 0, 1, intervalUnit)
            chart.setTimeScaleMinorUnit(0, 0, 1, intervalUnit)
        except:
            loggers.mainLogger.warning("Failed to set intervalUnit to %d" % intervalUnit)

    def setDayFormat(self, workbook, col, startRow, endRow):
        """
        The function iterates over cells and updates their format so that each new day will be presented as 'mmm dd', e.g.:
        18:00 -> 18:00
        00:00 -> May 01
        06:00 -> 06:00
        12:00 -> 12:00
        02:00 -> May 02
        """
        if not self.shouldUpdateDayFormat:
            return
        lastDay = workbook.getNumber(startRow, col)
        dayFormat = "[$-409]mmm dd"
        for row in range(startRow+1, endRow):
            currentDay = workbook.getNumber(row, col)
            if int(currentDay) != int(lastDay):
                rangeStyle = workbook.getRangeStyle(row, col, row, col)
                rangeStyle.setCustomFormat(dayFormat)
                workbook.setRangeStyle(rangeStyle, row, col, row, col)
                lastDay = currentDay

class OvertimeWriter(Writer):
    def __init__(self, sheetName, linkRange, dataType, rangePrameter, scale):
        Writer.__init__(self, sheetName, linkRange)
        self.dataType = dataType
        self.scale = scale
        self.rangeParameter = rangePrameter

    def getRequest(self, paramsDecoder):
        self.intervalUnit = getIntervalUnit(paramsDecoder.getFromTime(), paramsDecoder.getToTime(), intervalType=self.rangeParameter)
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        interval = getRangeParameter(paramsDecoder.getFromTime(), paramsDecoder.getToTime(), self.rangeParameter)
        # Align from and to according to the "strict API"
        from_ = floorTime(from_, interval)
        to_ = ceilTime(to_, interval)

        return {'section':    'report',
                'reportType': 'overTime',
                'dataType':   self.dataType,
                'from':       str(from_),
                'to':         str(to_),
                'interval':   str(interval),
               }

    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        try:
            overtimeReports = response['reports']['overTime']
            (reportType, reportData) = overtimeReports.items()[0]
            potentialPoints = reportData["potential"]["points"]
            totalPoints = reportData["total"]["points"]
            servedPoints = reportData["served"]["points"]
        except:
            loggers.mainLogger.error("response=%s" % response)
            raise
        numPoints = len(totalPoints)
        for i in range(numPoints):
            workbook.setNumber( i+self.startRow+1, self.startCol+0, time2excel(totalPoints[i]["date"]))
            workbook.setNumber(i+self.startRow+1, self.startCol+1, float(totalPoints[i]["value"])/self.scale)
            workbook.setNumber(i+self.startRow+1, self.startCol+2, float(potentialPoints[i]["value"])/self.scale)
            workbook.setNumber(i+self.startRow+1, self.startCol+3, float(servedPoints[i]["value"])/self.scale)
            workbook.setFormula(i+self.startRow+1, self.startCol+4, "%s/%s"% (cellName(self.startCol+3,i+self.startRow+1), cellName(self.startCol+1, i+self.startRow+1)))

        self.extendRows(workbook, numPoints+1)
        self.setDayFormat(workbook, self.startCol, self.startRow+1, self.endRow)
        chart = workbook.getChart(0)
        # last col is percentage - do not show it on graph
        self.endCol -= 1
        chart.setLinkRange(self.getFullRange(), False)
        self.updateChartIntervalUnit(chart, self.intervalUnit)

class CurrentTrafficWriter(Writer):
    def __init__(self, sheetName, linkRange):
        Writer.__init__(self, sheetName, linkRange)

    def getRequest(self, paramsDecoder):
        # get current time alignet to minutes
        currentTime = floorTime(api.getCurrentTime(), 60)
        return {'section':    'report',
                'reportType': 'overTime',
                'dataType':   'BW',
                'from':       str(currentTime - 600),
                'to':         str(currentTime),
                'interval':   '60',
               }

    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        try:
            overtimeReports = response['reports']['overTime']
            (reportType, reportData) = overtimeReports.items()[0]
            potentialPoints = reportData["potential"]["points"]
            totalPoints = reportData["total"]["points"]
            servedPoints = reportData["served"]["points"]
        except:
            loggers.mainLogger.error("response=%s" % response)
            raise
        numPoints = len(totalPoints)
        # Find latest available point
        if numPoints > 0:
            total = float(totalPoints[-1]["value"])/1e9
            if total == 0:
                total = 1e-9
            served = float(servedPoints[-1]["value"])/1e9
            potential = float(potentialPoints[-1]["value"])/1e9

            if self.endRow - self.startRow == 1:
                # range is horizontal
                workbook.setNumber(self.startRow, self.startCol+1, total)
                workbook.setNumber(self.startRow, self.startCol+3, served)
                if self.endCol > self.startCol+5:
                    workbook.setNumber(self.startRow, self.startCol+5, potential)
            else:
                # assumed range is vertical
                workbook.setNumber(self.startRow+0, self.startCol+1, total)
                workbook.setNumber(self.startRow+1, self.startCol+1, served)
                workbook.setNumber(self.startRow+2, self.startCol+1, potential)

class BandwidthWriter(OvertimeWriter):
    def __init__(self, sheetName, linkRange):
        OvertimeWriter.__init__(self, sheetName, linkRange, "BW", "point-interval", 1e9)

class SessionsWriter(OvertimeWriter):
    def __init__(self, sheetName, linkRange):
        OvertimeWriter.__init__(self, sheetName, linkRange, "sessions", "col-interval", 1000)

class ViewTimeWriter(OvertimeWriter):
    def __init__(self, sheetName, linkRange):
        OvertimeWriter.__init__(self, sheetName, linkRange, "viewTime", "col-interval", 24*3600)

class TrafficWriter(OvertimeWriter):
    def __init__(self, sheetName, linkRange):
        Writer.__init__(self, sheetName, linkRange)
    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        interval = getPointInterval(from_, to_)
        # Align from and to according to the "strict API"
        from_ = floorTime(from_, interval)
        to_ = ceilTime(to_, interval)
        self.intervalUnit = getIntervalUnit(from_, to_)
        return {'section':    'report',
                'reportType': 'overTime',
                'dataType':   'L2BW',
                'from':       str(from_),
                'to':         str(to_),
                'interval':   str(interval),
               }

    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        overtimeReports = response['reports']['overTime']
        (reportType, reportData) = overtimeReports.items()[0]
        totalPoints = reportData["total"]["points"]
        videoPoints = reportData["video"]["points"]
        servedPoints = reportData["videoServed"]["points"]
        numPoints = len(totalPoints)
        for i in range(numPoints):
            workbook.setNumber(i+self.startRow+1, self.startCol+0, time2excel(totalPoints[i]["date"]))
            workbook.setNumber(i+self.startRow+1, self.startCol+1, float(totalPoints[i]["value"])/1e9)
            workbook.setNumber(i+self.startRow+1, self.startCol+2, float(videoPoints[i]["value"])/1e9)
            workbook.setNumber(i+self.startRow+1, self.startCol+3, float(servedPoints[i]["value"])/1e9)
            if self.startCol+4 < self.endCol:
                # fifth column may be a cache ratio
                workbook.setFormula(i+self.startRow+1, self.startCol+4, "%s/%s"% (cellName(self.startCol+3,i+self.startRow+1), cellName(self.startCol+1, i+self.startRow+1)))

        self.extendRows(workbook, numPoints+1)
        self.setDayFormat(workbook, self.startCol, self.startRow+1, self.endRow)
        chart = workbook.getChart(0)
        # Exclude cache ratio column if exists
        self.endCol = self.startCol + 4
        chart.setLinkRange(self.getFullRange(), False)
        self.updateChartIntervalUnit(chart, self.intervalUnit)

class ParetoWriter(Writer):
    def __init__(self, sheetName, linkRange, groupBy):
        Writer.__init__(self, sheetName, linkRange)
        self.groupBy = groupBy
    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        from_ = floorTime(from_, 3600)
        to_ = ceilTime(to_, 3600)
        return {'section':    'report',
                'reportType': 'pareto',
                'dataType':   'volume',
                'groupBy':    self.groupBy,
                'from':       str(from_),
                'to':         str(to_),
               }
    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        loggers.accessLogger.debug("response=%s", str(response))
        report = response['reports']['pareto'][self.groupBy]['volume']
        totalItems = report['grandTotal']['items']
        totalValue = report['grandTotal']['value']/1e9
        rowIter = self.startRow + 1
        for entry in report['entries']:
            workbook.setNumber(rowIter, self.startCol+2, entry['cumValue']/1e9)
            workbook.setNumber(rowIter, self.startCol+3, float(entry['cumItems']))
            workbook.setFormula(rowIter, self.startCol+0, "%s/%f" % (cellName(self.startCol+3, rowIter), totalItems))
            workbook.setFormula(rowIter, self.startCol+1, "%s/%f" % (cellName(self.startCol+2, rowIter), totalValue))
            rowIter += 1

        self.extendRows(workbook, rowIter - self.startRow)

        # Only first 2 columns are drawn on the chart
        self.endCol = self.startCol + 2
        chart = workbook.getChart(0)

        loggers.accessLogger.debug("..xaxisFormula = %s" % chart.getSeriesXValueFormula(0))
        loggers.accessLogger.debug("..yaxisFormula = %s" % chart.getSeriesYValueFormula(0))
        loggers.accessLogger.debug("..new Range: \"%s\"" % self.createFullRange(self.startCol, self.startRow+1, self.startCol, self.endRow))
        loggers.accessLogger.debug("..new Range: \"%s\"" % self.createFullRange(self.startCol+1, self.startRow+1, self.startCol+1, self.endRow))
        chart.setSeriesXValueFormula(0, self.createFullRange(self.startCol, self.startRow+1, self.startCol, self.endRow))
        chart.setSeriesYValueFormula(0, self.createFullRange(self.startCol + 1, self.startRow+1, self.startCol + 1, self.endRow))

class SubscribersParetoWriter(ParetoWriter):
    def __init__(self, sheetName, linkRange):
        ParetoWriter.__init__(self, sheetName, linkRange, "subscribers")

class TitlesParetoWriter(ParetoWriter):
    def __init__(self, sheetName, linkRange):
        ParetoWriter.__init__(self, sheetName, linkRange, "titles")

class SystemStatusWriter(Writer):
    def __init__(self, sheetName, linkRange):
        Writer.__init__(self, sheetName, linkRange)
    def getRequest(self, paramsDecoder):
        return {'section':    'system',
                'type':       'shortStatus',
               }
    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        status = response["system"]["status"]
        # cache
        workbook.setNumber(self.startRow+1, self.startCol+1, float(navigateOrDefault(status,"cache/stored", 0)))
        workbook.setNumber(self.startRow+2, self.startCol+1, float(navigateOrDefault(status,"cache/acquired", 0)))
        workbook.setNumber(self.startRow+3, self.startCol+1, float(navigateOrDefault(status,"cache/delivered", 0)))
        # software information
        workbook.setText(self.startRow+1, self.startCol+3, status["software"]["version"])
        workbook.setText(self.startRow+2, self.startCol+3, status["software"]["license"])
        workbook.setText(self.startRow+3, self.startCol+3, "N/A") # site pack

class ReportTimeWriter(Writer):
    def __init__(self, sheetName, linkRange):
        Writer.__init__(self, sheetName, linkRange)
    def getRequest(self, paramsDecoder):
        self.from_ = paramsDecoder.getFromTime()
        self.to_ = paramsDecoder.getToTime()
        return None
    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        workbook.setNumber(self.startRow, self.startCol, time2excel(api.getCurrentTime()))
        workbook.setNumber(self.startRow+1, self.startCol+0, time2excel(self.from_))
        workbook.setNumber(self.startRow+1, self.startCol+1, time2excel(self.to_))

class HostnameWriter(Writer):
    def __init__(self, sheetName, linkRange):
        Writer.__init__(self, sheetName, linkRange)
    def getRequest(self, paramsDecoder):
        return None
    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        workbook.setText(self.startRow, self.startCol, socket.gethostname())

class TopSitesWriter(Writer):
    def __init__(self, sheetName, linkRange, dataType, scale):
        Writer.__init__(self, sheetName, linkRange)
        self.dataType = dataType
        self.scale = scale
    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        try:
            countNum = paramsDecoder.getCount()
        except:
            countNum = 10
        return {'section':    'report',
                'reportType': 'top',
                'dataType':   self.dataType,
                'groupBy':    'sites',
                'from':       str(from_),
                'to':         str(to_),
                'count':      str(countNum),
               }
    def write(self, workbook, response):
        report = response['reports']['top']['sites'][self.dataType]
        grandTotal = report["grandTotal"]
        row = self.startRow+1
        
        for e in report['entries']:
            workbook.setNumber(row, self.startCol+0, float(e['rank']))
            workbook.setText(row, self.startCol+1, e['siteId'])
            workbook.setNumber(row, self.startCol+2, float(e['total']/self.scale))
            workbook.setNumber(row, self.startCol+3, float(e['potential']/self.scale))
            workbook.setNumber(row, self.startCol+4, float(e['served']/self.scale))
            row += 1

        workbook.setText(row, self.startCol+1, "Other")
        workbook.setFormula(row, self.startCol+2, "%s-SUM(%s:%s)" % (cellName(self.startCol+2,row+1), cellName(self.startCol+2,self.startRow+1), cellName(self.startCol+2, row-1) ) )
        workbook.setFormula(row, self.startCol+3, "%s-SUM(%s:%s)" % (cellName(self.startCol+3,row+1), cellName(self.startCol+3,self.startRow+1), cellName(self.startCol+3, row-1) ))
        workbook.setFormula(row, self.startCol+4, "%s-SUM(%s:%s)" % (cellName(self.startCol+4,row+1), cellName(self.startCol+4,self.startRow+1), cellName(self.startCol+4, row-1) ))

        row += 1
        workbook.setText(row, self.startCol+1, "Total")
        workbook.setNumber(row, self.startCol+2, float(grandTotal['total']/self.scale))
        workbook.setNumber(row, self.startCol+3, float(grandTotal['potential']/self.scale))
        workbook.setNumber(row, self.startCol+4, float(grandTotal['served']/self.scale))
        self.extendRows(workbook, row+1-self.startRow)
        chart = workbook.getChart(0)
        self.endRow = row+1

        linkRange = ExcelRange()
        linkRange.sheetName = self.sheetName
        linkRange.setRegion(self.startRow, self.startCol+1, self.endRow-1, self.startCol+3)

        chart.setLinkRange(str(linkRange), False)
        ChartFormat = jpype.JClass('com.smartxls.ChartFormat')
        chartFormat = chart.getPlotFormat()
        if report['entries'] < 20:
            chartFormat.setDataLabelTypes(ChartFormat.DataLabelPercentageMask | ChartFormat.DataLabelXValueMask )
        else:
            chartFormat.setDataLabelTypes( ChartFormat.DataLabelPercentageMask )
        chart.setPlotFormat(chartFormat)


class TopSubscribersWriter(Writer):
    def __init__(self, sheetName, linkRange, dataType, factor):
        Writer.__init__(self, sheetName, linkRange)
        self.dataType = dataType
        self.factor = factor
    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        try:
            countNum = paramsDecoder.getCount()
        except:
            countNum = 10
        return {'section':    'report',
                'reportType': 'top',
                'dataType':   self.dataType,
                'groupBy':    'subscribers',
                'from':       str(from_),
                'to':         str(to_),
                'count':      str(countNum),
               }
    def write(self, workbook, response):
        report = response['reports']['top']['subscribers'][self.dataType]
        row = self.startRow+1

        for e in report['entries']:
            workbook.setNumber(row, self.startCol+0, float(e['rank']))
            workbook.setText(row, self.startCol+1, e['subscriberId'])
            workbook.setNumber(row, self.startCol+2, float(e['value']/self.factor))
            row += 1
        self.extendRows(workbook, row-self.startRow)

class TopTitlesWriter(Writer):
    def __init__(self, sheetName, linkRange, dataType, firstCol, firstColScale, secondCol, secondColScale):
        Writer.__init__(self, sheetName, linkRange)
        self.dataType = dataType
        self.firstCol = firstCol
        self.firstColScale = firstColScale
        self.secondCol = secondCol
        self.secondColScale = secondColScale
    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        try:
            countNum = paramsDecoder.getCount()
        except:
            countNum = 10
        return {'section':    'report',
                'reportType': 'top',
                'dataType':   self.dataType,
                'groupBy':    'titles',
                'from':       str(from_),
                'to':         str(to_),
                'count':      str(countNum),
               }
    def write(self, workbook, response):
        report = response['reports']['top']['titles'][self.dataType]
        row = self.startRow+1

        for e in report['entries']:
            workbook.setNumber(row, self.startCol+0, float(e['rank']))
            workbook.setText(row,   self.startCol+1, e['name'])
            workbook.setText(row,   self.startCol+2, e['siteId'])
            sessionNum = e['sessionNumber']
            if sessionNum < 1:
                loggers.accessLogger.warning("Session number for title '%s' was 0 etting to 1" % e['name'])
                sessionNum = 1
            workbook.setNumber(row, self.startCol+3, float(e[self.firstCol])/self.firstColScale)
            workbook.setNumber(row, self.startCol+4, float(e[self.secondCol])/self.secondColScale)
            workbook.setNumber(row, self.startCol+5, float(e['totalViewTime'])/sessionNum/DAY)
            workbook.setNumber(row, self.startCol+6, float(e['totalVolume'])/sessionNum/MB)
            row += 1
        self.extendRows(workbook, row-self.startRow)

class DailyDistributionWriter(Writer):
    def __init__(self, sheetName, linkRange, dataType, scale):
        Writer.__init__(self, sheetName, linkRange)
        self.dataType = dataType
        self.scale = scale
        self.timezone = getCurrentTimezone()
    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        return {'section':    'report',
                'reportType': 'distribution',
                'distributionType': 'time',
                'dataType':   self.dataType,
                'count':      '24',
                'interval':   '3600',
                'from':       str(from_),
                'to':         str(to_),
               }
    def getLocalHour(self, time):
        return ((time - self.timezone)/3600)%24
    def write(self, workbook, response):
        try:
            report = response['reports']['distribution']['time'][self.dataType]
            totalPoints = report['total']['points']
        except:
            loggers.mainLogger.warning("report = %s" % report)
            return

        potentialPoints = report['potential']['points'] if 'potential' in report else None
        servedPoints = report['served']['points'] if 'served' in report else None
        row = self.startRow+1
        for p in totalPoints:
            workbook.setNumber(self.startRow+1+self.getLocalHour(p['time']), self.startCol+1, float(p['value']/self.scale))
        if potentialPoints:
            for p in potentialPoints:
                workbook.setNumber(self.startRow+1+self.getLocalHour(p['time']), self.startCol+2, float(p['value']/self.scale))
        if servedPoints:
            for p in servedPoints:
                workbook.setNumber(self.startRow+1+self.getLocalHour(p['time']), self.startCol+3, float(p['value']/self.scale))

class ParetoOverTimeWriter(Writer):
    def __init__(self, sheetName, linkRange, groupBy, percentiles):
        Writer.__init__(self, sheetName, linkRange)
        self.groupBy = groupBy
        self.percentiles = percentiles

    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        interval = 3600
        from_ = floorTime(from_, interval)
        to_ = ceilTime(to_, interval)
        self.intervalUnit = getRangeParameter(from_, to_, 'tick-interval')/interval
        loggers.accessLogger.debug("intervalUnit=%d to-from=%d" % (self.intervalUnit, to_-from_))
        return {'section':    'report',
                'reportType': 'overTime',
                'dataType':   'pareto',
                'paretoDataType': 'volume',
                'groupBy':    self.groupBy,
                'percentiles': ",".join(str(p) for p in self.percentiles),
                'from':       str(from_),
                'to':         str(to_),
                'interval':   str(interval),
               }

    def write(self, workbook, response):
        """Writes response to workbook. Relevant sheet is selected"""
        loggers.accessLogger.info("Write workbook")
        try:
            report = response['reports']['overTime']['pareto'][self.groupBy]
        except:
            loggers.mainLogger.error("response=%s" % response)
            raise
        numPoints = len(self.percentiles)
        percentilePoints = {}
        for pArr in report['percentiles']:
            percentilePoints[pArr['value']] = pArr['points']
        # print times
        firstP = self.percentiles[0]
        numPoints = len(percentilePoints[firstP])
        for i in range(numPoints):
            workbook.setNumber(i+self.startRow+1, self.startCol, time2excel(percentilePoints[firstP][i]["date"]))

        totalPoints = report['total']['points']
        for i in range(numPoints):
            #totalEntities = response['total'][i]["entities"]
            totalValue = totalPoints[i]["value"]
            col = self.startCol+1
            for p in self.percentiles:
                workbook.setNumber(i+self.startRow+1, col, float(percentilePoints[p][i]["value"])/totalValue)
                col += 1
        self.extendRows(workbook, numPoints+1)
        self.setDayFormat(workbook, self.startCol, self.startRow+1, self.endRow)
        chart = workbook.getChart(0)
        chart.setLinkRange(self.getFullRange(), False)
        self.updateChartIntervalUnit(chart, self.intervalUnit)


class PeakDataRequestor:
    def __init__(self):
        pass

    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        # align from_ and to_ to round days:
        from_ = floorDay(from_)
        to_ = ceilDay(to_)
        self.interval = getRangeParameter(from_, to_, "col-interval")
        if self.interval < DAY:
            self.interval = DAY
            self.intervalUnit = 1
        else:
            self.intervalUnit = getIntervalUnit(from_, to_, intervalType="col-interval")

        return {'section':    'report',
                'reportType': 'overTime',
                'dataType':   self.dataType,
                'from':       str(from_),
                'to':         str(to_),
                'interval':   str(self.interval),
                'aggregationType': 'max',
               }

class PeakDataWriter(OvertimeWriter, PeakDataRequestor):
    def __init__(self, sheetName, linkRange, dataType, scale):
        OvertimeWriter.__init__(self, sheetName, linkRange, dataType, "col-interval", scale)
        PeakDataRequestor.__init__(self)
        self.shouldUpdateDayFormat = False
    def getRequest(self, paramsDecoder):
        return PeakDataRequestor.getRequest(self, paramsDecoder)

class PeakTrafficDataWriter(TrafficWriter, PeakDataRequestor):
    def __init__(self, sheetName, linkRange):
        TrafficWriter.__init__(self, sheetName, linkRange)
        PeakDataRequestor.__init__(self)
        self.shouldUpdateDayFormat = False
        self.dataType = "L2BW"
    def getRequest(self, paramsDecoder):
        return PeakDataRequestor.getRequest(self, paramsDecoder)

class PeakTopSitesWriter(TopSitesWriter):
    def __init__(self, sheetName, linkRange, dataType, scale):
        TopSitesWriter.__init__(self, sheetName, linkRange, dataType, scale)
    def getRequest(self, paramsDecoder):
        from_ = paramsDecoder.getFromTime()
        to_ = paramsDecoder.getToTime()
        if (from_ - to_) != 3600:
            # send the peak request to obtain maximum data point
            request =  {'section':    'report',
                    'reportType': 'overTime',
                    'dataType':   'L2BW',
                    'from':       str(from_),
                    'to':         str(to_),
                    'interval':   str(to_ - from_),
                    'aggregationType': 'max',
                   }
            response = Requestor.instance().getResponse(request)
            try:
                maxDate = navigate(response,"reports/overTime/L2BW/total/points/0/date")
                from_ = floorTime(maxDate, 3600)
                to_ = ceilTime(maxDate+1, 3600)
            except:
                loggers.mainLogger.warning("Failed to extract max date, response=%s" % str(response))
        paramsDecoder.setParam("from", from_)
        paramsDecoder.setParam("to", to_)
        return TopSitesWriter.getRequest(self, paramsDecoder)


