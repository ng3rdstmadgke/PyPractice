#!/usr/bin/env python

def sum(l):
    if len(l) == 0:
        return 0
    else:
        ret = sum(l[1:])
        ret += l[0]
        return ret

def length(l):
    if len(l) == 0:
        return 0
    else:
        ret = length(l[1:])
        ret += 1
        return ret

def max(l):
    if len(l) == 1:
        return l[0]
    else:
        ret = max(l[1:])
        if l[0] > ret:
            ret = l[0]
        return ret

def min(l):
    if len(l) == 1:
        return l[0]
    else:
        ret = min(l[1:])
        if l[0] < ret:
            ret = l[0]
        return ret

def forall(l):
    if len(l) == 0:
        return True
    else:
        ret = forall(l[1:])
        if l[0] % 2 != 0:
            ret = False
        return ret

def exists(l):
    if len(l) == 0:
        return False
    else:
        ret = exists(l[1:])
        if l[0] % 2 != 0:
            ret = True
        return ret

def find(l):
    if len(l) == 0:
        return None
    else:
        ret = find(l[1:])
        if l[0] % 2 == 0 and l[0] != 0:
            ret = l[0]
        return ret



if __name__ == "__main__":
    print("sum : ", sum([1, 2, 3, 4, 5]))
    print("length : ", length([1,2,3,4,5,6,7,8,9]))
    print("max : ", max([1, 0, 6, 10, 3, 3]))
    print("min : ", min([1, 0, 6, 10, 3, 3]))
    print("forall : ", forall([2,4,6,8]), forall([1,2,4,6]))
    print("exists : ", exists([2,4,6,8]), exists([1,2,4,6]))
    print("find : ", find([0,5,6,7,1,2,3,4,8,9]))
