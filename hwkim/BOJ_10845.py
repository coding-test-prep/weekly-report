# [BOJ] 큐 / STK / 15

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys 
from collections import deque
n = int(input())  # 첫 줄에서 명령어 갯수를 입력 받음
a = [sys.stdin.readline().rstrip() for i in range(n)] # n줄 입력 
Q = deque()

def command(c):
    if c == 'pop':
        if len(Q) > 0:
            print(Q.popleft())
        else:
            print(-1)
    elif c == 'size':
        print(len(Q))
    elif c == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif c == 'front':
        if len(Q) > 0:
            print(Q[0])
        else:
            print(-1)
    elif c == 'back':
        if len(Q) > 0:
            print(Q[-1])
        else:
            print(-1)
    elif c.startswith('push'):
        tmp = c.split()
        Q.append(tmp[1])
        

for commandline in a:
    command(commandline)
    