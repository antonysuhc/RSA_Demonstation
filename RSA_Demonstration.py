### Demonstrates RSA public-private key encryption
import random

def generatePrimes(a, b, n): #generates n prime numbers between a and b.
    return 283, 293  #write an actual thing

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
    return (gcd(a, b) == 1)

def modularMultiplicativeInverse(a, b): #returns d, given d*a = 1 mod (b). Extended Euclidean Algorithm
    if(isCoPrime(a, b)): #Inverse exists iif a is not coprime to b.
        m = b
        pnminus2 = 0
        pnminus1 = 1
        remainder = b % a
        while(remainder != 0):
            qnminus2 = b//a
            remainder = b % a
            b = a
            a = remainder
            pn = (pnminus2-pnminus1*qnminus2) % m
            pnminus2 = pnminus1
            pnminus1 = pn
            print(pnminus2, pnminus1, pn, qnminus2)
        return pnminus2
    else:
        raise Exception("The modular multiplicative inverse does not exist for " + str(a) + " and " + str(b))



if __name__ == "__main__":
    #print(gcd(5381, 8190))
    p, q = generatePrimes(2, 3, 1)
    n = p*q
    phiN = lcm(p-1, q-1)
    #print("phiN is " + str(phiN))   
    e = 313   #Write generate primes function
    d = modularMultiplicativeInverse(e, phiN)
    print("Public Key is: " + str(e) + ", " +str(n))
    print("Private Key is: " + str(d) + ", " + str(n))
    plainText = int(input("Input plaintext: "))
    if plainText>n:
        raise Exception("Plaintext cannot be larger than n. ")
    cipherText = plainText**e % n
    print("Ciphertext is: " + str(cipherText))
    key = int(input("Input key: "))
    message = cipherText**key % n
    print(message)


