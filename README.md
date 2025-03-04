# **PROJECT TITLE :**

### **NETWORK PACKET ANALYZER**
---
## **DESCRIPTION :**

### A Python-based network packet sniffer tool that captures and analyzes network traffic. This tool is designed for educational purposes to help users understand how network protocols work by inspecting packet details such as source and destination IP addresses, protocols, and payload data.
---
## **Features :**

- **Packet Capture**: Captures live network packets on specified interfaces.
- **Protocol Analysis**: Identifies and displays protocols (e.g., TCP, UDP).
- **Payload Inspection**: Extracts and displays payload data (limited to 100 characters for readability).
- **Ethical Use**: Designed for educational purposes and ethical use only.
---
## **Installation :**

1. Install the required dependencies:
   ```
   pip install scapy
   ```
2. Installation of npcap: https://npcap.com/

   During installation:
   - Check "Install Npcap in WinPcap API-compatible Mode"
   - Check "Support raw 802.11 traffic"

   *After installation: Run the following command in cmd/powershell*
   ```
   python your_script.py -i "Wi-Fi" -c 10
   ```

3. *After verification: Run the final python script*

---
## **Ethical Use :**

### This tool is intended for educational purposes only. Ensure you have proper authorization before using it on any network. Unauthorized use of packet sniffers may violate local laws and regulations.
---

## How Does It Work?

**1. Capturing Network Packets**
   - The script uses scapy.sniff() to listen for incoming and outgoing network packets.

**2. Extracting Packet Information**
   - When a packet is detected, the packet_callback() function is triggered.
   - The script extracts:
       - Source IP Address – The sender of the packet.
       - Destination IP Address – The receiver of the packet.
       - Protocol – Identifies whether it's TCP, UDP, or other protocols.
       - Payload Data – Displays the first 50 bytes of the packet payload for analysis.

**3. Displaying Captured Data**
   - Each captured packet is printed in the format:
```
[+] Packet Captured: TCP | Src: 192.168.1.10 -> Dst: 192.168.1.20
    Payload: b'GET /index.html HTTP/1.1\\r\\nHost: example.com...'
```
   - The payload (if available) helps analyze HTTP requests, DNS queries, and other traffic types.

**4. Running the Sniffer**
   - The script starts sniffing upon execution.
   - It displays available network interfaces before capturing traffic.
   - Press Ctrl + C to stop the sniffer safely.

---
## **Example Output :**

```
Starting packet sniffer...
Source IP: 192.168.1.100 | Destination IP: 192.168.1.1 | Protocol: TCP
Payload: GET / HTTP/1.1...
--------------------------------------------------------------------------------
Source IP: 192.168.1.1 | Destination IP: 192.168.1.100 | Protocol: TCP
Payload: HTTP/1.1 200 OK...
--------------------------------------------------------------------------------
```
