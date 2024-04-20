import socket
import netifaces as ni
import time

# Get the IP address of the Raspberry Pi
ni.ifaddresses('eth0')
pi_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

# Set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((pi_ip, 8096))  # Use any available port
server_socket.listen(1)

print("Waiting for connection...")

# Accept a connection
connection, client_address = server_socket.accept()

try:
    print("Connection established with", client_address)

    # Send data continuously
    while True:
        # Replace this with the data you want to send
        data_to_send = "Hello from Raspberry Pi!"
        connection.sendall(data_to_send.encode())
        time.sleep(1)  # Adjust the interval as needed

finally:
    # Clean up the connection
    connection.close()
