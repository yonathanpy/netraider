from scapy.layers.inet import IP, TCP, UDP


def parse_packet(packet):

    if IP not in packet:
        return None

    src = packet[IP].src
    dst = packet[IP].dst

    proto = None
    sport = None
    dport = None

    if TCP in packet:
        proto = "TCP"
        sport = packet[TCP].sport
        dport = packet[TCP].dport

    elif UDP in packet:
        proto = "UDP"
        sport = packet[UDP].sport
        dport = packet[UDP].dport

    else:
        proto = "OTHER"

    return {
        "src": src,
        "dst": dst,
        "protocol": proto,
        "sport": sport,
        "dport": dport
    }
