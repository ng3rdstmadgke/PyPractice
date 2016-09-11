#/usr/bin/env python

class Maze(object):
    def __init__(self, maze):
        self.maze = maze
        self.branch = []
        self.cp = (-1, -1)
        self.end = (-1, -1)

    def __search_start_point(self):
        """
        スタート地点の座標を算出する.
        """
        for cnt, i in enumerate(self.maze[0]):
            if i == " ":
                self.cp = (0, cnt)
                break

    def __search_end_point(self):
        """
        ゴールの座標を算出する
        """
        for cnt, i in enumerate(self.maze[-1]):
            if i == " ":
                self.end = (len(self.maze)-1, cnt)

    def __calculate_cost(self, current_point):
        """
        引数にとった座標からゴールまでのコストを計算する。
        :param current_point:
        :return: ある座標からゴールまでのコスト(int)
        """
        cost_l = self.end[0] - current_point[0]
        cost_c = self.end[1] - current_point[1]
        cost = cost_l + cost_c
        return cost

    @staticmethod
    def __choose_way(ways_list):
        """
        与えられたリストから最もコストが低い座標を選択し、その座標を返す
        :param ways_list: [[(line, column), cost], ...]
        :return: way=(line, column), ways_list=[[(line, column), cost], ...]
        """
        ways_list = ways_list.copy()
        cost = None
        way = None
        counter = 0
        for cnt, i in enumerate(ways_list):
            if cost is None or i[1] < cost:
                way = i[0]
                counter = cnt
        if way is not None:
            del ways_list[counter]
        return way, ways_list

    def __search_ways(self):
        """
        現在地からすすめる座標を探索し、最良の座標を返す。
        選択しなかった座標はbranchに追加する。
        :return: (line, column)
        """
        tmp_ways = []
        # 右
        if self.maze[self.cp[0]][self.cp[1]+1] == " ":
            cost = self.__calculate_cost((self.cp[0], self.cp[1]+1))
            tmp_ways.append([(self.cp[0], self.cp[1]+1), cost])
        # 左
        if self.maze[self.cp[0]][self.cp[1]-1] == " ":
            cost = self.__calculate_cost((self.cp[0], self.cp[1]-1))
            tmp_ways.append([(self.cp[0], self.cp[1]-1), cost])
        # 上
        if self.cp[0] != 0 and self.maze[self.cp[0]-1][self.cp[1]] == " ":
            cost = self.__calculate_cost((self.cp[0]-1, self.cp[1]))
            tmp_ways.append([(self.cp[0]-1, self.cp[1]), cost])
        # 下
        if self.cp[0] < len(self.maze)-1 and self.maze[self.cp[0]+1][self.cp[1]] == " ":
            cost = self.__calculate_cost((self.cp[0]+1, self.cp[1]))
            tmp_ways.append([(self.cp[0]+1, self.cp[1]), cost])
        # 進む方向を探索する
        way, ways_list = self.__choose_way(tmp_ways)
        self.branch.extend(ways_list)
        return way

    def __search_branch(self):
        """
        分岐点を評価し、進む方向を返す。
        :return: (line, column)
        """
        way, ways_list = self.__choose_way(self.branch)
        self.branch = ways_list
        return way

    def __go_to(self, way):
        """
        移動先の座標を引数にとり、現在地座標を移動先座標に書き換えた後、迷路の当該座標を"+"に置換する。
        :param way: 移動先の座標(line, column)
        """
        self.cp = way
        self.maze[self.cp[0]][self.cp[1]] = "+"

    def exe_maze(self):
        self.__search_start_point()
        self.__go_to(self.cp)
        self.__search_end_point()
        while self.cp != self.end:
            way = self.__search_ways()
            if way is None:
                way = self.__search_branch()
            self.__go_to(way)

if __name__ == "__main__":
    import os
    cwd = os.path.dirname(os.path.abspath(__name__))
    file_name = cwd + "/maze.txt"
    with open(file_name, "rt") as f:
        ret = f.read()
        ret = ret.split("\n")
    for cnt,i in enumerate(ret):
        ret[cnt] = list(i)

    ins = Maze(ret)
    ins.exe_maze()
    for i in ins.maze:
        print("".join(i))

