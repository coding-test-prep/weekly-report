# [BOJ] 약수 / IMP / 10
import sys  
a = sys.stdin.readlines()

nums = list(map(int, a[1].split()))
answer = min(nums) * max(nums)
print(answer)