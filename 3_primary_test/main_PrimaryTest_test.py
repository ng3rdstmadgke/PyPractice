import unittest
from main import PrimaryTest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ins = PrimaryTest()

    def test_validation_1(self):
        with self.assertRaises(Exception):
            self.ins.validation("hello")

    def test_validation_2(self):
        for i in [-1, 0, 1]:
            with self.assertRaises(Exception):
                self.ins.validation(i)

    def test_judge_primary_True(self):
        p_list = [2, 3, 5]
        ret = self.ins.judge_primary(11, p_list)
        self.assertEqual(ret, True)

    def test_judge_primary_False(self):
        p_list = [2, 3, 5]
        ret = self.ins.judge_primary(25, p_list)
        self.assertEqual(ret, False)

    def test_main_True(self):
        for i in [3, 11, 1021, 15761]:
            ret = self.ins.main(i)
            self.assertEqual(ret, True)

    def test_main_False(self):
        for i in [4, 12, 1023, 15763]:
            ret = self.ins.main(i)
            self.assertEqual(ret, False)

if __name__ == '__main__':
    unittest.main()
