import excel_writer
import jpype
import loggers
import os

import a.sys.sys_web.mng.django_app as api

class Exporter:
    def __init__(self):
        self.writers = []
        self.sheetMap = {}
        self.sectionMap = {}

    def addWriter(self, writer):
        self.writers.append(writer)

    def addSection(self, section, sheet):
        """
        Adds logical section which is used in external API
        Section can be mapped to single sheet or to the list of sheets
        """
        self.sectionMap[section] = sheet

    def getTemplateFileName(self):
        raise NotImplementedError

    def createSheetMap(self, workbook):
        sheetNum = workbook.getNumSheets()
        for sheet in range(sheetNum):
            loggers.accessLogger.debug("sheet = %d '%s'" % (sheet, workbook.getSheetName(sheet)))
            self.sheetMap[workbook.getSheetName(sheet)] = sheet

    def processWriter(self, writer, workbook, paramsDecoder):
        requestParams = writer.getRequest(paramsDecoder)
        if requestParams:
            response = excel_writer.Requestor.instance().getResponse(requestParams)
        else:
            response = None
        loggers.accessLogger.debug("processing %s on sheet '%s'" % (writer.__class__.__name__, writer.sheetName))
        writer.write(workbook, response)

    def buildSheetsToExport(self, sectionsParams):
        sheetsToExport = {}
        # map sections
        for (ind, sectionParams) in enumerate(sectionsParams):
            sectionName = sectionParams.get('section')
            loggers.accessLogger.info("sectionName = %s" % sectionName)
            if not sectionName:
                loggers.mainLogger.warning("Section name not specified for index %d" % ind)
                continue
            elif sectionName == "all":
                # export all sheets
                for singleSheet in self.sheetMap.keys():
                    loggers.accessLogger.info("adding sheet %s to export" % singleSheet)
                    sheetsToExport[singleSheet] = (sectionParams, [])
                break
            
            sheet = self.sectionMap.get(sectionName)
            if not sheet:
                loggers.mainLogger.error("Unexisting section %s" % sectionName)
            else:
                if isinstance(sheet, list):
                    for singleSheet in sheet:
                        loggers.accessLogger.info("adding sheet %s to export" % singleSheet)
                        sheetsToExport[singleSheet] = (sectionParams, [])
                else:
                    loggers.accessLogger.info("adding sheet %s to export" % sheet)
                    sheetsToExport[sheet] = (sectionParams, [])
        # distribute writers
        for writer in self.writers:
            sheet = writer.sheetName
            if sheet in sheetsToExport:
                sheetsToExport[sheet][1].append(writer)

        return sheetsToExport

    def export(self, sectionsParams, templateDir, exportFileName):
        loggers.accessLogger.info("Start export")
        WorkBook = jpype.JClass('com.smartxls.WorkBook')
        workbook = WorkBook()

        templateFile = os.path.join(templateDir, self.getTemplateFileName())
        workbook.readXLSX(templateFile)
        loggers.accessLogger.debug("After read of template file '%s'" % templateFile)

        self.createSheetMap(workbook)
        sheetsToExport = self.buildSheetsToExport(sectionsParams)
        
        excel_writer.Requestor.instance().clearCache()
        numSheets = workbook.getNumSheets()
        sheetId = 0
        while sheetId < numSheets:
            sheetName = workbook.getSheetName(sheetId)
            sheet = sheetsToExport.get(sheetName, None)
            if sheet:
                # sheet[0] -> contains section params, sheet[1] -> relevant writers 
                for writer in sheet[1]:
                    workbook.setSheet(sheetId)
                    self.processWriter(writer, workbook, api.systemApiSectionParamsDecoder(sheet[0]))
                sheetId += 1
            else:
                loggers.accessLogger.debug("deleting sheet %d" % sheetId)
                if numSheets == 1:
                    # cannot delete workbook with single sheet so create an empty one and exit
                    workbook.insertSheets(1,1)
                    workbook.deleteSheets(sheetId, 1)
                    break

                workbook.deleteSheets(sheetId, 1)
                numSheets = workbook.getNumSheets()
                loggers.accessLogger.debug("New number of sheets %d" % numSheets)

        excel_writer.Requestor.instance().clearCache()
        workbook.recalc()
        workbook.setSheet(0)
        loggers.accessLogger.info("Writing to export file '%s'" % exportFileName)
        workbook.writeXLSX(exportFileName)
        loggers.accessLogger.debug("After write to export file '%s'" % exportFileName)


class OverviewExporter(Exporter):
    def __init__(self):
        Exporter.__init__(self)
        # define sections
        self.addSection("trafficOverTime", "Main Chart Traffic")
        self.addSection("videoTrafficOverTime", "Main Chart Video Traffic")
        self.addSection("viewTimeOverTime", "Main Chart Stream Duration")
        self.addSection("sessionsOverTime", "Main Chart Sessions")
        self.addSection("subscribersPareto", "Subscriber BW")
        self.addSection("titlesPareto", "Titles BW")

        # specify writers
        self.addWriter(excel_writer.TrafficWriter('Main Chart Traffic', 'A20:D25'))
        self.addWriter(excel_writer.BandwidthWriter('Main Chart Video Traffic', 'A19:E24'))
        self.addWriter(excel_writer.ViewTimeWriter('Main Chart Stream Duration', 'A19:E22'))
        self.addWriter(excel_writer.SessionsWriter('Main Chart Sessions', 'A19:E24'))
        self.addWriter(excel_writer.SubscribersParetoWriter('Subscriber BW', 'A19:D30'))
        self.addWriter(excel_writer.TitlesParetoWriter('Titles BW', 'A19:D30'))
        for sheet in ['Main Chart Traffic', 'Main Chart Video Traffic', 'Main Chart Stream Duration', 'Main Chart Sessions',
                      'Subscriber BW', 'Titles BW']:
            self.addWriter(excel_writer.ReportTimeWriter(sheet, 'B2:C3'))
            self.addWriter(excel_writer.SystemStatusWriter(sheet, 'C4:F7'))
            self.addWriter(excel_writer.CurrentTrafficWriter(sheet, 'A5:B7'))
            self.addWriter(excel_writer.HostnameWriter(sheet, 'B1:B1'))

    def getTemplateFileName(self):
        return "HomePageExport.xlsx"

class ContentExporter(Exporter):
    def __init__(self):
        Exporter.__init__(self)

        # define section to sheet mapping
        self.addSection("trafficOverTime", "Main Chart Traffic")
        self.addSection("videoTrafficOverTime", "Main Chart Video Traffic")
        self.addSection("viewTimeOverTime", "Main Chart Stream Duration")
        self.addSection("sessionsOverTime", "Main Chart Sessions")
        self.addSection("dailyDistribution", "Daily Distribution")
        self.addSection("topSitesByVolume", "Sites By Volume")
        self.addSection("topSitesBySessions", "Sites By Sessions")
        self.addSection("topSitesByViewTime", "Sites By Stream Duration")
        self.addSection("titlesParetoOverTime", "Titles BW")
        self.addSection("topTitlesByVolume", "Titles By Volume")
        self.addSection("topTitlesBySessions", "Titles By Sessions")
        self.addSection("topTitlesByViewTime", "Titles By Stream Duration")
        self.addSection("subscribersParetoOverTime", "Subscriber BW")
        self.addSection("subscribersDailyDistribution", "Subscriber Daily Dist")
        self.addSection("topSubscribersByVolume", "Subscriber By Volume")
        self.addSection("topSubscribersBySessions", "Subscriber By Sessions")
        self.addSection("topSubscribersByViewTime", "Subscriber By Stream Duration")
        self.addSection("trafficPeakTime", "Peak Time - Total Traffic")
        self.addSection("videoTrafficPeakTime", "Peak Time - Total Video")
        self.addSection("viewTimePeakTime", "Peak Time - Stream Duration")
        self.addSection("sessionsPeakTime", "Peak Time - Sessions")
        self.addSection("topSitesByVolumePeakTime", "Peak Time - Sites By Volume")
        self.addSection("topSitesBySessionsPeakTime", "Peak Time - Sites By Sessions")
        self.addSection("topSitesByViewTimePeakTime", "Peak Time - Sites By Stream Dur")

        # specify writers
        self.addWriter(excel_writer.TopSitesWriter('Sites By Volume', 'A21:E25', 'volume', float(excel_writer.GB)))
        self.addWriter(excel_writer.TopSitesWriter('Sites By Sessions', 'A21:E25', 'sessions', 1000.))
        self.addWriter(excel_writer.TopSitesWriter('Sites By Stream Duration', 'A21:E25', 'viewTime', float(excel_writer.DAY)))
        self.addWriter(excel_writer.TopSubscribersWriter('Subscriber By Volume', 'A7:C10', 'volume', float(excel_writer.MB)))
        self.addWriter(excel_writer.TopSubscribersWriter('Subscriber By Sessions', 'A7:C10', 'sessions', 1000.))
        self.addWriter(excel_writer.TopSubscribersWriter('Subscriber By Stream Duration', 'A7:C10', 'viewTime', 3600.))
        self.addWriter(excel_writer.BandwidthWriter('Main Chart Video Traffic', 'A16:E29'))
        self.addWriter(excel_writer.TrafficWriter('Main Chart Traffic', 'A16:D29'))
        self.addWriter(excel_writer.ViewTimeWriter('Main Chart Stream Duration', 'A16:E29'))
        self.addWriter(excel_writer.SessionsWriter('Main Chart Sessions', 'A16:E29'))
        self.addWriter(excel_writer.DailyDistributionWriter('Daily Distribution', 'A16:E40', 'BW', float(excel_writer.Gbps)))
        self.addWriter(excel_writer.DailyDistributionWriter('Daily Distribution', 'A52:E76', 'viewTime', 3600))
        self.addWriter(excel_writer.DailyDistributionWriter('Daily Distribution', 'A88:E112', 'sessions', 1000))
        self.addWriter(excel_writer.DailyDistributionWriter('Subscriber Daily Dist', 'A16:B40', 'subscribers', 1000))
        # System status on all sheets
        for sheet in ["Main Chart Video Traffic", "Main Chart Traffic", "Main Chart Stream Duration", "Main Chart Sessions",
                      "Daily Distribution", "Sites By Volume", "Sites By Sessions", "Sites By Stream Duration",
                      "Titles BW", "Titles By Volume", "Titles By Sessions", "Titles By Stream Duration",
                      "Subscriber BW", "Subscriber Daily Dist", "Subscriber By Volume", "Subscriber By Sessions", "Subscriber By Stream Duration",
                      "Peak Time - Total Traffic", "Peak Time - Total Video", "Peak Time - Stream Duration", "Peak Time - Sessions",
                      "Peak Time - Sites By Volume", "Peak Time - Sites By Sessions", "Peak Time - Sites By Stream Dur"] :
            self.addWriter(excel_writer.ReportTimeWriter(sheet, 'B2:C3'))
            self.addWriter(excel_writer.CurrentTrafficWriter(sheet, 'B4:E4'))
            self.addWriter(excel_writer.HostnameWriter(sheet, 'B1:B1'))

        self.addWriter(excel_writer.TopTitlesWriter('Titles By Volume', 'A7:G18', 'volume', "totalVolume", float(excel_writer.GB), "sessionNumber", 1000))
        self.addWriter(excel_writer.TopTitlesWriter('Titles By Sessions', 'A7:G18', 'sessions', "sessionNumber", 1000, "totalVolume", float(excel_writer.GB)))
        self.addWriter(excel_writer.TopTitlesWriter('Titles By Stream Duration', 'A7:G18', 'viewTime', "totalViewTime", 60, "sessionNumber", 1000))
        self.addWriter(excel_writer.ParetoOverTimeWriter('Titles BW', 'A17:F42', 'titles', [1,5,10,20,30]))
        self.addWriter(excel_writer.ParetoOverTimeWriter('Subscriber BW', 'A16:F41', 'subscribers', [1,5,10,20,30]))
        self.addWriter(excel_writer.PeakTrafficDataWriter("Peak Time - Total Traffic", 'A16:E23'))
        self.addWriter(excel_writer.PeakDataWriter("Peak Time - Total Video", 'A16:E23', "BW", excel_writer.Gbps))
        self.addWriter(excel_writer.PeakDataWriter("Peak Time - Stream Duration", 'A16:E23', "viewTime", excel_writer.DAY))
        self.addWriter(excel_writer.PeakDataWriter("Peak Time - Sessions", 'A16:E23', "sessions", 1000))
        self.addWriter(excel_writer.PeakTopSitesWriter("Peak Time - Sites By Volume", "A21:E25", "volume", float(excel_writer.GB)))
        self.addWriter(excel_writer.PeakTopSitesWriter("Peak Time - Sites By Sessions", "A21:E25", "sessions", 1000))
        self.addWriter(excel_writer.PeakTopSitesWriter("Peak Time - Sites By Stream Dur", "A21:E25", "viewTime", 3600))

    def getTemplateFileName(self):
        return "ReportsExport.xlsx"

