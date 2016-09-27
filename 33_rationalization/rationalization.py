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
    prime_factors = []
    # 素因数分解を行う
    while n != 1:
        for i in prime_list:
            if n % i == 0:
                n //= i
                prime_factors.append(i)
                break
    # 平方根を整理する
    prime_factors = [(i, prime_factors.count(i)) for i in list(set(prime_factors))]
    odd = 1
    even = 1
    for i in prime_factors:
        if i[1] // 2 > 0:
            even *= (i[0] ** (i[1] // 2))
        if i[1] % 2 == 1:
            odd *= i[0]
    return even, odd

def calc_gcd(a, b):
    # ユークリッドの互除法
    if a > b:
        big, small = a, b
    else:
        big, small = b, a
    while big % small != 0:
        big, small = small, big % small
    return small

def rationalization(prime_list, numerator, denominator):
    # 分子と分母の平方根を整理する
    numer = prime_factorization(prime_list, numerator)
    denom = prime_factorization(prime_list, denominator)
    # 分子のroot部分に分母のroot部分を掛ける
    tmp = prime_factorization(prime_list, numer[1]*denom[1])
    tmp_numer = (numer[0]*tmp[0], tmp[1])
    # 分母のroot部分に分母のroot部分を掛ける
    tmp_denom = (denom[0]*denom[1], 1)
    # 分母と分子の整数部分の最大公約数を求める
    gcd = calc_gcd(tmp_numer[0], tmp_denom[0])
    opt_numer = (tmp_numer[0] // gcd, tmp_numer[1])
    opt_denom = (tmp_denom[0] // gcd, tmp_denom[1])
    return opt_numer, opt_denom

def format_result(fraction):
    ret = ""
    for cnt, i in enumerate(fraction):
        if (i[0] == 1 and i[1] == 1) or i[0] != 1:
            ret += str(i[0])
        if i[1] != 1:
            ret += "√{}".format(i[1])
        if cnt == 0 and (fraction[1][0] != 1 or fraction[1][1] != 1):
            ret += "/"
        else:
            break
    return ret

if __name__ == "__main__":
    pl = gen_prime_list(10000)
    for i in range(1, 101):
        for j in range(2, 101):
            ret = rationalization(pl, i, j)
            print("√{}/√{} -> ".format(i, j), format_result(ret))

