#!/usr/bin/env python
from fractions import Fraction
import pprint

class SimultaneousEqutions(object):
    def __init__(self, matrix):
        validate_matrix = self.__validation(matrix)
        self.matrix = self.__mkmatrix(validate_matrix)

    @staticmethod
    def __mkmatrix(seq):
        ret = []
        for i in seq:
            elem = [Fraction(str(j)) for j in i]
            ret.append(elem)
        return ret

    @staticmethod
    def __validation(seq):
        for i in range(len(seq)):
            if seq[i][i] == 0:
                for j in range(i, len(seq)):
                    if seq[j][i] != 0:
                        seq[i:i] = [seq[j]]
                        del seq[j+1]
                        break
                else:
                    raise Exception("matrix is invalid")
        return seq

    @staticmethod
    def __subtraction(k, i):
        ret = []
        for kk, ii in zip(k, i):
            ret.append(kk - ii)
        return ret

    def simultaneous_equations(self):
        # 基準行の基準変数(i列)の係数が1となるような数で、基準行の係数を割る
        for i in range(len(self.matrix)):
            i_rate = self.matrix[i][i]
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] / i_rate

        # 基準行よりも上の行を基準行で引く
        # 基準行の係数を引く対象の行の係数に合わせる
            for k in range(i):
                k_rate = self.matrix[k][i] # 引く対象の行の基準列の係数
                tmp = []
                for l in range(len(self.matrix[k])):
                    tmp.append(self.matrix[i][l] * k_rate)
                self.matrix[k] = self.__subtraction(self.matrix[k], tmp)

        # 基準行よりも下の行を基準行で引く
        # 引く対象の行の係数を基準業の係数似合わせる
            for k in range(i+1, len(self.matrix)):
                k_rate = self.matrix[k][i]
                for l in range(len(self.matrix[k])):
                    self.matrix[k][l] = self.matrix[k][l] / k_rate
                self.matrix[k] = self.__subtraction(self.matrix[k], self.matrix[i])
        return self.matrix

if __name__ == "__main__":
    matrix = [[4,1,1,9],[1,3,1,10],[2,1,5,19]]
    ins = SimultaneousEqutions(matrix)
    print(ins.simultaneous_equations())

