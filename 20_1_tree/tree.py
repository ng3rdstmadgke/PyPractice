#!/usr/bin/env python
from turtle import Turtle

def tree(n, t):
    if n == 1:
        t.forward(10*n)
        t.back(10*n)
        return n
    else:
        t.forward(10*n)
        t.left(15)
        tree(n-1, t)
        t.right(30)
        tree(n-1, t)
        t.left(15)
        t.back(10*n)
        return n



if __name__ == "__main__":
    t = Turtle()
    tree(3, t)
