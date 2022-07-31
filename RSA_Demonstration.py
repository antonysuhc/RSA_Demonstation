### Demonstrates RSA public-private key encryption
import math

def generatePrimes(b, n): #generates n largest prime numbers between 1 and b. Sieve of Sundaram.
    k = (b-1)/2
    a = [True] * b
    for i in range (1, math.ceil(math.sqrt(k))):
        j = i
        while (i+j+2*i*j <= k):
            a[i+j+2*i*j] = False       #number is not prime if it equals i*j*2ij
            j += 1
    t = [i for i, x in enumerate(a) if x]   # indices of elements in a if element is True
    t = [2*x + 1 for x in t]
    return [t[-(i+1)] for i in range(n)]

def lcm(a, b): #returns least common multiple of a and b.
    return int(a/(gcd(a, b)) * b)

def gcd(a, b): #returns the greateast common divisor of a and b. Euclidean algorithm.
    remainder = a
    while(remainder > 0):
        remainder = b % a
        b = a
        a = remainder
    return b
    
def isCoPrime(a, b): #returns TRUE if a is a coprime of b. 
    return (gcd(a, b) == 1)

def modularMultiplicativeInverse(a, b): #returns d, given d*a = 1 mod (b). Extended Euclidean Algorithm.
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
            #print(pnminus2, pnminus1, pn, qnminus2)
        return pnminus2
    else:
        raise Exception("The modular multiplicative inverse does not exist for " + str(a) + " and " + str(b))

def stringToIntList(str):
    result = []
    for x in str:
        result.extend(ord(i) for i in x)
    return result
def intToString(intList):
    result = ""
    for i in intList:
        result += chr(i)
    return result

if __name__ == "__main__":
    #print(gcd(5381, 8190))
    keySize = int(input("Input key size (<= 1000): "))
    if keySize > 1000:
        raise Exception("Key size must be less than 1000.")
    p, q = generatePrimes(keySize, 2)
    n = p*q
    phiN = lcm(p-1, q-1)
    #print("phiN is " + str(phiN))
    e = generatePrimes(phiN, 1000)[999]
    d = modularMultiplicativeInverse(e, phiN)
    print("Public Key is: " + str(e) + ", " +str(n))
    print("Private Key is: " + str(d) + ", " + str(n))
    plainText = stringToIntList(input("Input plaintext: "))
    cipherText = [pow(i, e, n) for i in plainText]
    try: 
        print("Ciphertext is: " + str(intToString(cipherText)))
    except ValueError:
        print("Ciphertext could not be converted to Unicode due to large key size.")
        print(cipherText)
    key = int(input("Input key: "))
    try: 
        message = intToString([pow(i, key, n) for i in cipherText])
    except ValueError:
        print("Message could not be decoded into text.")
        #print(plainText)
        message = [pow(i, key, n) for i in cipherText]
    print(message)


