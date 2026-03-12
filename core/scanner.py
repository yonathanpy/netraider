import socket
import concurrent.futures

COMMON_PORTS = [
21,22,23,25,53,80,110,111,135,139,
143,443,445,993,995,1723,3306,3389,
5900,8080
]


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        sock.connect((host, port))
        return port
    except:
        return None
    finally:
        sock.close()


def scan_host(host):
    print(f"Scanning {host}")

    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(scan_port, host, p) for p in COMMON_PORTS]

        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)

    print("Open ports:")
    for p in open_ports:
        print(p)
