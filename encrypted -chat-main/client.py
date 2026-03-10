import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

HOST = "127.0.0.1"
PORT = 5500

print("creating socket..")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to secure chat")

def receive_messages():
    while True:
        try:
            encrypted = client.recv(1024)
            message = decrypt_message(encrypted)
            print("\nFriend:", message)
        except:
            print("Connection closed")
            client.close()
            break

def send_messages():
    while True:
        message = input("You: ")
        encrypted = encrypt_message(message)
        client.send(encrypted)
        print("encrypted message:",encrypted)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_messages()
