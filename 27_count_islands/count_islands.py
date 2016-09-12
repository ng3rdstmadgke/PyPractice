#!/usr/bin/env python

class CountIslands(object):
    def __init__(self, line, column, map):
        self.line = line
        self.column = column
        self.map = map
        self.island_cnt = 0
        self.coordinate_list = []

    def __search(self):
        for i in range(self.line):
            for j in range(self.column):
                if self.map[i][j] == "#":
                    self.coordinate_list.append((i, j))
                    self.island_cnt += 1
                    return True
        return False

    def __count(self):
        self.map[self.coordinate_list[0][0]][self.coordinate_list[0][1]] = "."
        for i in self.coordinate_list:
            # 上
            if i[0] > 0 and self.map[i[0] - 1][i[1]] == "#":
                self.coordinate_list.append((i[0] - 1, i[1]))
                self.map[i[0] - 1][i[1]] = "."
            # 下
            if i[0] < self.line - 1 and self.map[i[0] + 1][i[1]] == "#":
                self.coordinate_list.append((i[0] + 1, i[1]))
                self.map[i[0] + 1][i[1]] = "."
            # 右
            if i[1] < self.column - 1 and self.map[i[0]][i[1] + 1] == "#":
                self.coordinate_list.append((i[0], i[1] + 1))
                self.map[i[0]][i[1] + 1] = "."
            # 左
            if i[1] > 0 and self.map[i[0]][i[1] - 1] == "#":
                self.coordinate_list.append((i[0], i[1] - 1))
                self.map[i[0]][i[1] - 1] = "."

    def count_island(self):
        while True:
            ret = self.__search()
            if ret:
                self.__count()
                self.coordinate_list = []
            else:
                break

if __name__ == "__main__":
    import os
    cwd = os.path.dirname(os.path.abspath(__name__))
    with open(cwd + "/input.txt", "rt") as f:
        text = f.read()
    l = text.split("\n")
    map = []
    for i in l[1:]:
        map.append(list(i))
    line, column = l[0].split(" ")
    ins = CountIslands(int(line), int(column), map)
    ins.count_island()
    print(ins.island_cnt)
