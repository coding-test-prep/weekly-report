x = int(input())
n = [int(x) for x in input().split(" ", x)]

a = max(n) * min(n)

if any(a % i != 0 for i in n):
    pass
else:
    print(a)
