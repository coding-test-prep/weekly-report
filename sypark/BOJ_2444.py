n = int(input())

for i in range(1, n):
    print(" " * (n - i) + "*" * (i + (i - 1)))
for i in range(1, n + 1):
    print(" " * (i - 1) + "*" * ((n * 2) - (i + (i - 1))))