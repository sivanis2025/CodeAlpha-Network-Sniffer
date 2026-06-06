from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def analyze_packet(packet):
    print("\n---------------- Packet Captured ----------------")

    if IP in packet:
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if TCP in packet:
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif ICMP in packet:
            print("Protocol: ICMP")

        else:
            print("Protocol: Other IP Protocol")

        if Raw in packet:
            print("Payload:", packet[Raw].load[:50])
        else:
            print("Payload: No payload")

    else:
        print("Non-IP Packet")
        print(packet.summary())

print("Network Sniffer Started...")
print("Capturing 20 packets...")
print("Use internet normally or open any website.")

sniff(prn=analyze_packet, count=20)

print("\nSniffing completed.")