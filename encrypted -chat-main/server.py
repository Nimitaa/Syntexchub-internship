import socket
import threading

HOST = "127.0.0.1"
PORT = 5500

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break 
            print ("encrypted received:" ,message)

            with open("chat_log.txt", "a") as f:
                f.write(message.decode() + "\n")

            broadcast(message, client)

        except:
            clients.remove(client)
            client.close()
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server started... Waiting for clients")

while True:
    client, addr = server.accept()
    print("Connected:", addr)

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()