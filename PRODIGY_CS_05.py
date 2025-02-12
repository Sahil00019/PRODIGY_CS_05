from scapy.all import sniff, IP, TCP, UDP, Ether
def packet_callback(packet):
    """
    Callback function to process each captured packet.
    """
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        if protocol == 6 and packet.haslayer(TCP):
            protocol_name = "TCP"
            payload = bytes(packet[TCP].payload).decode('utf-8', errors='ignore')
        elif protocol == 17 and packet.haslayer(UDP):
            protocol_name = "UDP"
            payload = bytes(packet[UDP].payload).decode('utf-8', errors='ignore')
        else:
            protocol_name = "Other"
            payload = ""
        print(f"Source IP: {ip_src} | Destination IP: {ip_dst} | Protocol: {protocol_name}")
        if payload:
            print(f"Payload: {payload[:100]}...")  # Print first 100 characters of payload
        print("-" * 80)
def start_sniffer(interface=None, count=0):
    """
    Start the packet sniffer.
    :param interface: Network interface to sniff on (None for all interfaces).
    :param count: Number of packets to capture (0 for unlimited).
    """
    print("Starting packet sniffer...")
    sniff(iface=interface, prn=packet_callback, count=count)
if __name__ == "__main__":
    print("This tool is for educational purposes only. Do not use it on networks you do not own or have permission to monitor.")
    start_sniffer(interface=None, count=10)