from statistics import mean

n = int(input())
grades = [int(x) for x in input().split(" ", n)]

new = [g / max(grades) * 100 for g in grades]

print(mean(new))