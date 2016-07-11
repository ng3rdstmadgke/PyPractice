import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_main(self):
        ret = main.main(15)
        text = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz "
        self.assertEqual(ret, text)