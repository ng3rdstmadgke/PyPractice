#!/usr/bin/env python

def zodiac(year):
    kan_list =["庚","辛","壬","癸","甲","乙","丙","丁","戊","己"]
    shi_list = ["申","酉","戌","亥","子","丑","寅","卯","辰","巳","午","未"]
    ret = kan_list[year%10] + shi_list[year%12]
    return ret
if __name__ == "__main__":
    ret = zodiac(2005)
    print(ret)