# [BOJ] 덱 / STK / 20

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# size: 덱에 들어있는 정수의 개수를 출력한다.

# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys 
from collections import deque
n = int(input())  # 첫 줄에서 명령어 갯수를 입력 받음
a = [sys.stdin.readline().rstrip() for i in range(n)] # n줄 입력 
Q = deque()

def command(c):
    if c.startswith('push_front'):
        tmp = c.split()
        Q.appendleft(tmp[1])
    elif c.startswith('push_back'):
        tmp = c.split()
        Q.append(tmp[1])
    elif c == 'size':
        print(len(Q))
        
    if Q: # if Q is not empty
        if c == 'pop_front':
            print(Q.popleft())
        elif c == 'pop_back':
            print(Q.pop())
        elif c == 'empty':
            print(0)
        elif c == 'front':
            print(Q[0])
        elif c == 'back':
            print(Q[-1])
    else: # empty
        if c in ['pop_front', 'pop_back', 'front', 'back']:
            print(-1)
        elif c == 'empty':
            print(1)

for commandline in a:
    command(commandline)