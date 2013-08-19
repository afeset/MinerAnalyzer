import sys
import types

import unittest2


class Test_TestLoader(unittest2.TestCase):

    ### Tests for TestLoader.loadTestsFromTestCase
    ################################################################

    # "Return a suite of all tests cases contained in the TestCase-derived
    # class testCaseClass"
    def test_loadTestsFromTestCase(self):
        class Foo(unittest2.TestCase):
            def test_1(self): pass
            def test_2(self): pass
            def foo_bar(self): pass

        tests = unittest2.TestSuite([Foo('test_1'), Foo('test_2')])

        loader = unittest2.TestLoader()
        self.assertEqual(loader.loadTestsFromTestCase(Foo), tests)

    # "Return a suite of all tests cases contained in the TestCase-derived
    # class testCaseClass"
    #
    # Make sure it does the right thing even if no tests were found
    def test_loadTestsFromTestCase__no_matches(self):
        class Foo(unittest2.TestCase):
            def foo_bar(self): pass

        empty_suite = unittest2.TestSuite()

        loader = unittest2.TestLoader()
        self.assertEqual(loader.loadTestsFromTestCase(Foo), empty_suite)

    # "Return a suite of all tests cases contained in the TestCase-derived
    # class testCaseClass"
    #
    # What happens if loadTestsFromTestCase() is given an object
    # that isn't a subclass of TestCase? Specifically, what happens
    # if testCaseClass is a subclass of TestSuite?
    #
    # This is checked for specifically in the code, so we better add a
    # test for it.
    def test_loadTestsFromTestCase__TestSuite_subclass(self):
        class NotATestCase(unittest2.TestSuite):
            pass

        loader = unittest2.TestLoader()
        try:
            loader.loadTestsFromTestCase(NotATestCase)
        except TypeError:
            pass
        else:
            self.fail('Should raise TypeError')

    # "Return a suite of all tests cases contained in the TestCase-derived
    # class testCaseClass"
    #
    # Make sure loadTestsFromTestCase() picks up the default test method
    # name (as specified by TestCase), even though the method name does
    # not match the default TestLoader.testMethodPrefix string
    def test_loadTestsFromTestCase__default_method_name(self):
        class Foo(unittest2.TestCase):
            def runTest(self):
                pass

        loader = unittest2.TestLoader()
        # This has to be false for the test to succeed
        self.assertFalse('runTest'.startswith(loader.testMethodPrefix))

        suite = loader.loadTestsFromTestCase(Foo)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [Foo('runTest')])

    ################################################################
    ### /Tests for TestLoader.loadTestsFromTestCase

    ### Tests for TestLoader.loadTestsFromModule
    ################################################################

    # "This method searches `module` for classes derived from TestCase"
    def test_loadTestsFromModule__TestCase_subclass(self):
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass
        m.testcase_1 = MyTestCase

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, loader.suiteClass)

        expected = [loader.suiteClass([MyTestCase('test')])]
        self.assertEqual(list(suite), expected)

    # "This method searches `module` for classes derived from TestCase"
    #
    # What happens if no tests are found (no TestCase instances)?
    def test_loadTestsFromModule__no_TestCase_instances(self):
        m = types.ModuleType('m')

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [])

    # "This method searches `module` for classes derived from TestCase"
    #
    # What happens if no tests are found (TestCases instances, but no tests)?
    def test_loadTestsFromModule__no_TestCase_tests(self):
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            pass
        m.testcase_1 = MyTestCase

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, loader.suiteClass)

        self.assertEqual(list(suite), [loader.suiteClass()])

    # "This method searches `module` for classes derived from TestCase"s
    #
    # What happens if loadTestsFromModule() is given something other
    # than a module?
    #
    # XXX Currently, it succeeds anyway. This flexibility
    # should either be documented or loadTestsFromModule() should
    # raise a TypeError
    #
    # XXX Certain people are using this behaviour. We'll add a test for it
    def test_loadTestsFromModule__not_a_module(self):
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass

        class NotAModule(object):
            test_2 = MyTestCase

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromModule(NotAModule)

        reference = [unittest2.TestSuite([MyTestCase('test')])]
        self.assertEqual(list(suite), reference)


    # Check that loadTestsFromModule honors (or not) a module
    # with a load_tests function.
    def test_loadTestsFromModule__load_tests(self):
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass
        m.testcase_1 = MyTestCase

        load_tests_args = []
        def load_tests(loader, tests, pattern):
            self.assertIsInstance(tests, unittest2.TestSuite)
            load_tests_args.extend((loader, tests, pattern))
            return tests
        m.load_tests = load_tests

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, unittest2.TestSuite)
        self.assertEquals(load_tests_args, [loader, suite, None])

        load_tests_args = []
        suite = loader.loadTestsFromModule(m, use_load_tests=False)
        self.assertEquals(load_tests_args, [])

    def test_loadTestsFromModule__faulty_load_tests(self):
        m = types.ModuleType('m')

        def load_tests(loader, tests, pattern):
            raise TypeError('some failure')
        m.load_tests = load_tests

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, unittest2.TestSuite)
        self.assertEqual(suite.countTestCases(), 1)
        test = list(suite)[0]
        
        self.assertRaisesRegexp(TypeError, "some failure", test.m)
        

    ################################################################
    ### /Tests for TestLoader.loadTestsFromModule()

    ### Tests for TestLoader.loadTestsFromName()
    ################################################################

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # Is ValueError raised in response to an empty name?
    def test_loadTestsFromName__empty_name(self):
        loader = unittest2.TestLoader()

        try:
            loader.loadTestsFromName('')
        except ValueError, e:
            self.assertEqual(str(e), "Empty module name")
        else:
            self.fail("TestLoader.loadTestsFromName failed to raise ValueError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # What happens when the name contains invalid characters?
    def test_loadTestsFromName__malformed_name(self):
        loader = unittest2.TestLoader()

        # XXX Should this raise ValueError or ImportError?
        try:
            loader.loadTestsFromName('abc () //')
        except ValueError:
            pass
        except ImportError:
            pass
        else:
            self.fail("TestLoader.loadTestsFromName failed to raise ValueError")

    # "The specifier name is a ``dotted name'' that may resolve ... to a
    # module"
    #
    # What happens when a module by that name can't be found?
    def test_loadTestsFromName__unknown_module_name(self):
        loader = unittest2.TestLoader()

        try:
            loader.loadTestsFromName('sdasfasfasdf')
        except ImportError, e:
            self.assertEqual(str(e), "No module named sdasfasfasdf")
        else:
            self.fail("TestLoader.loadTestsFromName failed to raise ImportError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # What happens when the module is found, but the attribute can't?
    def test_loadTestsFromName__unknown_attr_name(self):
        loader = unittest2.TestLoader()

        try:
            loader.loadTestsFromName('unittest2.sdasfasfasdf')
        except AttributeError, e:
            self.assertEqual(str(e), "'module' object has no attribute 'sdasfasfasdf'")
        else:
            self.fail("TestLoader.loadTestsFromName failed to raise AttributeError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # What happens when we provide the module, but the attribute can't be
    # found?
    def test_loadTestsFromName__relative_unknown_name(self):
        loader = unittest2.TestLoader()

        try:
            loader.loadTestsFromName('sdasfasfasdf', unittest2)
        except AttributeError, e:
            self.assertEqual(str(e), "'module' object has no attribute 'sdasfasfasdf'")
        else:
            self.fail("TestLoader.loadTestsFromName failed to raise AttributeError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    # ...
    # "The method optionally resolves name relative to the given module"
    #
    # Does loadTestsFromName raise ValueError when passed an empty
    # name relative to a provided module?
    #
    # XXX Should probably raise a ValueError instead of an AttributeError
    def test_loadTestsFromName__relative_empty_name(self):
        loader = unittest2.TestLoader()

        try:
            loader.loadTestsFromName('', unittest2)
        except AttributeError:
            pass
        else:
            self.fail("Failed to raise AttributeError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    # ...
    # "The method optionally resolves name relative to the given module"
    #
    # What happens when an impossible name is given, relative to the provided
    # `module`?
    def test_loadTestsFromName__relative_malformed_name(self):
        loader = unittest2.TestLoader()

        # XXX Should this raise AttributeError or ValueError?
        try:
            loader.loadTestsFromName('abc () //', unittest2)
        except ValueError:
            pass
        except AttributeError:
            pass
        else:
            self.fail("TestLoader.loadTestsFromName failed to raise ValueError")

    # "The method optionally resolves name relative to the given module"
    #
    # Does loadTestsFromName raise TypeError when the `module` argument
    # isn't a module object?
    #
    # XXX Accepts the not-a-module object, ignorning the object's type
    # This should raise an exception or the method name should be changed
    #
    # XXX Some people are relying on this, so keep it for now
    def test_loadTestsFromName__relative_not_a_module(self):
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass

        class NotAModule(object):
            test_2 = MyTestCase

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromName('test_2', NotAModule)

        reference = [MyTestCase('test')]
        self.assertEqual(list(suite), reference)

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # Does it raise an exception if the name resolves to an invalid
    # object?
    def test_loadTestsFromName__relative_bad_object(self):
        m = types.ModuleType('m')
        m.testcase_1 = object()

        loader = unittest2.TestLoader()
        try:
            loader.loadTestsFromName('testcase_1', m)
        except TypeError:
            pass
        else:
            self.fail("Should have raised TypeError")

    # "The specifier name is a ``dotted name'' that may
    # resolve either to ... a test case class"
    def test_loadTestsFromName__relative_TestCase_subclass(self):
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass
        m.testcase_1 = MyTestCase

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromName('testcase_1', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [MyTestCase('test')])

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    def test_loadTestsFromName__relative_TestSuite(self):
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass
        m.testsuite = unittest2.TestSuite([MyTestCase('test')])

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromName('testsuite', m)
        self.assertIsInstance(suite, loader.suiteClass)

        self.assertEqual(list(suite), [MyTestCase('test')])

    # "The specifier name is a ``dotted name'' that may resolve ... to
    # ... a test method within a test case class"
    def test_loadTestsFromName__relative_testmethod(self):
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass
        m.testcase_1 = MyTestCase

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromName('testcase_1.test', m)
        self.assertIsInstance(suite, loader.suiteClass)

        self.assertEqual(list(suite), [MyTestCase('test')])

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # Does loadTestsFromName() raise the proper exception when trying to
    # resolve "a test method within a test case class" that doesn't exist
    # for the given name (relative to a provided module)?
    def test_loadTestsFromName__relative_invalid_testmethod(self):
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass
        m.testcase_1 = MyTestCase

        loader = unittest2.TestLoader()
        try:
            loader.loadTestsFromName('testcase_1.testfoo', m)
        except AttributeError, e:
            self.assertEqual(str(e), "type object 'MyTestCase' has no attribute 'testfoo'")
        else:
            self.fail("Failed to raise AttributeError")

    # "The specifier name is a ``dotted name'' that may resolve ... to
    # ... a callable object which returns a ... TestSuite instance"
    def test_loadTestsFromName__callable__TestSuite(self):
        m = types.ModuleType('m')
        testcase_1 = unittest2.FunctionTestCase(lambda: None)
        testcase_2 = unittest2.FunctionTestCase(lambda: None)
        def return_TestSuite():
            return unittest2.TestSuite([testcase_1, testcase_2])
        m.return_TestSuite = return_TestSuite

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromName('return_TestSuite', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [testcase_1, testcase_2])

    # "The specifier name is a ``dotted name'' that may resolve ... to
    # ... a callable object which returns a TestCase ... instance"
    def test_loadTestsFromName__callable__TestCase_instance(self):
        m = types.ModuleType('m')
        testcase_1 = unittest2.FunctionTestCase(lambda: None)
        def return_TestCase():
            return testcase_1
        m.return_TestCase = return_TestCase

        loader = unittest2.TestLoader()
        suite = loader.loadTestsFromName('return_TestCase', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [testcase_1])

    # "The specifier name is a ``dotted name'' that may resolve ... to
    # ... a callable object which returns a TestCase ... instance"
    #*****************************************************************
    #Override the suiteClass attribute to ensure that the suiteClass
    #attribute is used
    def test_loadTestsFromName__callable__TestCase_instance_ProperSuiteClass(self):
        class SubTestSuite(unittest2.TestSuite):
            pass
        m = types.ModuleType('m')
        testcase_1 = unittest2.FunctionTestCase(lambda: None)
        def return_TestCase():
            return testcase_1
        m.return_TestCase = return_TestCase

        loader = unittest2.TestLoader()
        loader.suiteClass = SubTestSuite
        suite = loader.loadTestsFromName('return_TestCase', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [testcase_1])

    # "The specifier name is a ``dotted name'' that may resolve ... to
    # ... a test method within a test case class"
    #*****************************************************************
    #Override the suiteClass attribute to ensure that the suiteClass
    #attribute is used
    def test_loadTestsFromName__relative_testmethod_ProperSuiteClass(self):
        class SubTestSuite(unittest2.TestSuite):
            pass
        m = types.ModuleType('m')
        class MyTestCase(unittest2.TestCase):
            def test(self):
                pass
        m.testcase_1 = MyTestCase

        loader = unittest2.TestLoader()
        loader.suiteClass=SubTestSuite
        suite = loader.loadTestsFromName('testcase_1.test', m)
        self.assertIsInstance(suite, loader.suiteClass)

        self.assertEqual(list(suite), [MyTestCase('test')])

    # "The specifier name is a ``dotted name'' that may resolve ... to
    # ... a callable object which returns a TestCase or TestSuite instance"
    #
    # What happens if the callable returns something else?
    def test_loadTestsFromName__callable__wrong_type(self):
        m = types.ModuleType('m')
        def return_wrong():
            return 6
        m.return_wrong = return_wrong

        loader = unittest2.TestLoader()
        try:
            loader.loadTestsFromName('return_wrong', m)
        except TypeError:
            pass
        else:
            self.fail("TestLoader.loadTestsFromName failed to raise TypeError")

    # "The specifier can refer to modules and packages which have not been
    # imported; they will be imported as a side-effect"
    def test_loadTestsFromName__module_not_loaded(self):
        # We're going to try to load this module as a side-effect, so it
        # better not be loaded before we try.
        #
        module_name = 'unittest2.test.dummy'
        sys.modules.pop(module_name, None)

        loader = unittest2.TestLoader()
        try:
            suite = loader.loadTestsFromName(module_name)

            self.assertIsInstance(suite, loader.suiteClass)
            self.assertEqual(list(suite), [])

            # module should now be loaded, thanks to loadTestsFromName()
            self.assertIn(module_name, sys.modules)
        finally:
            if module_name in sys.modules:
                del sys.modules[module_name]

    ################################################################
    ### Tests for TestLoader.loadTestsFromName()

    ### Tests for TestLoader.loadTestsFromNames()
    ################################################################

    # "Similar to loadTestsFromName(), but takes a sequence of names rather
    # than a single name."
    #
    # What happens if that sequence of names is empty?
    def test_loadTestsFromNames__empty_name_list(self):
        loader = unittest2.TestLoader()

        suite = loader.loadTestsFromNames([])
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [])

    # "Similar to loadTestsFromName(), but takes a sequence of names rather
    # than a single name."
    # ...
    # "The method optionally resolves name relative to the given module"
    #
    # What happens if that sequence of names is empty?
    #
    # XXX Should this raise a ValueError or just return an empty TestSuite?
    def test_loadTestsFromNames__relative_empty_name_list(self):
        loader = unittest2.TestLoader()

        suite = loader.loadTestsFromNames([], unittest2)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [])

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # Is ValueError raised in response to an empty name?
    def test_loadTestsFromNames__empty_name(self):
        loader = unittest2.TestLoader()

        try:
            loader.loadTestsFromNames([''])
        except ValueError, e:
            self.assertEqual(str(e), "Empty module name")
        else:
            self.fail("TestLoader.loadTestsFromNames failed to raise ValueError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # What happens when presented with an impossible module name?
    def test_loadTestsFromNames__malformed_name(self):
        loader = unittest2.TestLoader()

        # XXX Should this raise ValueError or ImportError?
        try:
            loader.loadTestsFromNames(['abc () //'])
        except ValueError:
            pass
        except ImportError:
            pass
        else:
            self.fail("TestLoader.loadTestsFromNames failed to raise ValueError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # What happens when no module can be found for the given name?
    def test_loadTestsFromNames__unknown_module_name(self):
        loader = unittest2.TestLoader()

        try:
            loader.loadTestsFromNames(['sdasfasfasdf'])
        except ImportError, e:
            self.assertEqual(str(e), "No module named sdasfasfasdf")
        else:
            self.fail("TestLoader.loadTestsFromNames failed to raise ImportError")

    # "The specifier name is a ``dotted name'' that may resolve either to
    # a module, a test case class, a TestSuite instance, a test method
    # within a test case class, or a callable object which returns a
    # TestCase or TestSuite instance."
    #
    # What happens when the module can be found, bu