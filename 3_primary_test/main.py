#!/usr/bin/env python3


class PrimaryTest(object):
    def __init__(self):
        pass

    def main(self, num):
        """
        判定対象の数までの素数のリストを作り、そのリストに判定対象を割り切れる数が存在しなければ判定対象を素数と判定。
        :param num: 判定対象の数字
        :return: 判定(bool)と判定に使った素数のリスト(list)
        """
        self.validation(num)
        primary_list = [2]
        judge = True
        if num == 2:
            judge = True
            return judge
        for i in range(2, num):
            if self.judge_primary(i, primary_list) is True:
                primary_list.append(i)
                if self.judge_primary(num, primary_list) is False:
                    judge = False
                    break

        return judge, primary_list

    def judge_primary(self, num, primary_list):
        """
        numがprimary_listに含まれている数字で割り切れたらFalse、割り切れなかったらTrueを返す
        :param num: 判定対象の数字
        :param primary_list: 素数のリスト
        :return: bool
        """
        for i in primary_list:
            if num % i == 0:
                return False
        return True

    def validation(self, arg):
        """
        引数が3以上のintかを判定する。異なっていた場合はエラーを発する。
        :param arg: 3以上のint
        :return: None
        """
        try:
            if isinstance(arg, int) is False:
                raise Exception
            if arg < 2:
                raise Exception
        except Exception:
            raise_text = "An invalid argument exists. (value = {}).".format(arg)
            raise Exception(raise_text)

if __name__ == "__main__":
    ins = PrimaryTest()
    judge, plist = ins.main(333333333331)
    print(judge)
    print(plist)
