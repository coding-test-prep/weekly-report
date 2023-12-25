# [BOJ] 요세푸스 문제 / STK / 10
from collections import deque
nums = list(map(int, input().split())) # e.g. [7, 3]
Q = deque(list(range(1, nums[0]+1)))
output = '<'
r = -(nums[1]-1)

while Q:
    Q.rotate(r)
    output += str(Q.popleft()) + ', '
output = output.rstrip(', ') + '>'

print(output)

