"""
Sample Test case
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):

        res = calc.add(5,6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):

        res=calc.subtract(5,6)
        self.assertEqual(res, 1)