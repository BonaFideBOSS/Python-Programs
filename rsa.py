import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a   

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y
        
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q):
    n = p*q
    phi = ((p-1)*(q-1))

    e = 17

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi) 

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

def factorize(x):
   nums = []
   for i in range(2, x):
       if x % i == 0:
           nums.append(i)
   return nums

#Result of factorization
p,q = factorize(629)
#p = 17
#q = 37

public, private = generate_keypair(p, q)

#Decryption
#print(decrypt(private,[]))

message = input("Type message: ")

encrypted_msg = encrypt(public, message)

print(f"{encrypted_msg}")

print (f"Decrypted Message is : {decrypt(private,encrypted_msg)}")
