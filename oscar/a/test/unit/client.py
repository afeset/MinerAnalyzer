# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: yuvalsh
#
# client.py handles running test modules written in python, utilizing unittest2 test package
# this module is invoked by the tested module, and takes care off all testing procedure.
# basic flow:
# 1.    q-ut uploads a test module.
# 2.    test module imports client, then invokes client.init() using decorator
# 3.    client.init() takes over and runs:
#       a. test module's init()
#       b. __clientInit(), including utservices.start()
#       c. __runTest() (this is where unittest2 kicks in, collecting and running all test in tested module)
#       d. __processResults() in order to transform testResult to a format readble by utservices
#       e. __clientCleanUp(), including utservices.end()
#  module then exits with a rc that signals succsess/failure to q-ut.

# System imports, needed for branchRoot extraction
import os 
import sys
import re
import utcommon
import time
import utservices
import unittest2
import inspect

#===============================================================#
# Global Variables Class and Python path changes
#===============================================================#
class __GlobalVars:
    def __init__ (self):
        self.verbosity = 4;
        self.hasInit = False
        self.msgHeader = "Python test Client: "

        # Add path of current tested module, to enable loading of tests
        (self.dirName, self.fileName) = os.path.split(sys.argv[0])


        # finding the test module name
        (self.testModuleName,self.fileExtension)=os.path.splitext(self.fileName)
        self.logger = ''
        self.startTime = 0
        self.results = utservices.PythonResults()
        self.ExpectMethodFailures = []

# Create GlobalVars instance 
globalVars = __GlobalVars()
globalVars.results.testClassSet.add('moduleLevel')
globalVars.results.testsPerClass['moduleLevel'] = []

# Inhariting utservices into client.services
# Defining options, args so the user could access by 
# client.options, client.args
services = utservices
options = ''
args = ''   
CLIENT = "client"
DEBUG = "debug"

#===============================================================#
# Overloading TestCase object into Fixture, to keep in convention 
# of C++ testing. in the Future, may want to add capacities
# 
#===============================================================#
class Fixture(unittest2.TestCase):
    startTime = None
    currentTestMethodName = ''
    expectList = []

    # private function to retrieve code and line number for expect record in result xml file
    def __getFrameInfo (self):
        lineNumber = inspect.stack()[2][2]
        codeLineIndex = inspect.stack()[2][5]
        codeLine = inspect.stack()[2][4][codeLineIndex]
        codeLine = codeLine.replace('\n',' ')
        codeLine = codeLine.replace('\r',' ')
        return (lineNumber,codeLine)


    # custom expect functionallity
    def expectTrue(self, A, msg=None):
        (lineNumber,codeLine) = self.__getFrameInfo()
        if not A:
            fullmsg = format("%s : expectTrue faild (line %s) %s" % (codeLine,lineNumber,msg))
            self.expectList.append(fullmsg)

    def expectFalse(self, A, msg=None):
        (lineNumber,codeLine) = self.__getFrameInfo()
        if A:
            fullmsg = format("%s : expectFalse faild (line %s) %s" % (codeLine,lineNumber,msg))
            self.expectList.append(fullmsg)

    def expectEqual(self,A,B,msg=None):
        (lineNumber,codeLine) = self.__getFrameInfo()

        if A != B :
            fullmsg = format("%s : expectEqual faild(line %s): %s is not equal to %s %s" %(codeLine,lineNumber,A,B,msg))
            self.expectList.append(fullmsg)

    def expectNotEqual(self,A,B,msg=None):
        (lineNumber,codeLine) = self.__getFrameInfo()
        if A == B:
            fullmsg = format("%s : expectNotEqual faild(line %s): %s is equal to %s %s" %(codeLine,lineNumber,A,B,msg))
            self.expectList.append(fullmsg)

     
    # to be overriden by user
    def setUpTest(self):
        pass

    # to be overriden by user
    def tearDownTest(self):
        pass

    # actual set up conducted before each test
    def setUp(self):
        # init expectList
        self.expectList = []
        self.currentTestMethodName = self._testMethodName
        className = self.__class__.__name__

        # register testmethod in map
        globalVars.results.testClassSet.add(className)

        if (globalVars.results.testsPerClass.has_key(className)):
            newValue = globalVars.results.testsPerClass.get(className)
            newValue.append(self.currentTestMethodName)
            globalVars.results.testsPerClass[className] = newValue;
           
        else:
            globalVars.results.testsPerClass[className] = [self.currentTestMethodName]


        startTime = time.time()

        globalVars.logger("client-test-setup").info("performing setup for %s testcase" % self.currentTestMethodName)
        # check if been asked to skip test by filter
        match = re.search(options.pythonFilter,self.currentTestMethodName)
        if (match == None):
            globalVars.logger("client-test-setup").notice("testcase %s skipped due to filter %s" % (self.currentTestMethodName, options.pythonFilter))
            globalVars.results.timePerTest[self.currentTestMethodName] = "0"
            self.skipTest("test skipped due to filter: %s" % options.pythonFilter)
        # if test name doesn't match filter, procced
        else:
            # Create Local Temp directory
            services.setCurrentTestNameTempDir(self.currentTestMethodName)
            globalVars.startTime = time.time()
            # Run user-written set up
            self.setUpTest()
            

    # Actual tear down conducted after each test
    def tearDown(self):
        duration = time.time()-globalVars.startTime
        timeStr = "%g" % duration
        globalVars.results.timePerTest[self.currentTestMethodName] = timeStr
        globalVars.logger("client-test-setup").info("performing teardown for %s testcase" % self.currentTestMethodName)
        # Run user-written tear down
        self.tearDownTest()

        # check custom expectList, add record to list if contains anything
        if len(self.expectList) > 0:
            aggregetedExpectMsg = "The following expecting methods failed: \n"
            aggregetedExpectMsg += "\n".join("%s" % msg for msg in self.expectList)
            self.fail(aggregetedExpectMsg)

        # check local temp directory is empty
        fileList = os.listdir(services.getTestTempDir())
        if len(fileList) > 0 :
            globalVars.logger("client-test-teardown").notice("files found in temp directory, failing testcase %s" % self.currentTestMethodName)
            # fail test and list all found files
            errMsg = "The following files were found in test temp directory: %s " % (fileList)
            self.fail(errMsg)  
             
#===============================================================#
# A function for adding client options to the command line parser    
# if needed in the future
# @pre start() 
# Note: currently all old options are configured in utservices
#===============================================================#
def __addClientOptions ():
    parser = services.getOptionParser()

    # option to allow skipping of tests in python unit test client
    # default value is empty string, this will assure all testMethods will match
    parser.add_option(utcommon.PYTHON_FILTER_OPTION, dest="pythonFilter", default="",
                    help="python regex used to filter tests")

#===============================================================#
# A function for performing all client-needed init' operations
# before actual testing takes place    
# 
# @pre start() 
# 
#===============================================================#
def __clientInit ():
    global options
    global args
    # adding needed options to the parser
    __addClientOptions()

    # starting utservices
    services.start(globalVars.testModuleName)
    globalVars.logger = services.getLogger().createLogger(CLIENT,DEBUG)
    globalVars.logger("client-init").info("client has finished both user and client init, started services")
    # parse command line arguments
    (options,args) = services.parseArgs()

#===============================================================#
# A function for collecting and running all tests from testModule 
# 
#===============================================================#
def __runTest():
    globalVars.logger("client-run-tests").info("about to run all tests in the tested module")
    # Add tests from testing module
    clientTestLoader = unittest2.TestLoader()
    # main module is the module object representing the original test module who was run
    allTestsSuite = clientTestLoader.loadTestsFromModule(sys.modules['__main__'])

    # Start testing procedue
    testResults = unittest2.TextTestRunner(verbosity=globalVars.verbosity).run(allTestsSuite)
    globalVars.logger("client-run-tests").info("finished running tests, returning testResults object")
    # End test procedure
    return testResults
#===============================================================#
# A function for creating a custom-made results object from
# testResults, in order to pass it to utservices which is blind
# to unittest2 objects.
# 
# @param: testResults object which is not None
#
# @output: equivalent utservices.PythonResults instance
#===============================================================#
def __processResultes(testResults):
    globalVars.logger("client-process-results").info("about to process testing results")

    # gather test statistics
    globalVars.results.testsRun = testResults.testsRun
    globalVars.results.failures = len(testResults.failures)
    globalVars.results.errors = len(testResults.errors)
    globalVars.results.skipped = len(testResults.skipped)
    globalVars.results.wasSuccessful = testResults.wasSuccessful() 

    for className in globalVars.results.testClassSet :
        globalVars.results.failPerClass[className] = 0
        globalVars.results.errorsPerClass[className] = 0
        globalVars.results.skipPerClass[className] = 0

    # arrange records for XML file in records list
    resultDict = {utcommon.PYTHON_TEST_FAIL: testResults.failures,
                  utcommon.PYTHON_TEST_ERROR: testResults.errors, 
                  utcommon.PYTHON_TEST_SKIP: testResults.skipped}

    # test childs failures
    for key,value in resultDict.iteritems() :
        for (test, traceback) in value:
            try:
                methodName = test._testMethodName
                className = test.__class__.__name__

            except:
                # error or exception happend in module level function
                methodName = test.id()
                className = "moduleLevel"
                globalVars.results.testsPerClass[className] = [methodName]
          
            matching = None
            lineNumber = None

            # Get line number from traceback if exists, from the closest frame
            matching = re.findall("line (\d+)",traceback)
            if len(matching) != 0:
                lastLine = max(0,len(matching) - 1)
                lineNumber = matching[lastLine]

    
            matching = None
            # format traceback massage for xml report
    
            if (key == utcommon.PYTHON_TEST_FAIL):
                globalVars.results.failPerClass[className] += 1
                # extracting specific assertion for failures
                matching = re.search('(assert[\w\W]+)',traceback)
            elif (key == utcommon.PYTHON_TEST_ERROR):
                globalVars.results.errorsPerClass[className] += 1
                # extracting specific assertion for errors
                matching = re.search('[\w]+Error[\W\w]+',traceback)
            else:
                globalVars.results.skipPerClass[className] += 1
    
            # combine massage with line number
            msgAttr = traceback
            if (matching != None):
               msgAttr = matching.group(0)
            msgAttr = msgAttr.replace('\n',' ')
            msgAttr = msgAttr.replace('\r',' ')
    
            if lineNumber != None:
                msgAttr += format("(line %s)" % lineNumber)
    
            # extracting specific failed testcase name
            typeAttr = "test: %s" % test.id()
    
            # Add to record list per test
            if globalVars.results.problemTest.has_key(methodName):
                newList = globalVars.results.problemTest.get(methodName)
                newList.append((msgAttr,typeAttr,key))
                globalVars.results.problemTest[methodName] = newList
            else:
                globalVars.results.problemTest[methodName] = [(msgAttr,typeAttr,key)]


    globalVars.logger("client-process-results").info("finished processing test results")
    return globalVars.results

#===============================================================#
# A function for performing all client-needed cleanup operations
# after actual testing takes place.    
# 
# @pre start() 
# @param: utservices.PythonResults object
# 
# @return: 0 for test success, number of failures otherwise
#===============================================================#
def __clientCleanUp (testResults):
    globalVars.logger("client-clean-up").info("about to perform client clean up, including services.end()")
    # closing utservices with passed testResult object
    return services.__endUnittest(testResults)

#===============================================================#
# main running function, called by test module and passed the
# user genereted init function
#
# Note: the second execution is caused when loading test 
# information from testModule.   
#===============================================================#
def main(userInitFunc=None):
    # Execute user generated Init function
    if (userInitFunc != None):
        userInitFunc()

    # Execute Client Init Function
    __clientInit()

    # Conduct Testing
    testResults = __runTest()

    # Conduct Client CleanUp
    results = __processResultes(testResults)
    rc = __clientCleanUp(results)
    globalVars.logger("client").info("finished testing procedure, exiting with return code")
    sys.exit(rc)

