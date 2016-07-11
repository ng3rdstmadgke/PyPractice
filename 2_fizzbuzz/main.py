#!/usr/bin/env python3

def main(num):
    ret = ""
    for i in range(1, num + 1):
        if i % 3 == 0:
            ret += "Fizz"
        if i % 5 == 0:
            ret += "Buzz"
        if (i % 3 != 0) and (i % 5 != 0):
            ret += str(i)
        ret += " "
    return ret

if __name__ == "__main__":
    fizzbuzz = main(30)
    print(fizzbuzz)


