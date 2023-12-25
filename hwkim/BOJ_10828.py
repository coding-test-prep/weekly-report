# [BOJ] 스택 / STK / 15

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 "출력"한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 "출력"한다.
# empty: 스택이 비어있으면 1, 아니면 0을 "출력"한다.
# top: 스택의 가장 위에 있는 정수를 "출력"한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys 
n = int(input())  # 첫 줄에서 명령어 갯수를 입력 받음
a = [sys.stdin.readline().rstrip() for i in range(n)] # n줄 입력 
stack = []

def command(c):
    if c == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif c.startswith('push'):
        tmp = c.split()
        stack.append(tmp[1])
        
for commandline in a:
    command(commandline)
    