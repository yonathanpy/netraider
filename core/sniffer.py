from scapy.all import sniff
from network.packets import parse_packet


def process(packet):
    result = parse_packet(packet)
    if result:
        print(result)


def start_sniffer(interface):
    print(f"Listening on {interface}")
    sniff(iface=interface, prn=process, store=False)
