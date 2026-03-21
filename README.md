<p align="center">
  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAMAAAC5zwqKAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAAd0SU1FB+YJEg4bEeh8UaEAAAHsUExURUdwTNnZ2d3d3e3t7fX19fn5+f7+/vDw8Pn5+f39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f7+/v7+/v39/fz8/P39/f39/f7+/v7+/v39/fz8/P39/f4AAACGx7TtAAAAS0lEQVR4nO3BAQ0AAADCoPdPbQhqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAfQEBABgABVFLMAAAAABJRU5ErkJggg==" width="400" alt="NetRaider Banner" />
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
