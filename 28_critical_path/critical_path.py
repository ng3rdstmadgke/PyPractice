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
        for node_i in range(1, self.nodes_num):
            node = self.alphabet_list[node_i]
            node_time_list = []
            for diagram_i in self.diagram:
                if diagram_i[1] == node:
                    src_node = self.alphabet_list.index(diagram_i[0])
                    src_node_time = self.nodes_status[src_node][1]
                    node_time = src_node_time + diagram_i[2]
                    node_time_list.append(node_time)
            self.nodes_status[node_i][1] = max(node_time_list)

    def __latest_node_time(self):
        self.nodes_status[-1][2] = self.nodes_status[-1][1]
        for node_i in range(self.nodes_num - 1)[::-1]:
            node = self.alphabet_list[node_i]
            node_time_list = []
            for diagram_i in self.diagram:
                if diagram_i[0] == node:
                    src_node = self.alphabet_list.index(diagram_i[1])
                    src_node_time = self.nodes_status[src_node][2]
                    node_time = src_node_time - diagram_i[2]
                    node_time_list.append(node_time)
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
    nodes = 7
    works = 9
    diagram = [['A', 'B', 10], ['A', 'C', 3], ['B', 'D', 4], ['B', 'E', 7], ['C', 'D', 7], ['C', 'F', 9], ['D', 'E', 2], ['E', 'G', 1], ['F', 'G', 7]]
    ins = CriticalPath(nodes, works, diagram)
    ret = ins.critical_path()
    p = " -> ".join(ret[1:])
    print(p)
    print("cost : ", ret[0])