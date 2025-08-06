import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))

print("Receiver is listening on UDP port 9999...")
while True:
    data, addr = s.recvfrom(1024)
    print(f"[+] Received from {addr}: {data.decode(errors='ignore')}")
