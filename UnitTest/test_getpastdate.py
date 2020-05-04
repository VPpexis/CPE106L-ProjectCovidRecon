import sys
import unittest
from getpastdate import getpastdate

class test_getpastdate(unittest.TestCase):
    def test_getpastdate(self):
        self.assertNotEqual(getpastdate(), 123)

if __name__ == '__main__':
   unittest.main()