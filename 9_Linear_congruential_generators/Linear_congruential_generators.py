#!/usr/bin/env python
from decimal import *
def linear_congruential_generator():
    M = Decimal("65536")
    A = Decimal("997")
    B = Decimal("1")
    x = Decimal("12345")
    random_num = []
    for i in range(100):
        ret = (A * x + B) % M
        random_num.append(ret / Decimal(100000))
        x=ret
    return random_num

if __name__ == "__main__":
    a = linear_congruential_generator()
    for cnt, i in enumerate(a):
        # 四捨五入した数を表示する
        print(i.quantize(Decimal("1.0000"), rounding=ROUND_HALF_UP), end=" ")
        if (cnt + 1) % 10 == 0:
            print("")