def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def factorial(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

# not optimized
def binomial_coefficient(n, m):
    if m > n: return 0
    return factorial(n) / (factorial(n-m) * factorial(m))

def pow(x, n):
    assert n >= 0
    
    res = 1
    for i in range(n):
        res *= x
    return res

def gcd(a, b):
    if a < 0: a *= -1
    if b < 0: b *= -1

    if a == 0: return b
    if b == 0: return a

    while b > 0:
        temp = a
        a = b
        b = temp % b
    
    return a

def main():
    pass

if __name__ == "__main__":
    main()
