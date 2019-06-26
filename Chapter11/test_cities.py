import unittest
from Chapter11.city_functions import city_function, city_function1, city_function3

class CityTestCase(unittest.TestCase):

    def test_city_format(self):
        formatted_city = city_function('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_format1(self):
        formatted_city = city_function1('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_format2(self):
        formatted_city = city_function3('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_format3(self):
        formatted_city = city_function3('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()