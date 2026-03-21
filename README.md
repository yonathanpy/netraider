<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:002200,100:004400&height=180&section=header&text=NETRAIDER🔍Recon+Engine&fontSize=60&fontColor=00ff77&desc=Witwizard&descSize=18&descColor=cccccc" />
</p>

# NETRAIDER

NetRaider is a modular network reconnaissance and traffic inspection framework written in Python.

The system integrates high‑speed port scanning, packet capture, and protocol inspection into a single runtime environment designed for network analysis and research.

---

## Architecture

```
Target Host
    │
Port Scanner
    │
Service Fingerprinter
    │
Packet Capture Engine
    │
Protocol Analyzer
```

The scanner identifies reachable services while the packet capture subsystem observes network traffic in real time.

---

## Subsystems

### Scanner

Concurrent TCP port scanning using thread pools.

Capabilities:

- high‑speed port enumeration
- connection timeout control
- parallel socket execution
- open service detection

---

### Sniffer

Real‑time packet capture engine built on top of Scapy.

Responsibilities:

- packet interception
- protocol detection
- source/destination analysis
- packet forwarding to analysis modules

---

### Packet Analyzer

Decodes network packets into structured records.

Extracted attributes include:

- source IP
- destination IP
- transport protocol
- source port
- destination port

---

### Service Fingerprinter

Maps detected open ports to probable services.

Used to infer network service topology after scanning.

---

## Usage

Run host scan:

```
python main.py scan 192.168.1.1
```

Run packet sniffer:

```
python main.py sniff eth0
```

---

## Repository Layout

```
core/
    scanner.py
    sniffer.py
    analyzer.py

network/
    packets.py
    fingerprint.py

utils/
    logger.py
```

---

## Author

Yonathan,aka Witwizard
