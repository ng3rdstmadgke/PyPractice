#!/usr/bin/env python3

from decimal import Decimal


def squere_root(num):
    return Decimal(str(num)) ** Decimal("0.5")

if __name__ == "__main__":
    print(squere_root(2))

