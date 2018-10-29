# Project Euler
# 5 - Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def testdiv(n):
    '''Check if a number is evenly divisible by all of the numbers from 1 to 20.'''
    if n % 11 == 0:
        if n % 12 == 0:
            if n % 13 == 0:
                if n % 14 == 0:
                    if n % 15 == 0:
                        if n % 16 == 0:
                            if n % 17 == 0:
                                if n % 18 == 0:
                                    if n % 19 == 0:
                                        if n % 20 == 0:
                                            print 'Very dividable:', str(n)

x = 1

while x < 1000000000:
    testdiv(x)
    x = x + 1
