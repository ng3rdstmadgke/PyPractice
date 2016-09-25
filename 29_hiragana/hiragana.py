#!/usr/bin/env python
import random
import os
def hiragana(chars_num, hiragana_list):
    cat_name = ""
    for i in range(chars_num):
        cat_name += random.choice(hiragana_list)
    return cat_name

if __name__ == "__main__":
    cwd = os.path.dirname(os.path.abspath(__name__))
    with open(cwd + "/hiragana.txt", "rt") as f:
        text = f.read()
    h_list = list(text.replace("\n", ""))
    ret = hiragana(2, h_list)
    print(ret)