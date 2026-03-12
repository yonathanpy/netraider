SERVICE_MAP = {
22: "ssh",
21: "ftp",
80: "http",
443: "https",
3306: "mysql",
3389: "rdp",
8080: "http-alt"
}


def fingerprint(port):
    return SERVICE_MAP.get(port, "unknown")
