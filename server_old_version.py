import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('0.0.0.0', 5000)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server is listening for incoming connections...')

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Connected to client: {client_address}')
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            if not data:
                # Break the inner loop if no data is received (client closed the connection)
                break
            print(f'Received data from client: {data}')

            # Send a response back to the client
            response = "Data received successfully!"
            client_socket.send(response.encode())

    finally:
        # Close the client socket
        client_socket.close()
        print(f'Connection to client {client_address} has been closed.')