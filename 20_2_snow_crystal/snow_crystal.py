#!/usr/bin/env python
from turtle import Turtle

def elem(t):
    t.forward(10)
    t.left(60)
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.left(60)
    t.forward(10)

def snow_crystal(n, t):
    if n == 1:
        elem(t)
    else:
        snow_crystal(n-1, t)
        t.left(60)
        snow_crystal(n-1, t)
        t.right(120)
        snow_crystal(n-1, t)
        t.left(60)
        snow_crystal(n-1, t)

if __name__ == "__main__":
    t = Turtle()
    snow_crystal(4, t)