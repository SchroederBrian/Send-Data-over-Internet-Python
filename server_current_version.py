import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f'Received data from client: {data}')
        response = "Data received successfully!"
        client_socket.send(response.encode())
    client_socket.close()
    print(f'Connection to client {client_address} has been closed.')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 5000)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()