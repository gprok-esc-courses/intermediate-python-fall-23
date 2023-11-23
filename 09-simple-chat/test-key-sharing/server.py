import rsa
from socket import socket, AF_INET, SOCK_STREAM

public_key, private_key = rsa.newkeys(1024)

print(public_key.save_pkcs1())

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5002))

server_socket.listen()
print("Server started on port 5002")

while True:
    conn, addr = server_socket.accept()
    print("Connection request from ", addr)

    # EXERCISE: receive client's public key

    conn.send(public_key.save_pkcs1())

    msg_bytes = conn.recv(1024)
    msg = rsa.decrypt(msg_bytes, private_key).decode('utf-8')
    print(msg)

    # EXERCISE: send back an encrypted message "Hello clients-name"
