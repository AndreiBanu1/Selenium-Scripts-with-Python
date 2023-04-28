# This sample program demonstrates PyUnit/unittest framework
import time
import unittest
from HtmlTestRunner.runner import HTMLTestRunner

def addition(x, y, z=0):
    return x+y+z

class AddTest(unittest.TestCase):
    def setUp(self):

        pass

    def test_addition(self):
        self.assertEquals(addition(10, 11, 12), 33)
        self.assertNotEquals(addition(11, 12), 44)

    def test_negative_value(self):
        self.assertNotEquals(addition(-9, 25), 6)

    def tear_down(self):

        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader.loadTestsFromTestCase(AddTest))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    runner = HTMLTestRunner(log=True, verbosity=2,
                            output="/Reports",
                            title='Test report', report_name='assertions_report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Andrei B",
                            add_traceback=False)
    runner.run(suite)
