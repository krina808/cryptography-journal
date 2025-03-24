## Week 07 Journal Activity
## Capturing HTTPS Traffic with Wireshark
# Filter Traffic for TLS & HTTP
![Image Description](./images/Week7_tls.png)

![Image Description](./images/Week7_http.png)
# Inspect the TLS Handshake

![Image Description](./images/Week7_client_hello.png)

![Image Description](./images/Week7_server_hello.png)

## Python Code for Simulating TLS using SSL Library

![Image Description](./images/Week7_python.png)
running sslmodule.py: 
'''python
import socket
import ssl


host = 'www.google.com'
port = 443

context = ssl.create_default_context()
with socket.create_connection((host, port)) as sock:
    with context.wrap_socket(sock, server_hostname=host) as ssock:
        print("SSL established. Peer:", ssock.getpeercert())
        print("Cipher used:", ssock.cipher())
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
        data = ssock.recv(4096)
        print("Received:", data.decode('utf-8', errors='ignore')) ''''






## Insights and Reflections
I found out better about how crucial secure communication is over the internet while analyzing TLS traffic through Wireshark. This shows how symmetric and asymmetric cryptography work together to implement the TLS handshake process. I witnessed how websites exchange and verify the certificates to establish their identity to a user. I also took note of the encrypted payloads over HTTPS to make sure that the transmitted data is confidential. Then this practical experience showed that having secure connections is so important for being able to protect data privacy and prevent the spreading of cyber threats.

