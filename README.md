# WSN Spoofing Simulation using Scapy

This is a basic simulation of a spoofing attack in a Wireless Sensor Network (WSN) using Scapy, performed entirely within a single Kali Linux VM.

## 💡 What It Demonstrates

- Packet spoofing (fake source IP)
- Simulated WSN node sending forged data
- UDP listener acting as a sink node
- Localhost-based network simulation

## Files

- `receiver.py` – Simulates a WSN sink node by listening on UDP port `9999`
- `spoof_sender.py` – Sends a spoofed UDP packet using Scapy

## Requirements

- Kali Linux VM
- Python 3
- Scapy (install with `sudo apt install scapy`)

## How to Run-

### 1. Start the UDP Listener

```bash
python3 receiver.py
```

### 2. Send Spoofed Packet

```bash
sudo python3 spoof_sender.py