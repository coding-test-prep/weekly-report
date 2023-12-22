# [BOJ] 카이사르 암호/ IMP / 8

codestr = str(input())
test_ord =[]
for i in codestr:
    test_ord.append(ord(i)-3)

answer =''
for i in test_ord:
    answer += chr(i)

print(answer)
