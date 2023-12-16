# [BOJ] 최댓값 / IMP / 2
import sys  
a = [int(sys.stdin.readline()) for i in range(9)] # 9줄 입력 => 최댓값 \n 최댓값의 index

print(max(a))
print(a.index(max(a)) + 1)