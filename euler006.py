# Project Euler
# 6 - Sum square difference

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumsquares(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i * i)
    return sum

def squaresum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return (sum * sum)

def diff(n):
    return squaresum(n) - sumsquares(n)

print diff(10)
print diff(100)
