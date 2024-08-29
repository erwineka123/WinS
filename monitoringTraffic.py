#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP, UDP, ARP

def packet_callback(packet):
    packet_len = len(packet)  # Menghitung jumlah byte paket
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        ip_src = ip_layer.src
        ip_dst = ip_layer.dst
        print(f"IP Packet - Src: {ip_src}, Dst: {ip_dst}, Bytes: {packet_len}")

        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"  TCP Packet - Src Port: {tcp_layer.sport}, Dst Port: {tcp_layer.dport}")
        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"  UDP Packet - Src Port: {udp_layer.sport}, Dst Port: {udp_layer.dport}")

    elif packet.haslayer(ARP):
        arp_layer = packet.getlayer(ARP)
        print(f"ARP Packet - Opcode: {arp_layer.opcode}, Src MAC: {arp_layer.hwsrc}, Dst MAC: {arp_layer.hwdst}, Bytes: {packet_len}")

def traffic_monitor():
    print("Starting network traffic monitoring...")
    print("Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    traffic_monitor()
