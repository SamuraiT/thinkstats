"""
look up the page 9 of the thinkstats text for the details of this test
chap1 exercise 3
"""

import unittest
import first
class TestFirst(unittest.TestCase):

    def test_number_of_pregnancies(self):
        """check the number of pregnancies"""
        num = first.number_of_pregnancies()
        self.assertEqual(num, 9148)

    def test_categorize_by_birthord(self):
        """check if the first child and second child's number is correct"""
        fch, others = first.categorize_by_birthord()
        self.assertEqual(fch, 4413)
        self.assertEqual(others, 9148 - 4413)

    def test_average_pregnancy_length(self):
        fave, oave = first.average_pregnancy_length()
        print(fave, oave)
        print('difference in days: ', (fave - oave) * 7)

if __name__ == '__main__':
    unittest.main()
