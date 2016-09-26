#!/usr/bin/env python
import os
# バックトラッキング

def check(q_map, cnt):
    if cnt >= 1:
        # チェック対象の"Q"の座標(x, y)
        x = q_map[cnt-1]
        y = cnt-1
        for i in range(cnt-1):
            # pre_x, pre_yはx, y以前のQの座標(pre_x, pre_y)
            pre_x = q_map[i]
            pre_y = i
            # Qとpre_Qのx座標が同一の場合、Qとpre_Qのなす傾き(yの増加量/xの増加量)が1 or -1の場合はFalse
            if pre_x == x or y - pre_y == abs(x - pre_x):
                return False
        return True
    else:
        return True

def n_queen(q_map, cnt=0, ret=[]):
    # cnt-1の時に配置した"Q"がそれより以前においた"Q"の進行方向に配置されていないか確認。
    # 他の"Q"の進行方向上に配置されていたら以降の再帰を中止する。
    if check(q_map, cnt) is False:
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

def set_default(file_name):
    ret = []
    file_path = os.path.dirname(os.path.abspath(__name__)) + "/" + file_name
    with open(file_path, "rt") as f:
        text = f.read()
    chessboard = text.split("\n")
    for line, i in enumerate(chessboard):
        try:
            column = i.index("Q")
        except ValueError:
            pass
        else:
            ret.append((line, column))
    return ret

if __name__ == "__main__":
    # n Queenの全パターンを取得する
    n = 7
    sample = [0 for _ in range(n)]
    ret = n_queen(sample)

    # デフォルトの入力を読み取り、"Q"の座標(line, column)をタプルのリストで取得する
    default_q = set_default("input.txt")

    # 取得したリストを元に該当するパターンを抽出
    print_list = []
    for i in ret:
        for line, column in default_q:
            if i[line] != column:
                break
        else:
            print_list.append(i)
    # 整形して表示
    for i in print_list:
        for j in i:
            line = ["■" for _ in range(n)]
            line[j] = "Q"
            text = " ".join(line)
            print(text)
        print("")


