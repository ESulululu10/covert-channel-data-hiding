# Covert Channel & Data Hiding in TCP/IP Networks

> 📚 Coursework submission for **Digital Crime Investigation**  
> 👨‍🎓 Author: Gaurab Khadka 
> 🧪 Focus: Covert channels, TCP/IP protocol exploitation, forensic detection, and Wireshark packet analysis

---

## 📝 Project Summary

This project demonstrates **covert channel communication** by embedding hidden messages within TCP/IP packets using **Kali Linux** and **Ubuntu** environments. It shows how attackers can bypass detection using protocol weaknesses and highlights detection techniques via **Wireshark**.

### 🔒 What’s a Covert Channel?

A covert channel is a communication method used to transfer information secretly, bypassing normal security measures. It often exploits standard protocols like **TCP**, **ARP**, and **DHCP**.

---

## 🎯 Aims & Objectives

- To analyze covert channels in TCP/IP protocols
- To demonstrate hidden data transfer between two machines
- To detect hidden messages using network forensics tools
- To understand the legal and ethical implications of covert channels

---

## ⚙️ Setup & Tools Used

| Tool | Purpose |
|------|---------|
| **Kali Linux** | Packet analysis, receiver machine |
| **Ubuntu** | Message sender |
| **Wireshark** | Packet sniffing & analysis |
| **Python (Socket Programming)** | Custom scripts for sending/receiving messages |

---

## 🧪 Demonstration Workflow

1. Ubuntu sends TCP packets with hidden message bytes
2. Kali Linux listens for TCP SYN packets and responds
3. Wireshark monitors and logs packet exchanges
4. The covert message is reconstructed by the receiver script

### 📌 Key Demonstrations

- Sending/receiving crafted TCP packets
- Wireshark analysis of SYN/RST behaviors
- IP validation & ICMP ping communication
- Hidden data detection through byte-level investigation

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| `Covert_Channel_Report_GaurabKhadka.pdf` | Full academic report with demonstration, analysis, and conclusion |
| `sender_script.py` | Python script to send covert data from Ubuntu |
| `receiver_script.py` | Python script to receive and decode data in Kali |
| `images/` | Screenshots of Linux environments and network traces |
| `README.md` | This file |

---

## 📊 Conclusion Summary

> The report concludes that covert channel exploitation of TCP/IP protocols is feasible and difficult to detect without proactive monitoring. Proper logging, network segmentation, and forensic investigation tools like Wireshark are vital in detecting these hidden channels.

---

## 📚 References

- TCP/IP Protocol Suite (Forouzan, 2020)
- Network Security Essentials (Stallings, 2019)
- Wireshark Labs & Packet Analysis Guides
- Cyware, Cisco Docs, RFCs for ARP/DHCP/TCP

---

## ⚠️ Disclaimer

> This project was created for **educational and research purposes only** under academic supervision. Unauthorized or unethical use of covert channels is **illegal** and **discouraged**.

---

## 🙋 About the Author

**Gaurab Khadka**  
> Cybersecurity Enthusiast | MS Computer Science  
> [GitHub Profile](https://github.com/ESulululu10) | [LinkedIn](https://linkedin.com/in/gaurabk)
