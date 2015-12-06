#!/usr/bin/env python3
import unittest
from fizzbuzz import fizzbuzz, fizzbuzz_all


class MyTestCase(unittest.TestCase):
    def test_fizz(self):
        fnc = fizzbuzz(6)
        self.assertEqual(fnc, "Fizz")

    def test_buzz(self):
        fnc = fizzbuzz(10)
        self.assertEqual(fnc, "Buzz")

    def test_fizzbuzz(self):
        fnc = fizzbuzz(30)
        self.assertEqual(fnc, "FizzBuzz")

    def test_num(self):
        fnc = fizzbuzz(1)
        self.assertEqual(fnc, "1")

    def test_all(self):
        fnc = fizzbuzz_all(15)
        self.assertEqual(fnc, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz")



if __name__ == '__main__':
    unittest.main()
