#!/usr/bin/env python3


class Prime(object):

    def __init__(self, input_num):
        """
        :param input_num: 2以上の正の整数を入力
        self.prime_list : 素数のリスト
        self.input_num_list : 2からinput_numまでのリスト
        """
        if (isinstance(input_num, int) is False) or (input_num < 2):
            raise ValueError("不正な入力値です！2以上の正の整数を入力してください。")
        self.input_num_list = list(range(input_num + 1))[2:]  #[2,3,4,5,6,7,...,input_num]
        self.prime_list = []


    def _judge_num(self, num, prime_list):
        """
        numが素数かどうかを判定
        numがprime_list内の要素で割り切れればFalse,割り切れなければTrue
        :param num: 素数判定の対象
        :param prime_list: 素数のリスト
        :return: bool値
        """
        for i in prime_list:
            if num % i == 0:
                return False
        return True

    def _remove_prime_from_list(self, prime_num, input_num_list):
        """
        input_num_listからprime_numの倍数を削除する。
        :param prime_num:素数
        :param input_num_list:self.input_num_list
        :return:
        """
        for i in input_num_list:
            if (i > prime_num) and (i % prime_num == 0):
                input_num_list.remove(i)

    def judge_all(self):
        """
        input_numまでの素数をリストで返す
        :return:input_numまでの素数のリスト list型
        """
        for i in self.input_num_list:
            if self._judge_num(i, self.prime_list) is True:
                self.prime_list.append(i)
                self._remove_prime_from_list(i, self.input_num_list)
        return self.prime_list

if __name__ == "__main__":
    a = Prime(30)
    print(a.judge_all())
