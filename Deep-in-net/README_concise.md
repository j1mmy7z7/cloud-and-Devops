# Deep-in-Net Project Report

## Overview
This report documents the networking concepts and practical exercises completed for the Deep-in-Net project. It covers the OSI model, IP addressing schemes, and the configuration of network devices including hubs, switches, and routers.

## Key Concepts

*   **OSI Model:** A 7-layer framework for network communication (Physical, Data-link, Network, Transport, Session, Presentation, Application).
*   **Devices:**
    *   **Hub (Layer 1):** Broadcasts data to all ports; less secure/efficient.
    *   **Switch (Layer 2):** Uses MAC addresses to filter and forward data to specific devices.
    *   **Router (Layer 3):** Routes packets between different networks using IP addresses.
*   **Protocols:**
    *   **TCP/UDP:** Transport protocols. TCP is reliable (connection-oriented); UDP is fast (connectionless).
    *   **DHCP:** Automatically assigns IP addresses to clients.
    *   **DNS:** Resolves domain names to IP addresses.

## Exercises

### Ex01: Peer-to-Peer
![ex01](pics/ex01.jpg)
*   **Objective:** Connect PCs using cross-over cables.
*   **Networks:**
    *   `192.168.1.0/24` (Standard Class C)
    *   `192.168.13.80/29` (Subnetted, 6 usable IPs)
    *   `192.168.13.248/29`

### Ex02: Hubs vs Switches
![ex02](pics/ex02.jpg)
*   **Switch Network:** `192.168.1.0/29` (Efficient traffic management).
*   **Hub Network:** `192.168.1.192/27` (Broadcasts traffic to all nodes).

### Ex03: Servers & Services
![ex03](pics/ex03.jpg)
*   **Network:** `192.168.1.0/24`
*   **Configured Services:**
    *   **HTTPS Server:** `192.168.1.99` (Secure Web)
    *   **DNS Server:** `192.168.1.101` (Domain Resolution)
    *   **DHCP Server:** Assigns IPs starting from `192.168.1.1`.

### Ex04: Routing Basics
![ex04](pics/ex04.jpg)
*   **Objective:** Connect two subnets via a router.
*   **Configuration:**
    *   **PC 1:** `192.168.1.2/30` (GW: `192.168.1.1`)
    *   **PC 2:** `192.168.2.2/30` (GW: `192.168.2.1`)
    *   **Router:** Interfaces configured with Gateway IPs.

### Ex05: Extended Network
![ex05](pics/ex05.jpg)
*   **Objective:** Route between a small subnet and a larger subnet.
*   **Network A:** `192.168.1.0/29`
*   **Network B:** `192.168.1.192/27`

### Ex06: WAN & Static Routing
![ex06](pics/ex06.jpg)
*   **Objective:** Connect two routers via a serial WAN link.
*   **Topology:**
    *   **LAN 1:** `192.168.1.0/24`
    *   **LAN 2:** `192.168.2.0/24`
    *   **WAN:** `10.10.0.0/30`
*   **Static Routes:**
    *   **Router 1:** `ip route 192.168.2.0 255.255.255.0 10.10.0.2`
    *   **Router 2:** `ip route 192.168.1.0 255.255.255.0 10.10.0.1`

### Ex07: Multi-Router LAN
![ex07](pics/ex07.jpg)
*   **Objective:** Similar to Ex06 but with larger LANs (switches + multiple PCs).
*   **Routing:** Configured mutually to allow traffic between `192.168.1.0/24` and `192.168.2.0/24`.

### Ex08: Complex Routing (3 Routers)
![ex08](pics/ex08.jpg)
*   **Objective:** Route traffic across 3 distinct networks using 2 WAN links.
*   **Networks:**
    1.  `192.168.1.192/26`
    2.  `192.168.2.0/24`
    3.  `192.168.3.160/28`
*   **Routing Logic:**
    *   **Router 1:** Routes to Net 2 & 3 via Router 2.
    *   **Router 2:** Routes to Net 1 via Router 1; Net 3 via Router 3.
    *   **Router 3:** Routes to Net 1 & 2 via Router 2.
