n = [int(input()) for _ in range(7)]

odds = [num for num in n if num % 2 != 0]

if not odds:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))