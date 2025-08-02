import socket

def scan_ports(ip):
    print(f"Scanning {ip} for open ports...")
    for port in range(20, 1025):
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()

scan_ports("127.0.0.1")
