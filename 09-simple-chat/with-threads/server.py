from socket import socket, AF_INET, SOCK_STREAM
import threading


def client_thread(con, name):
    print(name, "thread started")
    while True:
        msg_bytes = conn.recv(1024)
        msg = msg_bytes.decode('utf-8')
        print(msg)
        message = name + ": " + msg
        for client in clients:
            if con != client['conn']:
                client['conn'].send(str.encode(message))


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5004))

clients = []

server_socket.listen()
print("Server started on port 5003")

while True:
    conn, addr = server_socket.accept()
    print("Connection request from ", addr)

    name_bytes = conn.recv(1024)
    name = name_bytes.decode('utf-8')
    print(name)

    client = {'conn': conn, 'addr': addr, 'name': name}
    clients.append(client)

    th = threading.Thread(target=client_thread, args=(conn, name))
    th.start()
