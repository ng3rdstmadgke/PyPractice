#!/usr/bin/env

def power_1(a, n):
    ret = 1
    for i in range(n):
        ret *= a
    return ret

def power_2(a, n):
    if n == 0:
        return 1
    ret = power_2(a*a, n//2)
    if n % 2 != 0:
        ret *= a
    return ret

if __name__ == "__main__":
    print(power_1(3, 21))
    print(power_2(3,21))