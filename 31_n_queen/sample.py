#!/usr/bin/env python
# 単純再帰

def check(q_list):
    # x, yは調査対象の"Q"の座標(x, y)
    for y in range(len(q_list)):
        x = q_list[y]
        # post_x, post_yはx, y以降の"Q"の座標(post_x, post_y)
        for post_y in range(y + 1, len(q_list)):
            post_x = q_list[post_y]
            # Qとpost_Qのx座標が同一の場合、Qとpost_Qのなす傾き(yの増加量/xの増加量)が1 or -1の場合はFalse
            if (post_x == x) or abs(post_x - x) == post_y - y:
                return False
    return True

def n_queen(q_list, ret=[], cnt=0):
    if cnt == len(q_list):
        if check(q_list):
            ret.append(q_list.copy())
    else:
        for i in range(len(q_list)):
            q_list[cnt] = i
            n_queen(q_list, cnt=cnt+1)
    return ret

if __name__ == "__main__":
    n = 8
    sample = [0 for _ in range(n)]
    ret = n_queen(sample)

    # 整形して表示
    for i in ret:
        for j in i:
            line = ["■" for _ in range(n)]
            line[j] = "Q"
            text = " ".join(line)
            print(text)
        print("")
    print(len(ret))