### Demonstrates RSA public-private key encryption
import random

def generatePrimes(a, b, n): #generates n prime numbers between a and b.
    return 7, 13 #write an actual thing

def lcm(a, b): #returns least common multiple of a and b.
    return int(a/(gcd(a, b)) * b)

def gcd(a, b): #returns the greateast common divisor of a and b. Euclidean algorithm
    remainder = a
    while(remainder > 0):
        remainder = b % a
        b = a
        a = remainder
    return b
    
def isDivisor(a, b): #returns TRUE if a is a divisor of b. 
    return (b%a == 0)

def modularMultiplicativeInverse(a, b): #returns d, given d*e = 1 mod (b)
    if(gcd(a, b) == 1): #Check if a and b are coprime.
        return (a % b + b) % b
    else:
        print("oiwiefohfowieh")


print(modularMultiplicativeInverse(5, 13))