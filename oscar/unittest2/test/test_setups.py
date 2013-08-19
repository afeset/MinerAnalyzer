import sys

from cStringIO import StringIO

import unittest2
from unittest2.test.support import resultFactory


class TestSetups(unittest2.TestCase):
    
    def getRunner(self):
        return unittest2.TextTestRunner(resultclass=resultFactory,
                                          stream=StringIO())
    def runTests(self, *cases):
        suite = unittest2.TestSuite()
        for case in cases:
            tests = unittest2.defaultTestLoader.loadTestsFromTestCase(case)
            suite.addTests(tests)
        
        runner = self.getRunner()
        
        # creating a nested suite exposes some potential bugs
        realSuite = unittest2.TestSuite()
        realSuite.addTest(suite)
        # adding empty suites to the end exposes potential bugs
        suite.addTest(unittest2.TestSuite())
        realSuite.addTest(unittest2.TestSuite())
        return runner.run(realSuite)
    
    def test_setup_class(self):
        class Test(unittest2.TestCase):
            setUpCalled = 0
            @classmethod
            def setUpClass(cls):
                Test.setUpCalled += 1
                unittest2.TestCase.setUpClass()
            def test_one(self):
                pass
            def test_two(self):
                pass
            
        result = self.runTests(Test)
        
        self.assertEqual(Test.setUpCalled, 1)
        self.assertEqual(result.testsRun, 2)
        self.assertEqual(len(result.errors), 0)

    def test_teardown_class(self):
        class Test(unittest2.TestCase):
            tearDownCalled = 0
            @classmethod
            def tearDownClass(cls):
                Test.tearDownCalled += 1
                unittest2.TestCase.tearDownClass()
            def test_one(self):
                pass
            def test_two(self):
                pass
            
        result = self.runTests(Test)
        
        self.assertEqual(Test.tearDownCalled, 1)
        self.assertEqual(result.testsRun, 2)
        self.assertEqual(len(result.errors), 0)
    
    def test_teardown_class_two_classes(self):
        class Test(unittest2.TestCase):
            tearDownCalled = 0
            @classmethod
            def tearDownClass(cls):
                Test.tearDownCalled += 1
                unittest2.TestCase.tearDownClass()
            def test_one(self):
                pass
            def test_two(self):
                pass
            
        class Test2(unittest2.TestCase):
            tearDownCalled = 0
            @classmethod
            def tearDownClass(cls):
                Test2.tearDownCalled += 1
                unittest2.TestCase.tearDownClass()
            def test_one(self):
                pass
            def test_two(self):
                pass
        
        result = self.runTests(Test, Test2)
        
        self.assertEqual(Test.tearDownCalled, 1)
        self.assertEqual(Test2.tearDownCalled, 1)
        self.assertEqual(result.testsRun, 4)
        self.assertEqual(len(result.errors), 0)

    def test_error_in_setupclass(self):
        class BrokenTest(unittest2.TestCase):
            @classmethod
            def setUpClass(cls):
                raise TypeError('foo')
            def test_one(self):
                pass
            def test_two(self):
                pass
        
        result = self.runTests(BrokenTest)
        
        self.assertEqual(result.testsRun, 0)
        self.assertEqual(len(result.errors), 1)
        error, _ = result.errors[0]
        self.assertEqual(str(error), 
                    'setUpClass (%s.BrokenTest)' % __name__)

    def test_error_in_teardown_class(self):
        class Test(unittest2.TestCase):
            tornDown = 0
            @classmethod
            def tearDownClass(cls):
                Test.tornDown += 1
                raise TypeError('foo')
            def test_one(self):
                pass
            def test_two(self):
                pass
            
        class Test2(unittest2.TestCase):
            tornDown = 0
            @classmethod
            def tearDownClass(cls):
                Test2.torn