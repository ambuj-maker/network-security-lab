# packet_sniffer.py
from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        proto = ''
        if TCP in packet:
            proto = 'TCP'
        elif UDP in packet:
            proto = 'UDP'
        else:
            proto = 'OTHER'

        print(f"[{datetime.now()}] {proto} Packet: {ip_layer.src} -> {ip_layer.dst}")

sniff(prn=process_packet, store=0)
