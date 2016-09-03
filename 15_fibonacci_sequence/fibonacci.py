#!/usr/bin/env python
import sys

def fibonacci(n):
    cnt = 0
    f_zero = 0
    f_one = 1
    while n > cnt:
        f_two = f_zero + f_one
        f_zero = f_one
        f_one = f_two
        cnt += 1
    return f_zero

if __name__ == "__main__":
    args = sys.argv
    n = int(args[1])
    ret = fibonacci(n)
    print(ret)