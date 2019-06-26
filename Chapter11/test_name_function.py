import unittest
from Chapter11.name_function import get_formatted_name, get_formatted_name1, get_formatted_name2

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理向Janis Joplin 这样的名字吗"""
        formatted_name = get_formatted_name2('aa', 'bb')
        self.assertEqual(formatted_name, 'Aa Bb')

    def test_first_last_middle_name(self):
        """能正确处理Wolfgang Amadeus Mozart这种姓名"""
        formatted_name = get_formatted_name2('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()