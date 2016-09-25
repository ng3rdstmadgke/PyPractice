#!/usr/bin/env python

def olympiad(num):
    FIRST_YEAR = 1896
    ret = []
    for i in range(num):
        ret.append(FIRST_YEAR)
        FIRST_YEAR += 4
    return ret

if __name__ == "__main__":
    ret = olympiad(30)
    for cnt, i in enumerate(ret):
        if i != 1916 and i != 1940:
            print("第{}回 {}年".format(cnt+1, i))
        else:
            pass