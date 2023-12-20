import itertools
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True

def solution(nums):
    l = []
    combi = [sum(x) for x in list(itertools.combinations(nums, 3))]
    for c in combi:
        l.append(is_prime(c))
        
    answer = sum(l)
    
    return answer