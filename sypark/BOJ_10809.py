import string

x = [i for i in str(input())]

alphabet = string.ascii_lowercase

print(*[x.index(a) if a in x else -1 for a in alphabet])