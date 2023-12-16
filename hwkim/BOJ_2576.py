# [BOJ] 홀수 / IMP / 8
import sys  
a = [int(sys.stdin.readline()) for i in range(7)] # a = [12, 77, 38,...]

odd = []
for i in a:
    if i % 2 != 0: # odd
        odd.append(i)
    else:
        pass

if len(odd)>0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)