import socket

def scan_ports(ip_address, start_port, end_port):
    """ Memindai port pada IP address tertentu """
    print(f"🌐 Scanning ports from {start_port} to {end_port} on {ip_address}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    if open_ports:
        print(f"🔓 Open ports: {open_ports}")
    else:
        print("🔒 No open ports found.")
