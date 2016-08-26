#!/usr/bin/env python
import random


def hit_and_blow(num):
    hit_num = random.choice(list(range(num)))
    while True:
        user_num = input_num()
        if user_num < hit_num:
            print("小さすぎます")
        elif user_num > hit_num:
            print("大きすぎます")
        else:
            break
    print("正解です！")

def input_num():
    while True:
        user_input = input("Input Number ! : ")
        try:
            user_num = int(user_input)
            return user_num
        except Exception as e:
            pass
    return user_input

if __name__ == "__main__":
    hit_and_blow(1000)
