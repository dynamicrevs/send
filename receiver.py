import socket

# Set up the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pi_ip = "192.168.104.36"  # Replace this with the Raspberry Pi's IP address
server_address = (pi_ip, 8096)  # Use the same port as in the Raspberry Pi script

try:
    # Connect to the Raspberry Pi
    client_socket.connect(server_address)

    # Receive data continuously
    while True:
        data_received = client_socket.recv(1024)
        print("Data received from Raspberry Pi:", data_received.decode())

finally:
    # Clean up the connection
    client_socket.close()
