from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())

def start_sniffer(interface, packet_count=10):
    print(f"Starting packet capture on {interface}...")
    sniff(prn=packet_callback, iface=interface, count=packet_count)
