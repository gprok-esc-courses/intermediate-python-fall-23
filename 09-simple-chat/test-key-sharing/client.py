from socket import socket, AF_INET, SOCK_STREAM
import rsa

# EXERCISE: Create the keys of the client

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5002))


# receive the public key of the server
msg_bytes = client_socket.recv(1024)

# EXERCISE: send client's public key to the server

server_public_key = rsa.PublicKey.load_pkcs1(msg_bytes)

print(server_public_key)

name = input("Give your name: ")
msg_bytes = str.encode(name)

message_encrypted = rsa.encrypt(msg_bytes, server_public_key)
print(message_encrypted)

client_socket.send(message_encrypted)

# EXERCISE: receive message from the server and print it



