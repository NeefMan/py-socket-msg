import socket
import json

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    username = input("What is your username? ")
    running = True
    while running:
        data = {}
        task = input("Would you like to view your inbox (vi), or send a message (sm), or disconnect (dc): ")
        data["task"] = task
        data["username"] = username
        if task == "vi":
            pass
        elif task == "sm":
            to_user = input("Who do you want to send a message to? ")
            message = input("What is the message? ")
            data["to_user"] = to_user
            data["message"] = message
        elif task == "dc":
            running = False
            continue
        else:
            print("task invalid")
            continue
        
        json_data = json.dumps(data)
        s.sendall(json_data.encode())