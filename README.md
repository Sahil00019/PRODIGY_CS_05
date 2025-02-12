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
---
## **Ethical Use :**

### This tool is intended for educational purposes only. Ensure you have proper authorization before using it on any network. Unauthorized use of packet sniffers may violate local laws and regulations.
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
