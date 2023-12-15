# [BOJ] 별 찍기-5 / IMP / 10
n = int(input())

for i in range(1, n+1):
    print(" " * (n-i) + "*" * (i + (i-1)))