# test_check.py
'''You need to the code of test.py file, you can extract it from AI models or from Copilot from github itself, but the test file should always start from the test name and the file which you are having should not have input and output because it can only test the logic of the code not the ip/op operations''' 

import unittest
from check import calculate_tax   # Importing from your check.py file

class TestCalculateTax(unittest.TestCase):

    def test_salary_below_50000(self):
        self.assertEqual(calculate_tax(40000), 40000 * 0.1)

    def test_salary_above_50000(self):
        self.assertEqual(calculate_tax(60000), 60000 * 0.2)

    def test_salary_equal_50000(self):
        self.assertEqual(calculate_tax(50000), 50000 * 0.1)

# This makes the test run when the file is executed directly
if __name__ == '__main__':
    unittest.main()
