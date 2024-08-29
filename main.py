import portScanner
import protocolScanner
import networkSniffer

def print_ascii_art():
    print(r"""
    ██╗    ██╗██╗███╗   ██╗██ ███████╗
    ██║    ██║██║████╗  ██║   ██╔════╝
    ██║ █╗ ██║██║██╔██╗ ██║   ███████╗
    ██║███╗██║██║██║╚██╗██║   ╚════██║
    ╚███╔███╔╝██║██║ ╚████║   ███████║
    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚   ╚══════╝ 
          """)
    print("✨ Welcome to CyberDefender✨")
          

def main():
    print_ascii_art()

    while True:
        print("\nChoose a feature to run:")
        print("1. Port Scanner")
        print("2. Protocol Scanner")
        print("3. Network Sniffer")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            ip_address = input("Enter IP address to scan: ")
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            portScanner.scan_ports(ip_address, start_port, end_port)

        elif choice == '2':
            ip_address = input("Enter IP address to scan: ")
            ports = list(map(int, input("Enter ports to scan (comma separated): ").split(',')))
            protocolScanner.protocol_scan(ip_address, ports)

        elif choice == '3':
            interface = input("Enter the network interface to monitor (or press Enter for default): ")
            networkSniffer.start_sniffer(interface)

        elif choice == '4':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    while True:
        main()
        continue_choice = input("\nDo you want to run another feature? (y/n): ")
        if continue_choice.lower() != 'y':
            print("Thank you for using CyberDefender! 🌟")
            break