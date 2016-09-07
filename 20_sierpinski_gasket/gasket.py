#!/usr/bin/env python
from turtle import *

def element(t):
    for i in range(2):
        t.forward(20)
        t.left(120)
    t.forward(10)
    t.left(120)
    for i in range(2):
        t.forward(10)
        t.right(120)
    t.forward(10)
    t.left(120)
    t.forward(10)
    t.left(120)

def gasket(n, t):
    if n  == 1:
        element(t)
        return n
    else:
        side = 10*(2**(n-1))
        gasket(n-1, t)
        t.forward(side)
        gasket(n-1, t)
        t.left(60)
        t.forward(side)
        t.left(120)
        t.forward(side)
        t.right(180)
        gasket(n - 1, t)
        t.right(120)
        t.forward(side)
        t.left(120)
        return n

if __name__ == "__main__":
    t = Turtle()
    #element(t)
    gasket(5, t)
