import socket
import threading
from collections import defaultdict
import json

HOST = "127.0.0.1"
PORT = 5000
END_DELIMETER = "*&^%"

inbox = defaultdict(list) # {"username": [(message, from_user)]}

def handle_data(data, conn):
    task = data["task"]
    username = data["username"]
    if task == "sm":
        to_user = data["to_user"]
        message = data["message"]
        inbox[to_user].append((message, username))
        print(f"(Message Request) From: {username} - To: {to_user} - Message: {message}")
    elif task == "vi":
        user_inbox = inbox.get(username)
        conn.sendall((json.dumps(user_inbox)+END_DELIMETER).encode())
        print(f"(View inbox request) For user: {username} - Inbox: {user_inbox}")
        

def recieve_data(conn):
    full_packet = ""
    while True:
        packet = conn.recv(1024).decode()
        full_packet += packet
        if full_packet[len(full_packet)-len(END_DELIMETER):] == END_DELIMETER:
            break
    return full_packet[:len(full_packet)-len(END_DELIMETER)]

def handle_connection(conn, addr):
    with conn:
        print(f"Connected with {addr}")
        data = json.loads(recieve_data(conn))
        while data["task"] != "dc":
            handle_data(data, conn)
            data = json.loads(recieve_data(conn))
    print(f"Disconnected from {addr}\n\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_connection, args=[conn, addr])
        thread.start()