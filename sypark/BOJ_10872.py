n = int(input())

def factorial(n: int):
    return n * factorial(n - 1) if n > 1 else 1

print(factorial(n))