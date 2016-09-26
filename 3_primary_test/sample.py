#!/usr/bin/env python

def prime_list_gen(n):
    if n <= 1:
        raise ValueError("number is too small : n={}".format(n))
    prime_list = []
    for i in range(2, n + 1):
        length = len(prime_list) // 2 + 1
        for j in prime_list[:length]:
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

if __name__ == "__main__":
    n = 100000
    x = n // 2 + 1
    pl = prime_list_gen(x)
    for i in pl:
        if n % i:
            flg = "is not"
            break
    else:
        flg = "is"
    print("{} {} prime".format(n, flg))
