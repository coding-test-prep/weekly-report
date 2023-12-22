# [BOJ] 평균 / IMP / 15
import sys  
# first line = num of subjects, second line = list of scores
n = int(input())  
scores = list(map(int, sys.stdin.readline().split()))
max_score = max(scores)

def new_score(old_score):
    new = old_score/max_score * 100
    return new

new_sum = 0
for i in scores:
    tmp = new_score(i)
    new_sum += tmp

print(new_sum/n)    