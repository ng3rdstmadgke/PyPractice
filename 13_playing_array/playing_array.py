#!/usr/bin/env python

def main(array):
    length = len(array)
    for i in range(1, length):
        array[i] = 0
    return array

if __name__ == "__main__":
    a = [8, 3, 5, 1, 0, 8]
    ret = main(a)
    print(ret)

