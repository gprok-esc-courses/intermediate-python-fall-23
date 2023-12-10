from socket import socket, AF_INET, SOCK_STREAM
import threading

def client_thread(sock):
    while True:
        msg_bytes = client_socket.recv(1024)
        msg = msg_bytes.decode('utf-8')
        # Decrypt the message
        print(msg)

# Generate Keys

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5004))

# Receive the server's public key
# Send client's public key to the server

name = input("Give your name: ")
msg_bytes = str.encode(name)
# Encrypt name
client_socket.send(msg_bytes)

th = threading.Thread(target=client_thread, args=(client_socket, ))
th.start()

while True:
    msg = input(": ")
    # Encrypt message
    client_socket.send(str.encode(msg))
