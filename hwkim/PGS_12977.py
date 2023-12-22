# [PGS] 소수 만들기 / IMP / 25
# input = list of nums, nC3 
import itertools
import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True

def solution(nums):
    nums = [1,2,3,4]
    nCr = list(itertools.combinations(nums, 3)) # r = 3
    result = [sum(t) for t in nCr]
    answer = 0
    for i in result:
        if is_prime_number(i):
            answer += 1

    return(answer)