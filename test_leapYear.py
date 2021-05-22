import leapYear
import unittest

class TestCase (unittest.TestCase):
    def testOne(self):
        self.assertEqual(leapYear.isLeapYear(400),True)

    def testTwo(self):
        self.assertEqual(leapYear.isLeapYear(2021),True)

    def testThree(self):
        self.assertEqual(leapYear.isLeapYear(2020),True)

    def testFour(self):
        self.assertEqual(leapYear.isLeapYear("Dog"),False)

if __name__ == '__main__':
    unittest.main()
