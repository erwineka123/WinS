import socket

def protocol_scan(ip_address, ports):
    """ Memindai protokol pada port tertentu di IP address """
    print(f"🔍 Scanning protocols on {ip_address} for ports: {ports}")
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip_address, port))
            sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
            response = sock.recv(100)
            try:
                # Coba mendekode sebagai UTF-8
                decoded_response = response.decode('utf-8')
                print(f"Port {port}: {decoded_response.splitlines()[0]}")
            except UnicodeDecodeError:
                print(f"Port {port}: Received non-UTF-8 data")
        except Exception as e:
            print(f"Port {port}: {e}")
        finally:
            sock.close()
