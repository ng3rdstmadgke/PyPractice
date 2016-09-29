#!/usr/bin/env python

def palindrome(text):
    length = len(text)
    cost = 0
    cost_list = []
    text_list = list(text)
    if length % 2 == 1 and text[len(text)//2] == "*":
        text_list[len(text)//2] = "N"
        cost_list.append("N")
    for i in range(len(text) // 2):
        if text[i] != text[-(i+1)]:
            if text[i] != "*" and text[-(i+1)] != "*":
                return text, -1
            elif text[i] == "*":
                text_list[i] = text[-(i+1)]
                cost_list.append(text[-(i+1)])
            elif text[-(i+1)] == "*":
                text_list[-(i+1)] = text[i]
                cost_list.append(text[i])
        elif text[i] == "*" and text[-(i+1)] == "*":
            text_list[i] = "N"
            text_list[-(i+1)] = "N"
            cost_list.extend(["N", "N"])
    cost += cost_list.count("N") * 10
    cost += cost_list.count("O") * 15
    return "".join(text_list), cost

if __name__ == "__main__":
    input_list = ["NOO*", "NO*N", "NO", "O*O", "***", "*O*O*", "NOO*O"]
    for i in input_list:
        ret = palindrome(i)
        print(ret)