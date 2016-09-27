#!/usr/bin/env python

def gen_prime_list(n):
    if n < 2:
        raise ValueError("input number {} is too small!!".format(n))
    prime_list = []
    for i in range(2, n + 1):
        flg = True
        for j in prime_list:
            if i % j == 0:
                flg = False
                break
            if j * 2 + 1 > i:
                break
        if flg is True:
            prime_list.append(i)
    return prime_list

def prime_factorization(prime_list, n):
    prime_factor = []
    for i in prime_list:



if __name__ == "__main__":
    pl = gen_prime_list(1000)
    print(pl)

