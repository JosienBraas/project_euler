# Project Euler
# 4 - Largest palindrome product

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

prods = []

def checkpal(n):
    return str(n)[::-1] == str(n)

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        prod = x * y
        prods.append(prod)

pals = filter(checkpal, prods)
pals.sort()

print 'Largest palindrome number:', str(pals[len(pals)-1])