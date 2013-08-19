from unittest2.test.support import EqualityMixin, LoggingResult

import sys
import unittest2

class Test(object):
    class Foo(unittest2.TestCase):
        def test_1(self): pass
        def test_2(self): pass
        def test_3(self): pass
        def runTest(self): pass

def _mk_TestSuite(*names):
    return unittest2.TestSuite(Test.Foo(n) for n in names)


class Test_TestSuite(unittest2.TestCase, EqualityMixin):

    ### Set up attributes needed by inherited tests
    ################################################################

    # Used by EqualityMixin.test_eq
    eq_pairs = [(unittest2.TestSuite(), unittest2.TestSuite()),
                (unittest2.TestSuite(), unittest2.TestSuite([])),
                (_mk_TestSuite('test_1'), _mk_TestSuite('test_1'))]

    # Used by EqualityMixin.test_ne
    ne_pairs = [(unittest2.TestSuite(), _mk_TestSuite('test_1')),
                (unittest2.TestSuite([]), _mk_TestSuite('test_1')),
                (_mk_TestSuite('test_1', 'test_2'), _mk_TestSuite('test_1', 'test_3')),
                (_mk_TestSuite('test_1'), _mk_TestSuite('test_2'))]

    ################################################################
    ### /Set up attributes needed by inherited tests

    ### Tests for TestSuite.__init__
    ################################################################

    # "class TestSuite([tests])"
    #
    # The tests iterable should be optional
    def test_init__tests_optional(self):
        suite = unittest2.TestSuite()

        self.assertEqual(suite.countTestCases(), 0)

    # "class TestSuite([tests])"
    # ...
    # "If tests is given, it must be an iterable of individual test cases
    # or other test suites that will be used to build the suite initially"
    #
    # TestSuite should deal with empty tests iterables by allowing the
    # creation of an empty suite
    def test_init__empty_tests(self):
        suite = unittest2.TestSuite([])

        self.assertEqual(suite.countTestCases(), 0)

    # "class TestSuite([tests])"
    # ...
    # "If tests is given, it must be an iterable of individual test cases
    # or other test suites that will be used to build the suite initially"
    #
    # TestSuite should allow any iterable to provide tests
    def test_init__tests_from_any_iterable(self):
        def tests():
            yield unittest2.FunctionTestCase(lambda: None)
            yield unittest2.FunctionTestCase(lambda: None)

        suite_1 = unittest2.TestSuite(tests())
        self.assertEqual(suite_1.countTestCases(), 2)

        suite_2 = unittest2.TestSuite(suite_1)
        self.assertEqual(suite_2.countTestCases(), 2)

        suite_3 = unittest2.TestSuite(set(suite_1))
        self.assertEqual(suite_3.countTestCases(), 2)

    # "class TestSuite([tests])"
    # ...
    # "If tests is given, it must be an iterable of individual test cases
    # or other test suites that will be used to build the suite initially"
    #
    # Does TestSuite() also allow other TestSuite() instances to be present
    # in the tests iterable?
    def test_init__TestSuite_instances_in_tests(self):
        def tests():
            ftc = unittest2.FunctionTestCase(lambda: None)
            yield unittest2.TestSuite([ftc])
            yield unittest2.FunctionTestCase(lambda: None)

        suite = unittest2.TestSuite(tests())
        self.assertEqual(suite.countTestCases(), 2)

    ################################################################
    ### /Tests for TestSuite.__init__

    # Container types should support the iter protocol
    def test_iter(self):
        test1 = unittest2.FunctionTestCase(lambda: None)
        test2 = unittest2.FunctionTestCase(lambda: None)
        suite = unittest2.TestSuite((test1, test2))

        self.assertEqual(list(suite), [test1, test2])

    # "Return the number of tests represented by the this test object.
    # ...this method is also implemented by the TestSuite class, which can
    # return larger [greater than 1] values"
    #
    # Presumably an empty TestSuite returns 0?
    def test_countTestCases_zero_simple(self):
        sui