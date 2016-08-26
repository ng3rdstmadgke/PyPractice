#!/usr/bin/env python3
import csv

def read_matrix_file(file):
    with open(file, "rt") as f:
        csvin = csv.reader(f)
        matrix = [i for i in csvin]
    return matrix

def validate_matrix(matrix):
    colmun_num = len(matrix[0])
    colmun_set = set([colmun_num])
    for i in matrix[1:]:
        colmun_set = colmun_set | set([len(i)])
    if len(colmun_set) == 1:
        return True
    else:
        return False

def transpose(matrix):
    column = len(matrix[0])
    transposed_matrix = []
    for i in range(column):
        transposed_matrix.append([])
    for i in matrix:
        for n, j  in enumerate(i):
            transposed_matrix[n].append(j)
    return transposed_matrix

if __name__ == "__main__":
    file = "matrix.txt"
    matrix = read_matrix_file(file)
    if validate_matrix(matrix) is False:
        print("invalid matrix !!")
    else:
        ret = transpose(matrix)
        for i in ret:
            for j in i:
                print(j, end=" ")
            print("")