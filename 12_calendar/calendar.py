#!/usr/bin/env python

class Calendar(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        self.days_leap_year = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def print_calendar(self):
        flg, week_days = self._days_cnt()
        if flg is True:
            calendar_list = ["" for i in range(week_days)] + [str(i) for i in range(1, self.days_leap_year[self.month] + 1)]
        else:
            calendar_list = ["" for i in range(week_days)] + [str(i) for i in range(1, self.days[self.month] + 1)]
        print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
        for cnt, i in enumerate(calendar_list):
            print(i, end="\t")
            if (cnt + 1) % 7 == 0:
                print("")

    def _days_cnt(self):
        # 西暦１年の１月１日の曜日
        cnt = 6
        flg = False
        for i in range(1, self.year):
            if i <= 1582 and i % 4 == 0:
                cnt += 366
            elif i > 1582 and (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
                cnt += 366
            else:
                cnt += 365
        if self.year <= 1582 and self.year % 4 == 0:
            cnt += sum(self.days_leap_year[:self.month])
            week_day = cnt % 7
            flg = True
        elif self.year > 1582 and (self.year % 4 == 0) and (self.year % 100 != 0) or (self.year % 400 == 0):
            cnt += sum(self.days_leap_year[:self.month])
            week_day = cnt % 7
            flg = True
        else:
            cnt += sum(self.days[:self.month])
            week_day = cnt % 7
        return (flg, week_day)

if __name__ == "__main__":
    ins = Calendar(2000, 2)
    ins.print_calendar()