#!/usr/bin/env python

def convert_days(md):
    calendar = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    month = int(md.split("/")[0])
    day = int(md.split("/")[1])
    ret = 0
    for i in range(month-1):
        ret += calendar[i]
    ret += day
    return ret

def constellation(days):
    ret = ""
    if 358 <= days <= 366 or 1 <= days <= 20:
        ret = "Capricorn"
    elif 21 <= days <= 50:
        ret = "Aquarius"
    elif 51 <= days <= 80:
        ret = "Pisces"
    elif 81 <= days <= 111:
        ret = "Aries"
    elif 112 <= days <= 141:
        ret = "Taurus"
    elif 142 <= days <= 173:
        ret = "Gemini"
    elif 174 <= days <= 205:
        ret = "Cancer"
    elif 206 <= days <= 236:
        ret = "Leo"
    elif 237 <= days <= 267:
        ret = "Virgo"
    elif 268 <= days <= 297:
        ret = "Libra"
    elif 298 <= days <= 327:
        ret = "Scorpio"
    elif 328 <= days <= 357:
        ret = "Sagittarius"
    return ret

if __name__ == "__main__":
    days = convert_days("3/21")
    ret = constellation(days)
    print(ret)