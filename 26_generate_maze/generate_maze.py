#!/usr/bin/env python
import random
class GenerateMaze(object):
    def __init__(self, line, column):
        self.maze = []
        for i in range(line):
            self.maze.append(["#" for j in range(column)])
        self.line = line
        self.column = column
        self.current = (-1, -1)

    def __define_start(self):
        l = [i for i in range(self.column) if i % 2 != 0 and i != self.column - 1]
        n = random.choice(l)
        self.current = (1, n)
        self.maze[1][n] = " "

    def __search_branch_point(self):
        ret = []
        for i in range(self.line):
            for j in range(self.column):
                if self.maze[i][j] == " ":
                    ret.append((i, j))
        random.shuffle(ret)
        return ret

    def __search_way(self, point):
        """
        :param : (line, column)
        :return: (line, column)
        """
        branch = []
        # 上
        if point[0] > 1 \
                and self.maze[point[0] - 2][point[1]] == "#" \
                and self.maze[point[0] - 1][point[1]] == "#" \
                and self.maze[point[0] - 1][point[1] + 1] == "#" \
                and self.maze[point[0] - 1][point[1] - 1] == "#":
            branch.append((point[0] - 1, point[1]))
        # 下
        if point[0] < self.line - 2 \
                and self.maze[point[0] + 2][point[1]] == "#" \
                and self.maze[point[0] + 1][point[1]] == "#" \
                and self.maze[point[0] + 1][point[1] + 1] == "#" \
                and self.maze[point[0] + 1][point[1] - 1] == "#":
            branch.append((point[0] + 1, point[1]))
        # 右
        if point[1] < self.column - 2 \
                and self.maze[point[0]][point[1] + 2] == "#" \
                and self.maze[point[0]][point[1] + 1] == "#" \
                and self.maze[point[0] + 1][point[1] + 1] == "#" \
                and self.maze[point[0] - 1][point[1] + 1] == "#" :
            branch.append((point[0], point[1] + 1))
        # 左
        if point[1] > 1 \
                and self.maze[point[0]][point[1] - 2] == "#" \
                and self.maze[point[0]][point[1] - 1] == "#" \
                and self.maze[point[0] + 1][point[1] - 1] == "#" \
                and self.maze[point[0] - 1][point[1] - 1] == "#" :
            branch.append((point[0], point[1] - 1))

        if branch:
            way = random.choice(branch)
            self.current = way
        else:
            way = None
        return way

    def generate_maze(self):
        self.__define_start()
        while True:
            way = self.__search_way(self.current)
            if way:
                self.maze[way[0]][way[1]] = " "
            else:
                point_list = self.__search_branch_point()
                for i in point_list:
                    way = self.__search_way(i)
                    if way:
                        self.maze[way[0]][way[1]] = " "
                        break
                else:
                    break

if __name__ == "__main__":
    ins = GenerateMaze(10, 20)
    ins.generate_maze()
    for i in ins.maze:
        print("".join(i))