#!/usr/bin/env python3
def main(num):
    for i in range(num):
        ret = "{} : Hellow World!!".format(i + 1)
        print(ret)

if __name__=="__main__":
    main(10)