import socket
import json

HOST = "127.0.0.1"
PORT = 5000

def send_data(data):
    s.connect((HOST, PORT))
    s.sendall(data)
    print("All packets sent successfully")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    username = input("What is your username? ")
    task = None
    while not task:
        data = {}
        data["username"] = username
        task = input("Would you like to view your inbox (vi), or send a message (sm): ")
        data["task"] = task
        if task == "vi":
            pass
        elif task == "sm":
            to_user = input("Who do you want to send a message to? ")
            message = input("What is the message? ")
            data["to_user"] = to_user
            data["message"] = message
        else:
            print("task invalid")
            task = None
            continue

        json_data = json.dumps(data).encode()
        send_data(json_data)