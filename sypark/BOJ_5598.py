import string

char = str(input())

a = string.ascii_uppercase

print(char.translate(str.maketrans(a[3:] + a[:3], a)))