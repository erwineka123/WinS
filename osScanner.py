import os
import platform

def os_scan(ip_address):
    # Menampilkan informasi OS yang terkait dengan IP address
    os_name = os.name
    if os_name == 'posix':
        os_name = 'Unix-like (Linux/MacOS)'
    elif os_name == 'nt':
        os_name = 'Windows'
    else:
        os_name = 'Unknown OS'
    
    platform_name = platform.system()
    platform_version = platform.version()
    architecture = platform.machine()
    platform_details = platform.platform()

    print(f"\nScanning OS details for IP address: {ip_address}")
    print(f"OS Name: {os_name}")
    print(f"Platform: {platform_name}")
    print(f"Version: {platform_version}")
    print(f"Architecture: {architecture}")
    print(f"Platform Details: {platform_details}")
