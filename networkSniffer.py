from scapy.all import sniff, TCP, IP

def packet_callback(packet):
    # Pastikan paket memiliki layer TCP
    if packet.haslayer(TCP):
        src_ip = packet[IP].src  # Alamat IP sumber
        dst_ip = packet[IP].dst  # Alamat IP tujuan
        src_port = packet[TCP].sport  # Port sumber
        dst_port = packet[TCP].dport  # Port tujuan

        # Tampilkan hasil tangkapan paket yang relevan
        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip} | Source Port: {src_port} -> Destination Port: {dst_port}")

def start_sniffer(interface, packet_count=10):
    print(f"Starting packet capture on {interface}...")
    sniff(prn=packet_callback, iface=interface, count=packet_count)

# Misalnya, Anda bisa memanggil fungsi ini seperti berikut:
# start_sniffer("eth0", 10)
