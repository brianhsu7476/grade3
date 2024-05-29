import socket

# Set up the UDP client
UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 5005     # The port to listen on

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on {UDP_IP}:{UDP_PORT}")

while True:
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    
    print(f"Received message: {data.decode()} from {addr}")
    
    # Send a response back to the sender
    response_message = "Hello, UDP server!"
    sock.sendto(response_message.encode(), addr)
    print(f"Sent response to {addr}")
