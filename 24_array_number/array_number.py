#!/usr/bin/env python

def array_number(array):
    sorted_list = []
    for cnt_i, i in enumerate(array):
        for cnt_j, j in enumerate(sorted_list):
            if i >= j[0]:
                sorted_list[cnt_j:cnt_j] = [(i, cnt_i)]
                break
        else:
            sorted_list.append((i, cnt_i))
    return sorted_list[:3]


if __name__ == "__main__":
    array = [12, 6, 8, 3, 10, 1, 0, 9]
    ret = array_number(array)
    for i in ret:
        print(i[1], "->", i[0])