'''
Created on Aug 15, 2013

@author: asaf
'''
from DAL import *
from Reports import *
from Tests import TestResult
from Queries import TruncateDB
from HttpObjects import *

class RequestsPercentagePerHeaderReportTests :
    
    def RunTests(self):
        '''Test scenario :
        Part #1:
        1. Clean DB
        2. Test behavior for empty DB
        Part #2:
        3. Manually insert data to DB
        4. Check actual results against expected.''' 
        
        #Create list for test results:
        result =[]
        
        #part 1:
        
        #Clean DB:
        TruncateDB.TruncateDB()
        #Run the report:
        r=ReqParamStatisticsReport.ReqParamStatisticsReport(1,1,1)
        r1=r.loadResults()
        #Make sure correct message is shown
        if(r1 != "***Empty Database - Cannot complete ReqParamStatisticsReport.loadResults***\n"):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part1 - Test Empty DB : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part1 - Test Empty DB : pass"))
        
        #Part2:
        
        #Generate several Transactions:
        translist = []
        for i in range (0, 5) :
            trans = Transaction.Transaction(1, "2013-02-12 09:33:09", 2, 1484380411543127206, "Static-YOUTUBE", 16377, "24.144.25.215", 52565, "199.59.103.141", 80, 551344839, i+1, 1809500)
            translist.append(trans)
        #Generate several Requests:
        reqslist = []
        for i in range (0, 5) :
            req = Request.Request(1, 1.1, i+1, "GET")
            reqslist.append(req)
        #Generate a list of Request Params (for the test, each trans-req will have only one param):
        reqparamslist= []
        param_names = ["begin", "bla", "bla", "begin", "bla"]
        param_values = [0, 1, 1, 1, 1]
        for i in range (0, 5) :
            reqparam = ReqParam.ReqParam((),i+1, param_names[i], param_values[i])
            reqparamslist.append(reqparam)
        #Insert to empty DB:
        TransactionHandler.TransactionHandler().insertTransactionsList(translist)
        RequestHandler.RequestsHandler().insertRequestsList(reqslist)
        RequestHandler.RequestsHandler().insertReqParamsList(reqparamslist)
        #Test!
        r1=r.loadResults()
        if(r.RequestsWithBeginURIParamTrans != 40):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Trans.Percentage of Requests with 'begin' URI param (all values) : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Trans. Percentage of Requests with 'begin' URI param (all values) : pass"))
        
        if(r.RequestsWithBeginURIParamBytes != 40):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests with 'begin' URI param (all values) : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests with 'begin' URI param (all values) : pass"))
        
        if(r.NoBeginPercent != 60):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Trans. Percentage of Requests WITHOUT 'begin' URI param : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Trans.Percentage of Requests WITHOUT 'begin' URI param : pass"))
        
        if(r.NoBeginBytes != 60):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests WITHOUT 'begin' URI param : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests WITHOUT 'begin' URI param : pass"))
        
        if(r.RequestsWithBeginEqZeroTrans != 20):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Trans. Percentage of Requests with 'begin' URI param = 0 : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Trans. Percentage of Requests with 'begin' URI param = 0 : pass"))
            
        if(r.RequestsWithBeginEqZeroBytes != 20):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests with 'begin' URI param = 0 : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests with 'begin' URI param = 0 : pass"))
        
        if(r.RequestsWithBeginNotEqZeroBytes != 20):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Trans. Percentage of Requests with 'begin' URI param != 0 : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Trans. Percentage of Requests with 'begin' URI param != 0 : pass"))
        
        if(r.RequestsWithBeginNotEqZeroBytes != 20):
            result.append(TestResult.TestResult(False, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests with 'begin' URI param != 0 : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsPercentagePerHeaderReportTests : Part2 - Bytes Percentage of Requests with 'begin' URI param != 0 : pass"))
        
        
        return result
        #for i in range (0, len(result)) :
        #   print(result[i].details)
        
        