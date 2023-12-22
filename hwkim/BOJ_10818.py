# [BOJ] 최소, 최대 / IMP / 2
import sys  
n = int(input())  
nums = list(map(int, sys.stdin.readline().split()))

print(min(nums), max(nums))