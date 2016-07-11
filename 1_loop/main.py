#!/usr/bin/env python3
def main(num):
    ret = ""
    for i in range(num):
        ret += "{} : Hellow World!!".format(i + 1)
        ret += "\n"

    return ret

if __name__=="__main__":
    hello = main(10)
    print(hello)