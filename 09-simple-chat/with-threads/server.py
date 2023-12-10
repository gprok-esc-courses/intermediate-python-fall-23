from socket import socket, AF_INET, SOCK_STREAM
import threading

# Generate Server Keys

def client_thread(con, name):
    print(name, "thread started")
    while True:
        msg_bytes = conn.recv(1024)
        msg = msg_bytes.decode('utf-8')
        # Decrypt the message
        print(msg)
        message = name + ": " + msg

        # Store in a messages.csv file as: client_name,message

        for client in clients:
            #if con != client['conn']:
            # Encrypt with client's key
            client['conn'].send(str.encode(message))


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5004))

clients = []

server_socket.listen()
print("Server started on port 5003")

while True:
    conn, addr = server_socket.accept()
    print("Connection request from ", addr)

    # Send the server's public key to the client
    # Receive the public of the client

    name_bytes = conn.recv(1024)
    name = name_bytes.decode('utf-8')
    # Decrypt the name
    print(name)

    client = {'conn': conn, 'addr': addr, 'name': name}
    # client = {'conn': conn, 'addr': addr, 'name': name, 'public_key': public_key}
    clients.append(client)

    th = threading.Thread(target=client_thread, args=(conn, name))
    th.start()
