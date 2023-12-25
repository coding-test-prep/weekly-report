# [BOJ] 단어 뒤집기 / STR / 7

import sys 
n = int(input())  # 첫 줄에서 명령어 갯수를 입력 받음
a = [sys.stdin.readline().rstrip() for i in range(n)] # n줄 입력 

def flip(x):
    return x[::-1]

for sentence in a:
    slist = sentence.split()
    tmp = ''
    for word in slist:
        tmp += flip(word) + ' '
    print(tmp)