import socket

# Server details
server_ip = "85.215.76.149"  # Replace with the IP address of your server
server_port = 5000  # Replace with the port number of your server

# Initialize data
data = 0  # Start with numeric data if you plan to increment it

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Main loop
while True:
    var = input("Please enter 'send' to send data: ")
    if var == "send":
        # Prepare the message to send
        message = f"Data: {data} the next one will be: {data + 1}"

        # Send data to the server
        client_socket.send(message.encode())

        # respons massage from the server after client
        response = client_socket.recv(1024).decode()

        print(f"This is the Response from the Server: {response}")

        # Increment data
        data += 1

# Optionally, close the connection outside the loop or handle with try/except to manage errors
#client_socket.close()

