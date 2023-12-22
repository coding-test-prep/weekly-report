# [BOJ] 별 찍기-7 / IMP / 2
n = int(input())

for i in range(1, n):
    print(" " * (n-i) + "*" * (i + (i-1)))
for i in reversed(range(1, n+1)):
    print(" " * (n-i) + "*" * (i + (i-1)))