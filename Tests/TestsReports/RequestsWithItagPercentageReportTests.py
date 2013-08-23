'''
Created on Aug 15, 2013

@author: asaf
'''
from DAL import *
from Reports import *
from HttpObjects.HTTP_Constants import UserAgent
from Tests import TestResult
from Queries import TruncateDB
from HttpObjects import *


class RequestsWithItagPercentageReportTests :
    
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
        r=ItagStatisticsReport.ItagStatisticsReport(1,1)
        r1=r.loadResults()
        #Make sure correct message is shown
        if(r1 != "***Empty Database - Cannot complete ItagStatisticsReport.loadResults***\n"):
            result.append(TestResult.TestResult(False, "RequestsWithItagPercentageReportTests : Part1 - Test Empty DB : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsWithItagPercentageReportTests : Part1 - Test Empty DB : pass"))
        
        #Part2:
        
        #Generate several Transactions:
        translist = []
        for i in range (0, 10) :
            trans = Transaction.Transaction(1, "2013-02-12 09:33:09", 2, 1484380411543127206, "Static-YOUTUBE", 16377, "24.144.25.215", 52565, "199.59.103.141", 80, 551344839, i+1, 1809500)
            translist.append(trans)
        #Generate several Requests:
        reqslist = []
        for i in range (0, 10) :
            req = Request.Request(1, 1.1, i+1, "GET")
            reqslist.append(req)
        #Generate a list of Request Params (for the test, each trans-req will have only one param):
        reqparamslist= []
        param_names = ["bla", "bla", "itag", "itag", "itag", "bla", "bla", "itag", "itag", "itag"]
        param_values = [0, 0, 1, 2, 2, 0, 0, 1, 2, 3]
        for i in range (0, 10) :
            reqparam = ReqParam.ReqParam((),i+1, param_names[i], param_values[i])
            reqparamslist.append(reqparam)
        #Insert to empty DB:
        TransactionHandler.TransactionHandler().insertTransactionsList(translist)
        RequestHandler.RequestsHandler().insertRequestsList(reqslist)
        RequestHandler.RequestsHandler().insertReqParamsList(reqparamslist)
        #Test!
        r1=r.loadResults()
        if(r.distinct != [1,2,3]) :
            result.append(TestResult.TestResult(False, "RequestsWithItagPercentageReportTests : Part2 - Distinct values of itag : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsUserAgentPercentageReportTests : Part2 - Distinct values of itag : pass"))
        
        if (r.count != [2,3,1]) :
            result.append(TestResult.TestResult(False, "RequestsWithItagPercentageReportTests : Part2 - itag values count : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsUserAgentPercentageReportTests : Part2 - itag values count : pass"))
        
        if (r.percent_trans != [20, 30, 10]) :
            result.append(TestResult.TestResult(False, "RequestsWithItagPercentageReportTests : Part2 - Trans. Percentage of itag values : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsUserAgentPercentageReportTests : Part2 - Trans. Percentage of itag values : pass"))
        
        if (r.percent_bytes != [20, 30, 10]) :
            result.append(TestResult.TestResult(False, "RequestsWithItagPercentageReportTests : Part2 - Bytes. Percentage of itag values : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsUserAgentPercentageReportTests : Part2 - Bytes. Percentage of itag values : pass"))
        
        return result
    
#test= RequestsWithItagPercentageReportTests().RunTests()
#for i in range(0, len(test)):
#    print(test[i].details)