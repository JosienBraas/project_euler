# Project Euler
# 3 - Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

number = 600851475143
factor = 1

while factor < (number/2):
    if number%factor == 0:
        bigdiv = number/factor
        if isprime(bigdiv):
            print 'This number is a divisor and also a prime: ', str(bigdiv)
            break
    factor = factor+2

print '-----\nFinished!'