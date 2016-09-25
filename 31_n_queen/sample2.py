#!/usr/bin/env python
# バックトラッキングを用いて最適化

def check(q_map, cnt):
    if cnt >= 0:
        # チェック対象の"Q"の座標(x, y)
        x = q_map[cnt]
        y = cnt
        for i in range(cnt):
            # pre_x, pre_yはx, y以前のQの座標(pre_x, pre_y)
            pre_x = q_map[i]
            pre_y = i
            # Qとpre_Qのx座標が同一の場合、Qとpre_Qのなす傾き(yの増加量/xの増加量)が1 or -1の場合はFalse
            if pre_x == x or y - pre_y == abs(x - pre_x):
                return False
        return True

def n_queen(q_map, cnt=0, ret=[]):
    # cnt-1の"Q"がそれより以前に配置した"Q"の進行方向に配置されていないか確認。
    # 他の"Q"の進行方向上に配置されていたら以降の再帰を中止する。
    if check(q_map, cnt-1) is False:
        return None
    # 再帰が途中で中断せずに、最後の行まで"Q"を配置できたq_mapはretに追加する。
    if cnt == len(q_map):
        ret.append(q_map.copy())
        return None
    # 深さ優先探索で再帰的に"Q"を配置する。
    for i in range(len(q_map)):
        q_map[cnt] = i
        n_queen(q_map, cnt=cnt+1)
    return ret

if __name__ == "__main__":
    n = 7
    qm = ["None" for i in range(n)]
    ret = n_queen(qm)

    # 整形して表示
    for i in ret:
        for j in i:
            line = ["■" for _ in range(n)]
            line[j] = "Q"
            text = " ".join(line)
            print(text)
        print("")
    print(len(ret))
