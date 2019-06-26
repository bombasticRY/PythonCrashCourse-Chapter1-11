# 11-3 Practice
class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increament=5000):
        self.salary += increament

import unittest

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('li', 'yi', 5000)


    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(10000, int(self.employee.salary))

    def test_give_custom_raise(self):
        self.employee.give_raise(3000)
        self.assertEqual(8000, int(self.employee.salary))

if __name__ == "__main__":
    unittest.main()