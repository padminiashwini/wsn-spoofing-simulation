from scapy.all import IP, UDP, Raw, send

# Craft a spoofed UDP packet
pkt = IP(src="192.168.1.101", dst="127.0.0.1")/UDP(sport=4444, dport=9999)/Raw(load="FAKE_SENSOR_DATA")

# Send the packet
send(pkt)
