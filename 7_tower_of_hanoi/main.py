#!/usr/bin/env python3


def tower_of_hanoi(num, start="左", work="中", end="右", message=""):
    if num == 1:
        return "1を{}から{}へ,".format(start, end)
    tower_num = num - 1
    ret = tower_of_hanoi(tower_num, start, end, work)
    message += ret
    message += "{}を{}から{}へ,".format(num, start, end)
    ret = tower_of_hanoi(tower_num, work, start, end)
    message += ret
    return message


if __name__ == "__main__":
    ret = tower_of_hanoi(3)
    for i in ret.split(","):
        print(i)