import unittest
from unittest import mock
from main import WordChain

class MyTestCase(unittest.TestCase):
    def setUp(self):
        with open("test_dictionary.txt", "w") as f:
            f.write("ab\nbc\ncd\nde")

    def test_user_input(self):
        wordchain = WordChain("test_dictionary.txt")
        
        mock.MagicMock(return_value="hello")
        ret = wordchain.user_input()
        self.assertEqual(ret, "hello")


if __name__ == '__main__':
    unittest.main()
