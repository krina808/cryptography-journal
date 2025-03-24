## Week 08 Journal Activity
## Algorithms Used

-SHA-256: A secure cryptographic hash function that produces a 256-bit hash value. It is widely used in blockchain, digital signatures, and data integrity checks.

-HMAC (Hash-based Message Authentication Code): Uses a secret key and hash function (e.g., SHA-256) to authenticate messages and ensure data integrity.

## Python Code for Simulation
# SHA-256 Hashing

running: nano SHA-256_Hashing.py
![Image Description](./images/week08_sha-256-hashing.png)

SHA-256 generates a fixed-length 64-character hexadecimal hash, ensuring data integrity. Even a small change in input results in a drastically different hash output due to the avalanche effect.

# HMAC using SHA-256

running: nano HMAC_SHA-256.py

![Image Description](./images/week08_HMAC_sha-256.png)


HMAC ensures data authenticity, as any change in data without the correct key will produce a different HMAC. It is resistant to attacks like replay attacks, ensuring data security in client-server communication.

## Insights and Reflections
-Hash functions provide robust security for data integrity by ensuring any small change in the input results in a significantly different hash output (avalanche effect).

-HMAC ensures both data authenticity and integrity by adding a layer of protection with a secret key, making it useful in secure communication protocols like TLS and SSL.

-While SHA-256 is collision-resistant, it is computationally expensive, so choosing algorithms based on use case scenarios is crucial.
