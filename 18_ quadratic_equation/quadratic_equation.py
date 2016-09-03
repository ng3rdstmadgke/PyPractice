#!/usr/bin/env python
from decimal import Decimal

def quadratic_equation(a, b, c):
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    ret_a = (-b - (b**Decimal(2) - (Decimal(4)*a*c))**Decimal(0.5))/(Decimal(2)*a)
    ret_b = (-b + (b**Decimal(2) - (Decimal(4)*a*c))**Decimal(0.5))/(Decimal(2)*a)
    return (ret_a, ret_b)

if __name__ == "__main__":
    ret = quadratic_equation(0.0000000045, 10, 1)
    print(ret)