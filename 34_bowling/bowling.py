#!/usr/bin/env python

def gen_score_sheet(pins_list):
    score_sheet = []
    cnt = 0
    for i in range(10):
        if i < 9:  # 1-9投目
            if pins_list[cnt] == 10:  # ストライクの時
                score_sheet.append((10, 0))
                cnt += 1
            else:
                score_sheet.append((pins_list[cnt], pins_list[cnt+1]))
                cnt += 2
        else:  # 10投目
            score_sheet.append(tuple(pins_list[cnt:]))
    return score_sheet

def calc_score(score_sheet):
    score_list = []
    score = 0
    for cnt_i, i in enumerate(score_sheet):
        if cnt_i < 9 and i[0] == 10:  # 1-9投目かつストライクのとき
            if cnt_i < 8 and score_sheet[cnt_i+1][0] == 10: # 1-8投目で次もストライクのとき
                score += (i[0] + score_sheet[cnt_i+1][0] + score_sheet[cnt_i+2][0])
            else:  # 9投目または、1-8投目で次がストライク以外の時
                score += (i[0] + score_sheet[cnt_i+1][0] + score_sheet[cnt_i+1][1])
        elif cnt_i < 9 and i[0] + i[1] == 10: # 1-9投目かつスペアのとき
            score += (sum(i) + score_sheet[cnt_i+1][0])
        else:  # 10投目または、1-9投目でストライクとスペア以外の時
            score += sum(i)
        score_list.append(score)
    return score_list

if __name__ == "__main__":
    pins_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pins_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
    pins_list = [6, 2, 0, 3, 5, 5, 0, 8, 10, 1, 9, 3, 6, 6, 4, 10, 5, 5, 3]
    # [8, 11, 21, 29, 49, 62, 71, 91, 111, 124]
    pins_list = [1, 9, 1, 9, 1, 9, 1, 0, 1, 9, 1, 9, 1, 9, 0, 1, 1, 9, 1, 9, 4]
    # [11, 22, 33, 34, 45, 56, 66, 67, 78, 92]
    pins_list = [1, 9, 2, 8, 3, 7, 4, 6, 10, 0, 0, 6, 4, 7, 3, 8, 2, 9, 1, 2]
    # [12, 25, 39, 59, 69, 69, 86, 104, 123, 135]
    pins_list = [1, 9, 2, 8, 3, 7, 4, 6, 10, 10, 6, 4, 7, 3, 8, 2, 9, 1, 2]
    # [12, 25, 39, 59, 85, 105, 122, 140, 159, 171]
    score_sheet = gen_score_sheet(pins_list)
    ret = calc_score(score_sheet)
    print(ret)