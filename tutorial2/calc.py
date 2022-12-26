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

def main():
    pass

if __name__ == "__main__":
    main()
