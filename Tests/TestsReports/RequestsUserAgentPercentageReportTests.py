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

class RequestsUserAgentPercentageReportTests :
    
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
        r=UseAgentStatisticsReport.UseAgentStatisticsReport(1,1,1)
        r1=r.loadResults()
        #Make sure correct message is shown
        if(r1 != "***Empty Database - Cannot complete UseAgentStatisticsReport.loadResults***\n"):
            result.append(TestResult.TestResult(False, "RequestsUserAgentPercentageReportTests : Part1 - Test Empty DB : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsUserAgentPercentageReportTests : Part1 - Test Empty DB : pass"))
        
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
        reqheaderslist= []
        header_values = ["bla", UserAgent.Nativehost, UserAgent.Playstation, "bla", "bla", UserAgent.PS3, UserAgent.Xbox, "bla", "bla", UserAgent.Zune]
        for i in range (0, 10) :
            reqheader = ReqHeader.ReqHeader((),i+1, "user-agent", header_values[i])
            reqheaderslist.append(reqheader)
        #Insert to empty DB:
        TransactionHandler.TransactionHandler().insertTransactionsList(translist)
        RequestHandler.RequestsHandler().insertRequestsList(reqslist)
        RequestHandler.RequestsHandler().insertReqHeadersList(reqheaderslist)
        #Test!
        r1=r.loadResults()
        if(r.NumberOfTransactionsResult != 50) :
            result.append(TestResult.TestResult(False, "RequestsUserAgentPercentageReportTests : Part2 - Trans. Percentage of Requests with problematic user-agent : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsUserAgentPercentageReportTests : Part2 - Trans. Percentage of Requests with problematic user-agent : pass"))
        
        if(r.NumberOfBytesResult != 50):
            result.append(TestResult.TestResult(False, "RequestsUserAgentPercentageReportTests : Part2 - Bytes Percentage of Requests with problematic user-agent : fail"))
        else:
            result.append(TestResult.TestResult(True, "RequestsUserAgentPercentageReportTests : Part2 - Bytes Percentage of Requests with problematic user-agent : pass"))
        
        return result
    
#test= RequestsUserAgentPercentageReportTests().RunTests()
#for i in range(0, len(test)):
#    print(test[i].details)
    
            