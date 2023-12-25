# [BOJ] 괄호 / STK / 35

import sys 
from collections import deque
n = int(input())  # 첫 줄에서 명령어 갯수를 입력 받음
a = [sys.stdin.readline().rstrip() for i in range(n)] # n줄 입력 

def search(x):
    stack = []
    for item in x:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if not stack or stack[-1] != '(':
                print('NO')
                return
            else:
                stack.pop()
    if not stack:
        print('YES')
    else:
        print('NO')

   
for x in a:
    search(x)