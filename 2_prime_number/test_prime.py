import unittest
from prime import Prime


class MyTestCase(unittest.TestCase):
    def test_init(self):
        test_cls = Prime(20)
        self.assertEqual(test_cls.input_num_list, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(test_cls.prime_list, [])

    def test_error(self):
        try:
            test_cls = Prime("gg")
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)
        try:
            test_cls = Prime(-5)
        except ValueError:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

    def test_judge_num(self):
        test_cls = Prime(20)
        a = test_cls._judge_num(5, [2, 3])
        b = test_cls._judge_num(4, [2, 3])
        self.assertEqual(a, True)
        self.assertEqual(b, False)

    def test_remove_prime_from_list(self):
        test_cls = Prime(20)
        list_a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        test_cls._remove_prime_from_list(2, list_a)
        test_cls._remove_prime_from_list(3, list_a)
        self.assertEqual(list_a, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_judge_all(self):
        test_cls = Prime(100)
        ret = test_cls.judge_all()
        self.assertEqual(ret,
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97])


if __name__ == '__main__':
    unittest.main()
