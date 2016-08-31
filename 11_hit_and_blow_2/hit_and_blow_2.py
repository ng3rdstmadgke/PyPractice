#!/usr/bin/env python
import random

def generate_random_number(digit):
    digit -= 1
    num_list = list(range(0,10))
    while True:
        random_number = []
        digit_1 = random.choice(num_list[1:])
        random_number.append(str(digit_1))
        num_list.remove(digit_1)
        for i in range(digit):
            digit_x = random.choice(num_list)
            random_number.append(str(digit_x))
            num_list.remove(digit_x)
        return random_number

def user_number(digit):
    while True:
        try:
            user_input = input("Input Number : ")
            int(user_input)
            if len(user_input) == digit:
                return list(user_input)
            else:
                raise Exception
        except Exception as e:
            print("Invalid Value !")

def judge(hit_num, user_num):
    blow = 0
    hit = 0
    for cnt, i in enumerate(user_num):
        if i in hit_num:
            blow += 1
        if i == hit_num[cnt]:
            blow -= 1
            hit += 1
    if hit == 4:
        return "end"
    else:
        ret = "{}hit {}blow".format(str(hit), str(blow))
        return ret

def hit_and_blow(digit):
    hit_num = generate_random_number(digit)
    while True:
        user_num = user_number(digit)
        ret = judge(hit_num, user_num)
        if ret == "end":
            print("HIT!!!!")
            exit()
        else:
            print(ret)


if __name__ == "__main__":
    hit_and_blow(4)