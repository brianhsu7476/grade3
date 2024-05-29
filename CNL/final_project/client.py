import socket, time, threading, random

# Set up the UDP server
UDP_IP = "10.5.6.119"  # The IP address of the UDP client
UDP_PORT = 5005		  # The port of the UDP client
MESSAGE = "Hello, UDP client!"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_loop():
	while True:
		random_num = random.random()
		MESSAGE = 'client'
		# Send the message to the UDP client
		sock.sendto(f"{MESSAGE} {random_num}".encode(), (UDP_IP, UDP_PORT))
		print(f"'{MESSAGE} {random_num}' sent to {UDP_IP}:{UDP_PORT}")
		time.sleep(1)

def recv_loop():
	while True:
		data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
		print(f"Received message: {data} from {addr}")

if __name__ == "__main__":
	# Create threads for sending and receiving messages
	send_thread = threading.Thread(target=send_loop)
	recv_thread = threading.Thread(target=recv_loop)

	# Start the threads
	send_thread.start()
	recv_thread.start()

	# Join the threads to the main thread to keep them running
	send_thread.join()
	recv_thread.join()
