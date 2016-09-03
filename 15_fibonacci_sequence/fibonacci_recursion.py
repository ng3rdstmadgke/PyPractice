#!/usr/bin/env python
import sys

def fibonacci_recursion(n, cnt=0, f_zero=0, f_one=1):
    if cnt == n:
        return f_zero
    f_two = f_zero + f_one
    cnt += 1
    ret = fibonacci_recursion(n, cnt, f_one, f_two)
    return ret

if __name__ == "__main__":
    args = sys.argv
    n = int(args[1])
    ret = fibonacci_recursion(n)
    print(ret)