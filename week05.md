## Weak 05 Journal Activity
## 1. RSA Key Generation using Python

-Genertaed Python: 
import random
from math import gcd

#  two random prime numbers between 175 and 410
primes = [179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409]
p = random.choice(primes)
q = random.choice([x for x in primes if x != p])

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

#  Choose e (1 < e < phi_n) and gcd(e, phi_n) = 1
for e in range(3, phi_n, 2):
    if gcd(e, phi_n) == 1:
        break

#  Calculate d using modular inverse
d = pow(e, -1, phi_n)

print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")
print(f"p = {p}, q = {q}, φ(n) = {phi_n}")

## Printed outputs: 
Public Key (e, n): (3, 62677)
Private Key (d, n): (41451, 62677)
p = 269, q = 233, φ(n) = 62176

## 2. RSA Encryption and Decryption
-Generated Python: 
def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Enter your keys from previous step
e = int(input("Enter Public Key (e): "))
n = int(input("Enter Public Key (n): "))
d = int(input("Enter Private Key (d): "))

# Choose a 3-digit message
message = int(input("Enter a 3-digit integer message (M): "))

# Encrypt and Decrypt
ciphertext = encrypt(message, e, n)
decrypted_message = decrypt(ciphertext, d, n)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")


-Values I enter: e = 2, n = 3, d = 4, and M = 5

# Results: 
Enter Public Key (e): 2
Enter Public Key (n): 3
Enter Private Key (d): 4
Enter a 3-digit integer message (M): 5
Ciphertext: 1
Decrypted Message: 1

## 3.RSA Keys in OpenSSL
-Generate RSA Keypair using OpenSSL:
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
-Extract the Public Key:

openssl rsa -in private_key.pem -pubout -out public_key.pem

-View Keys:

cat private_key.pem
cat public_key.pem

# Public key: 

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp09UCrafzk2UnypsgwOf
MawMc1SrLTRqLSsCrL0y1+WWQasJPktHavl0IRek5kfYkDSfRo+JI6jSQJj6K0a3
WMyFg8fF0wo7pQvEQD9H/rkzqQTRa7AF7CJhfJznTv3ZS0Sav/ZCka6t6MHjwszj
dnfpyRLTW+Ui10zu6Gk2dO8f1/D16orov4yrT0UK7OV6pCuTV87xU3Q6754mPuif
vUcs6Ub9OmYz01NI8n2WvQiR8mAx3Id/gbRoHZt3Q8ZWJQP6rxBdPuvhxGlHH/I6
mH/vsiKZDL/jgG4QgVCyw78rqSB11ek24OgDUQ6f/ofzdZQUj2PtyzlnTqIjRA67
zwIDAQAB
-----END PUBLIC KEY-----

## 4. RSA Encryption and Decryption in OpenSSL
✅ Encrypt Using pkeyutl

openssl pkeyutl -encrypt -in message.txt -pubin -inkey public_key.pem -out encrypted_message.bin

✅ Decrypt Using pkeyutl

openssl pkeyutl -decrypt -in encrypted_message.bin -inkey private_key.pem -out decrypted_message.txt

✅ Check Decrypted Message

cat decrypted_message.txt

Output: 

Hello, this is a secret message.
