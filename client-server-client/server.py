import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def handle_connection(conn, addr):
    with conn:
        print(f"Connected with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_connection, args=[conn, addr])
        thread.start()