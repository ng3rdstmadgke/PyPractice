#!/usr/bin/env python

def nabeatu(n):
    ret = []
    for i in range(1, n+1):
        if i % 3 == 0:
            ret.append("Aho")
        elif "3" in str(i):
            ret.append("Aho")
        else:
            ret.append(str(i))
    return ret

if __name__ == "__main__":
    l = nabeatu(40)
    print(l)