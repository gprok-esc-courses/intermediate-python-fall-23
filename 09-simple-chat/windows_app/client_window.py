from tkinter import Tk, Entry, Button, Listbox, Frame, Scrollbar, END, VERTICAL, N, S
from socket import socket, AF_INET, SOCK_STREAM
import threading


def client_thread_read(sock):
    while True:
        msg_bytes = client_socket.recv(1024)
        msg = msg_bytes.decode('utf-8')
        listbox.insert(END, msg)


def client_write():
    msg = entry.get()
    client_socket.send(str.encode(msg))
    entry.delete(0, END)


client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5004))

window = Tk()

listbox = Listbox(window, width=28, height=25)
listbox.grid(row=0, column=0)

# for i in range(50):
#     listbox.insert(END, i)

scrollbar = Scrollbar(window, orient=VERTICAL)
scrollbar.grid(row=0, column=2, sticky=N + S)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

frame = Frame(window)

entry = Entry(frame)
entry.grid(row=0, column=0)

button = Button(frame, text="Send", command=client_write)
button.grid(row=0, column=1)

frame.grid(row=1, column=0, columnspan=1)

name = input("Give your name: ")
window.title(name)
msg_bytes = str.encode(name)
client_socket.send(msg_bytes)

th_read = threading.Thread(target=client_thread_read, args=(client_socket, ))
th_read.start()

window.mainloop()

