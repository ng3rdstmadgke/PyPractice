#!/usr/bin/env python3

def search_leap_year(year):
    if year % 400 == 0:
        message = "{}年はうるう年です".format(year)
    elif year % 100 == 0:
        message = "{}年はうるう年ではありません".format(year)
    elif year % 4 == 0:
        message = "{}年はうるう年です".format(year)
    else:
        message = "{}年はうるう年ではありません".format(year)
    return message

if __name__ == "__main__":
    for i in [0, 1, 16, 200, 400, 800, 1500, 1600, 342]:
        print(search_leap_year(i))