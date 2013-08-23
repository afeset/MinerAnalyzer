'''
Created on Aug 13, 2013

@author: asaf
'''
#This modlue creates instances for all tests and runs them. It returns the number of failed tests.

#from TestsDAL import RequestHandlerTests
from Tests.TestsReports import *

#Counter for tests fail:
count=0
#List for all test results:
testresult=[]

#Reports Tests:

test1 = RequestsPercentagePerHeaderReportTests.RequestsPercentagePerHeaderReportTests().RunTests()
testresult.extend(test1)
#test2 = RequestsUserAgentPercentageReportTests.RequestsUserAgentPercentageReportTests().RunTests()
#testresult.extend(test2)
test3 = RequestsWithItagPercentageReportTests.RequestsWithItagPercentageReportTests().RunTests()
testresult.extend(test3)

#Summary of tests:
for i in range (0, len(testresult)) :
    print(testresult[i].details)
    if testresult[i].isPass == False:
        count = count+1
if count == 0:
    print("\nAll Pass!")
else :
    if count == 1 :
        print("\n"+str(count)+" test has failed. See log details.\n")
    else :
        print("\n"+str(count)+" tests have failed. See log details.\n")



#DAL Tests:

#test=RequestHandlerTests() #create test instanse
#result=test.RunTests() # run the test
#testresult.append(result) # collect results


#... all tests run


#At the end: prinr all results
#for (i in range(0, len(testresult))):
 #   print(i.isPass + " " i.details)