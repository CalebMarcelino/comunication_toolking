import socket

# Define the host and port for the server
HOST = input('ip: ')  # localhost
PORT = 12345

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((HOST, PORT))

print('Este socket foi criado pelo: Mr Code')
while True:
    # Send a message to the server
    message = input('Digite a mensagem  (ou digite q para sair): ')
    if message == 'q':
        break
    s.sendall(message.encode())

    # Receive and print the echoed message from the server
    data = s.recv(1024)
    print('Received:', data.decode())

# Close the connection
s.close()
