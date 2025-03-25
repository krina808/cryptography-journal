## Week 08 Journal Activity
## Algorithms Used

-SHA-256:  A secure cryptographic hash function which produces a 256 bit hash value. Very frequently used in blockchain, digital signatures and data integrity checks.

-HMAC (Hash-based Message Authentication Code):  It authenticates messages using a secret key and an available hash function (SHA-256, etc) to ensure data integrity.

## Python Code for Simulation
# SHA-256 Hashing

running: nano SHA-256_Hashing.py
![Image Description](./images/week08_sha-256-hashing.png)

In other words, SHA-256 produces a fixed 64 characters in length hexadecimal hash which verifies data integrity. The avalanche effect guarantees that even a little change in input will yield a completely different hash output..

# HMAC using SHA-256

running: nano HMAC_SHA-256.py

![Image Description](./images/week08_HMAC_sha-256.png)


This provides data authentication that, if data is changed and the correct key is formed, an HMAC will be different. Data security during client server communication is provided by it and is resistant to attacks like replay attack.

## Insights and Reflections
-With robust security for the data integrity, it allows any small change in an input to create a very different hash output (avalanche effect).

-Depending on the protocol application, HMAC helps provide some protection by adding a layer of security through a secret key - which is used to make secure communication protocols like TLS and SSL secure.

-SHA256 is resistant to collisions but computationally expensive, used in real life, it has to be chosen algorithm based case by case.
