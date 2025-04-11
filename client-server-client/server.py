import socket
import threading
from collections import defaultdict
import json

HOST = "127.0.0.1"
PORT = 5000

inbox = defaultdict(list) # {"username": [(message, from_user)]}

def recieve_data(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        return data.decode()

def handle_connection(conn, addr):
    with conn:
        print(f"Connected with {addr}")
        data = json.loads(recieve_data(conn))
        print(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_connection, args=[conn, addr])
        thread.start()