#!/usr/bin/env python

def prime_list_gen(n):
    # 指定された数までの素数をリストで返す
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

def prime_factorization(prime_list, n):
    # 素因数分解を行う
    elem_list = []
    while n != 1:
        for i in prime_list:
            if n % i == 0:
                n = n // i
                elem_list.append(i)
                break
    # 素因数のリストを元に平方根の形にする
    elem_cnt_list = [(i, elem_list.count(i)) for i in list(set(elem_list))]
    even = 1
    odd = 1
    for i, cnt_i in elem_cnt_list:
        mod = cnt_i % 2
        quot = cnt_i // 2
        if mod == 1:
            odd *= i
        if quot > 0:
            even *= (i**quot)
    return (even, odd)


if __name__ == "__main__":
    n = 10000
    pl = prime_list_gen(n) # 23322452
    print("√1 -> 1")
    for i in range(2, n+1):
        ret = prime_factorization(pl, i)
        if ret[0] == 1:
            print("√{} -> √{}".format(i, ret[1]))
        elif ret[1] == 1:
            print("√{} -> {}".format(i, ret[0]))
        else:
            print("√{} -> {}√{}".format(i, ret[0], ret[1]))
