### Demonstrates RSA public-private key encryption
import random

def generatePrimes(a, b, n): #generates n prime numbers between a and b.
    return 127, 131  #write an actual thing

def lcm(a, b): #returns least common multiple of a and b.
    return int(a/(gcd(a, b)) * b)

def gcd(a, b): #returns the greateast common divisor of a and b. Euclidean algorithm
    remainder = a
    while(remainder > 0):
        remainder = b % a
        b = a
        a = remainder
    return b
    
def isCoPrime(a, b): #returns TRUE if a is a coprime of b. 
    return (gcd(a, b) != 1)

def modularMultiplicativeInverse(a, b): #returns d, given d*a = 1 mod (b). !Requires b to be prime. Euler's Theorem.
    if(gcd(a, b) == 1): #Check if a and b are coprime.
        return (a**(b-2) % b)
    else:
        raise Exception("Multiplicative Modulo Inverse does not exist for " + str(a) + str(b))



if __name__ == "__main__":
    p, q = generatePrimes(2, 3, 1)
    n = p*q
    phiN = lcm(p-1, q-1)
    print("phiN is " + str(phiN))   
    e = 109   #Write generate e function
    if isCoPrime(e, phiN):
        raise Exception("e is coprime with phiN")
    d = modularMultiplicativeInverse(e, phiN)
    print("Public Key is: " + str(e) + ", " +str(n))
    print("Private Key is: " + str(d) + ", " + str(n))
    plainText = int(input("Input plaintext: "))
    cipherText = plainText**e % n
    print("Ciphertext is: " + str(cipherText))
    key = int(input("Input key: "))
    message = cipherText**key % n
    print(message)


