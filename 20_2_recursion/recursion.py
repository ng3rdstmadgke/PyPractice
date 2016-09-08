#!/usr/bin/env python

def sum(num_list):
    if len(num_list) == 0:
        return 0
    else:
        ret = sum(num_list[1:])
        ret += num_list[0]
        return ret

if __name__ == "__main__":
    ret = sum([1, 2, 3, 4, 5])
    print(ret)