import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        ret = main.main(5)
        text = "1 : Hellow World!!\n2 : Hellow World!!\n3 : Hellow World!!\n4 : Hellow World!!\n5 : Hellow World!!\n"
        self.assertEqual(ret, text)

if __name__ == '__main__':
    unittest.main()
