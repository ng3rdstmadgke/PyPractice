#!/usr/bin/env python

# 1 : sum
def sum(l):
    if len(l) == 0:
        return 0
    else:
        ret = sum(l[1:])
        ret += l[0]
        return ret

# 2 : length
def length(l):
    if len(l) == 0:
        return 0
    else:
        ret = length(l[1:])
        ret += 1
        return ret

# 3 : max
def max(l):
    if len(l) == 1:
        return l[0]
    else:
        ret = max(l[1:])
        if l[0] > ret:
            ret = l[0]
        return ret

# 4 : min
def min(l):
    if len(l) == 1:
        return l[0]
    else:
        ret = min(l[1:])
        if l[0] < ret:
            ret = l[0]
        return ret

# 5 : forall
def forall(l):
    if len(l) == 0:
        return True
    else:
        ret = forall(l[1:])
        if l[0] % 2 != 0:
            ret = False
        return ret

# 6 : exists
def exists(l):
    if len(l) == 0:
        return False
    else:
        ret = exists(l[1:])
        if l[0] % 2 != 0:
            ret = True
        return ret

# 7 : find
def find(l):
    if len(l) == 0:
        return None
    else:
        ret = find(l[1:])
        if l[0] % 2 == 0 and l[0] != 0:
            ret = l[0]
        return ret

# 8 : skip
def skip(l, n):
    if len(l) == 0:
        return []
    else:
        ret = skip(l[1:], n)
        if len(ret) < n:
            ret[0:0] = [l[0]]
        return ret

# 9 : take
def take(l, n, cnt=1):
    if cnt == n:
        return [l[0]]
    else:
        ret = take(l[1:], n, cnt+1)
        ret[0:0] = [l[0]]
        return ret

# 10 : map
def map(l):
    if len(l) == 0:
        return []
    else:
        ret = map(l[1:])
        ret[0:0] = [str(l[0]*2)]
        return ret

# 11 : filter
def mod(n, m):
    if n % m == 0:
        return True
    else:
        return False

def filter(l, func):
    if len(l) == 0:
        return []
    else:
        ret = filter(l[1:], func)
        if func(l[0], 3):
            ret[0:0] = [l[0]]
        return ret

# 12 : partition
def partition(l, func, cnt=0):
    if len(l) == 0:
        t_list = []
        f_list = []
        return t_list, f_list
    else:
        t, f = partition(l[1:], func, cnt+1)
        if func(l[0], 3):
            t[0:0] = [l[0]]
        else:
            f[0:0] = [l[0]]
        if cnt == 0:
            return [tuple(t), tuple(f)]
        else:
            return t, f


if __name__ == "__main__":
    print("sum : ", sum([1, 2, 3, 4, 5]))
    print("length : ", length([1,2,3,4,5,6,7,8,9]))
    print("max : ", max([1, 0, 6, 10, 3, 3]))
    print("min : ", min([1, 0, 6, 10, 3, 3]))
    print("forall : ", forall([2,4,6,8]), forall([1,2,4,6]))
    print("exists : ", exists([2,4,6,8]), exists([1,2,4,6]))
    print("find : ", find([0,5,6,7,1,2,3,4,8,9]))
    print("skip : ", skip([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
    print("take : ", take([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
    print("map : ", map([1, 2, 3, 4, 5]))
    print("filter : ", filter([1, 2, 3, 4, 5, 6, 7, 8, 9], mod))
    print("partition : ", partition([1, 2, 3, 4, 5, 6, 7, 8, 9], mod))

