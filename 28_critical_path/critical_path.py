#!/usr/bin/env python
import string

class CriticalPath(object):
    def __init__(self, nodes, works, diagram):
        self.nodes_num = nodes
        self.works_num = works
        self.diagram = diagram
        self.alphabet_list = tuple(string.ascii_uppercase)
        self.nodes_status = [[self.alphabet_list[i], 0, 0, 0] for i in range(self.nodes_num)]

    def __earliest_node_time(self):
        # 各ノードの最早結合点時刻を調べる
        for node_i in range(1, self.nodes_num):
            node = self.alphabet_list[node_i]
            node_time_list = []
            # "diagram"の行先ノードが"node"であったら、行先ノードの結合点時刻を算出する
            for diagram_i in self.diagram:
                if diagram_i[1] == node:
                    src_node_name = self.alphabet_list.index(diagram_i[0])
                    src_node_time = self.nodes_status[src_node_name][1]
                    node_time = src_node_time + diagram_i[2]
                    node_time_list.append(node_time)
            # もっとも大きい結合点時刻を最早結合点時刻としてnodes_statusに登録する
            self.nodes_status[node_i][1] = max(node_time_list)

    def __latest_node_time(self):
        # 最後のノードの最遅結合点時刻に最早結合点時刻を登録する
        self.nodes_status[-1][2] = self.nodes_status[-1][1]

        # 各ノードの最遅結合点時刻を調べる
        for node_i in range(self.nodes_num - 1)[::-1]:
            node = self.alphabet_list[node_i]
            node_time_list = []
            # "diagram"の出発ノードが"node"であったら、出発ノードの結合点時刻を算出する
            for diagram_i in self.diagram:
                if diagram_i[0] == node:
                    next_node_name = self.alphabet_list.index(diagram_i[1])
                    next_node_time = self.nodes_status[next_node_name][2]
                    node_time = next_node_time - diagram_i[2]
                    node_time_list.append(node_time)
            # もっとも小さい結合点時刻を最遅結合点時刻としてnodes_statusに登録する
            self.nodes_status[node_i][2] = min(node_time_list)

    def __margin(self):
        for cnt, i in enumerate(self.nodes_status):
            margin = i[2] - i[1]
            self.nodes_status[cnt][3] = margin

    def critical_path(self):
        """
        :return: [earliest_node_time, node(n), node(n+1), ...]
        """
        self.__earliest_node_time()
        self.__latest_node_time()
        self.__margin()
        cost = self.nodes_status[-1][1]
        critical_path = [cost]
        for i in self.nodes_status:
            if i[3] == 0:
                critical_path.append(i[0])
        return critical_path

if __name__ == "__main__":
    import os
    file = os.path.dirname(os.path.abspath(__name__)) + "/input.txt"
    with open(file, "rt") as f:
        data = f.read()
    input_list = data.split("\n")
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split(" ")
        if i == 0:
            input_list[i][0] = int(input_list[i][0])
            input_list[i][1] = int(input_list[i][1])
        else:
            input_list[i][2] = int(input_list[i][2])
    nodes = input_list[0][0]
    works = input_list[0][1]
    diagram = input_list[1:]
    ins = CriticalPath(nodes, works, diagram)
    ret = ins.critical_path()
    p = " -> ".join(ret[1:])
    print(p)
    print("cost : ", ret[0])