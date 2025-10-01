import math

print("RSA ENCRYPTOR/DECRYPTOR")
print("*****************************************************")

# Input Prime Numbers
print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")

p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
print("*****************************************************")

# Check if Input's are Prime
def prime_check(a):
    if a == 2:
        return True
    elif (a < 2) or (a % 2 == 0):
        return False
    else:
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

check_p = prime_check(p)
check_q = prime_check(q)

while not (check_p and check_q):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

# RSA Modulus
n = p * q
print("RSA Modulus (n) is:", n)

# Euler's Totient
r = (p - 1) * (q - 1)
print("Euler's Totient (r) is:", r)
print("*****************************************************")

# GCD
def egcd(e, r):
    while r != 0:
        e, r = r, e % r
    return e

# Extended Euclidean Algorithm
def eea(a, b):
    if a % b == 0:
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)

# Multiplicative Inverse
def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    if gcd != 1:
        return None
    else:
        return s % r

# e Value Calculation (choose smallest valid e)
for i in range(2, 1000):
    if egcd(i, r) == 1:
        e = i
        break

print("The value of e is:", e)
print("*****************************************************")

# d, Private and Public Keys
d = mult_inv(e, r)
print("The value of d is:", d)

public = (e, n)
private = (d, n)

print("Private Key is:", private)
print("Public Key is:", public)
print("*****************************************************")

# Encryption
def encrypt(pub_key, n_text):
    e, n = pub_key
    x = []
    for i in n_text:
        if i.isupper():
            m = ord(i) - 65
            c = pow(m, e, n)
            x.append(c)
        elif i.islower():
            m = ord(i) - 97
            c = pow(m, e, n)
            x.append(c)
        elif i.isspace():
            x.append(400)
    return x

# Decryption
def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text.split(',')
    x = ''
    for i in txt:
        if i == '400':
            x += ' '
        else:
            m = pow(int(i), d, n)
            c = chr(m + 65)   # only works for uppercase encoding
            x += c
    return x

# Message
message = input("What would you like encrypted or decrypted? (Separate numbers with ',' for decryption): ")
print("Your message is:", message)

# Choose Encrypt or Decrypt
choose = input("Type '1' for encryption and '2' for decryption: ")

if choose == '1':
    enc_msg = encrypt(public, message)
    print("Your encrypted message is:", enc_msg)
    print("Thank you for using the RSA Encryptor. Goodbye!")
elif choose == '2':
    print("Your decrypted message is:", decrypt(private, message))
    print("Thank you for using the RSA Encryptor. Goodbye!")
else:
    print("You entered the wrong option.")
    print("Thank you for using the RSA Encryptor. Goodbye!")
