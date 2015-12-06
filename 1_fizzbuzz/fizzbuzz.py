#!/usr/bin/env python3


def fizzbuzz(num):
    ret = ""
    if num % 3 == 0:
        ret += "Fizz"
    if num % 5 == 0:
        ret += "Buzz"
    if (num % 3 != 0) and (num % 5 != 0):
        ret += str(num)
    return ret


def fizzbuzz_all(end_num):
    ret = ""
    for i in range(1, end_num + 1):
        ret += fizzbuzz(i) + " "
    return ret.strip()

if __name__ == "__main__":
    input = input("数字を入力:")
    print(fizzbuzz_all(int(input)))