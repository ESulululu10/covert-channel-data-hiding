from scapy.all import IP, Raw, sniff, TCP 
 
def analyze(packet): 
    """ Analyze the sniffed packets. """ 
    try: 
        # Read only TCP packet 
        if packet.haslayer(TCP): 
            # Read only reply from sender PC in given port number 
            if packet[IP].src == ip_address and packet[TCP].dport == int(port): 
                print('Source:', packet[IP].src) 
                print('Message:', packet[Raw].load.decode('utf-8')) 
                print('-' * 100) 
    except Exception as e: 
        print(e) 
 
# Parameters 
print('-' * 100) 
interface = input("Enter interface: ") 
ip_address = input("Enter IP address to listen: ") 
port = input("Enter port to listen: ") 
print('-' * 100) 
 
# Status 
print("Listening on interface '{}' in port {} for '{}'...".format(interface, port, ip_address)) 
print('-' * 100) 
 
# Sniff 
sniffed = sniff(iface=interface, store=False, prn=analyze)
