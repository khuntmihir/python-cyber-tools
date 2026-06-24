import socket

target = input("Enter target IP address: ")

print(f"\nScanning target: {target}\n")

for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")

    sock.close()

print("\nScan completed.")
