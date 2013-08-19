import datetime

import unittest2


class Test_Assertions(unittest2.TestCase):
    def test_AlmostEqual(self):
        self.assertAlmostEqual(1.00000001, 1.0)
        self.assertNotAlmostEqual(1.0000001, 1.0)
        self.assertRaises(self.failureException,
                          self.assertAlmostEqual, 1.0000001, 1.0)
        self.assertRaises(self.failureException,
                          self.assertNotAlmostEqual, 1.00000001, 1.0)

        self.assertAlmostEqual(1.1, 1.0, places=0)
        self.assertRaises(self.failureException,
                          self.assertAlmostEqual, 1.1, 1.0, places=1)

        self.assertAlmostEqual(0, .1+.1j, places=0)
        self.assertNotAlmostEqual(0, .1+.1j, places=1)
        self.assertRaises(self.failureException,
                          self.assertAlmostEqual, 0, .1+.1j, places=1)
        self.assertRaises(self.failureException,
                          self.assertNotAlmostEqual, 0, .1+.1j, places=0)

        try:
            self.assertAlmostEqual(float('inf'), float('inf'))
            self.assertRaises(self.failureException, self.assertNotAlmostEqual,
                              float('inf'), float('inf'))
        except ValueError:
            # float('inf') is invalid on Windows in Python 2.4 / 2.5
            x = object()
            self.assertAlmostEqual(x, x)
            self.assertRaises(self.failureException, self.assertNotAlmostEqual,
                              x, x)
            
            
    def test_AmostEqualWithDelta(self):
        self.assertAlmostEqual(1.1, 1.0, delta=0.5)
        self.assertAlmostEqual(1.0, 1.1, delta=0.5)
        self.assertNotAlmostEqual(1.1, 1.0, delta=0.05)
        self.assertNotAlmostEqual(1.0, 1.1, delta=0.05)
        
        self.assertRaises(self.failureException, self.assertAlmostEqual,
                          1.1, 1.0, delta=0.05)
        self.assertRaises(self.failureException, self.assertNotAlmostEqual,
                          1.1, 1.0, delta=0.5)
        
        self.assertRaises(TypeError, self.assertAlmostEqual,
                          1.1, 1.0, places=2, delta=2)
        self.assertRaises(TypeError, self.assertNotAlmostEqual,
                          1.1, 1.0, places=2, delta=2)
        
        first = datetime.datetime.now()
        second = first + datetime.timedelta(seconds=10)
        self.assertAlmostEqual(first, second,
                               delta=datetime.timedelta(seconds=20))
        self.assertNotAlmostEqual(first, second,
                                  delta=datetime.timedelta(seconds=5))

    def testAssertNotRegexpMatches(self):
        self.assertNotRegexpMatches('Ala ma kota', r'r+')
        try:
            self.assertNotRegexpMatches('Ala ma kota', r'k.t', 'Message')
        except self.failureException, e:
            self.assertIn("'kot'", e.args[0])
            self.assertIn('Message', e.args[0])
        else:
            self.fail('assertNotRegexpMatches should have failed.')


class TestLongMessage(unittest2.TestCase):
    """Test that the individual asserts honour longMessage.
    This actually tests all the message behaviour for
    asserts that use longMessage."""

    def setUp(self):
        class TestableTestFalse(unittest2.TestCase):
            longMessage = False
            failureException = self.failureException

            def testTest(self):
                pass

        class TestableTestTrue(unittest2.TestCase):
            longMessage = True
            failureException = self.failureException

            def testTest(self):
                pass

        self.testableTrue = TestableTestTrue('testTest')
        self.testableFalse = TestableTestFalse('testTest')

    def testDefault(self):
        self.assertTrue(unittest2.TestCase.longMessage)

    def test_formatMsg(self):
        self.assertEquals(self.testableFalse._formatMessage(None, "foo"), "foo")
        self.assertEquals(self.testableFalse._formatMessage("foo", "bar"), "foo")

        self.assertEquals(self.testableTrue._formatMessage(None, "foo"), "foo")
        self.assertEquals(self.testab