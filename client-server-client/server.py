import socket
import threading
from collections import defaultdict
import json

HOST = "127.0.0.1"
PORT = 5000
END_DELIMETER = "*&^%"

inbox = defaultdict(list) # {"username": [(message, from_user)]}

def recieve_data(conn):
    full_packet = ""
    while True:
        packet = conn.recv(1024).decode()
        full_packet = full_packet.join(packet)
        if full_packet[len(full_packet)-len(END_DELIMETER):] == END_DELIMETER:
            break
    return full_packet[:len(full_packet)-len(END_DELIMETER)]

def handle_connection(conn, addr):
    with conn:
        print(f"Connected with {addr}")
        data = json.loads(recieve_data(conn))
        while data["task"] != "dc":
            print(data, "\n")
            data = json.loads(recieve_data(conn))
    print(f"Disconnected from {addr}\n\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_connection, args=[conn, addr])
        thread.start()