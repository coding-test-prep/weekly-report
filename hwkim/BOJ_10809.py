# [BOJ] 알파벳 찾기 / IMP / 5
import string
answer = ''
S = input()
alphabets = list(string.ascii_lowercase)
for alphabet in alphabets:
    if alphabet in S:
        ind = str(S.index(alphabet)) + ' '
        answer += ind
    else:
        answer += '-1 '
        
print(answer)
        
