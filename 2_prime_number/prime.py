#!/usr/bin/env python3


class Prime(object):

    def __init__(self, input_num):
        """
        :param input_num: 2以上の正の整数を入力
        self.prime_list : 素数のリスト
        self.num_list : 2からinput_numまでのリスト
        """
        if (isinstance(input_num, int) is False) or (input_num < 2):
            raise ValueError("不正な入力値です！2以上の正の整数を入力してください。")
        self.num_list = list(range(input_num + 1))[2:]  # [2,3,4,5,6,7,...,input_num]

    def _remove_prime_from_list(self, prime_num, num_list):
        """
        num_listからprime_numの倍数を削除する。
        :param prime_num:素数
        :param num_list:self.num_list
        :return:
        """
        for i in num_list:
            if (i > prime_num) and (i % prime_num == 0):
                num_list.remove(i)

    def judge_all(self):
        """
        input_numまでの素数をリストで返す
        :return:input_numまでの素数のリスト list型
        """
        for i in self.num_list:
            self._remove_prime_from_list(i, self.num_list)
        return self.num_list

if __name__ == "__main__":
    a = Prime(100000)
    print(a.judge_all())
