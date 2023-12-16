# [BOJ] 별 찍기-6 / IMP / 2
n = int(input())

for i in reversed(range(1, n+1)):
    print(" " * (n-i) + "*" * (i + (i-1)))