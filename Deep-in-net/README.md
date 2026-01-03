# DEEP-IN-NET
-> this is the report and findings while doing the deep-in-net project.


## The OSI model
The Open Systems Interconnection model is a set of rules that explains how different computer systems communicate over a newtwork.
The OSI model consists of 7 layers and each layer has specific functions and responsibilites.
They include.
1. Application layer
2. Presentation layer
3. Session layer
4. Transport layer
5. Network layer
6. Data-link layer
7. Physical layer

### Application layer
The application layer is the topmost layer of the OSI model and is responsible for providing services to the end-user. It includes protocols such as HTTP, FTP, SMTP, and DNS.

### Presentation layer
The presentation layer is responsible for data formatting, encryption, and compression. It ensures that data is presented in a consistent format across different systems.

### Session layer
The session layer manages the establishment, maintenance, and termination of sessions between devices. It provides mechanisms for establishing and managing connections between applications.

### Transport layer
The transport layer is responsible for end-to-end communication between devices. It ensures reliable and error-free data transmission by providing mechanisms for flow control, congestion control, and error detection.

### Network layer
The network layer is responsible for routing data packets between networks. It provides mechanisms for addressing, routing, and fragmentation of data packets.

### Data-link layer
The data-link layer is responsible for establishing and maintaining links between devices. It provides mechanisms for error detection, flow control, and addressing of data frames.

### Physical layer
The physical layer is responsible for the physical transmission of data over a network. It defines the electrical, mechanical, and functional characteristics of the network interface.

## ex01
### objective
Build this Network
![ex01](pics/ex01.jpg)

### components
6 computers
2 cross-over cables

The /24 in the notation indicates that 24 bits are allocated for the network portion of the address. In binary, this translates to:

-> the network is basically two computers each connected with a cross-over cable, which allows them to communicate directly without the need for a router or switch.
-> cross-over cable are cables used to connect similar devices while straight through cables are used to connect dissimmilar devices.


What is an RJ45?
To put it simply, an RJ45 is a type of connector commonly used for network cabling: the RJ stands for Registered Jack and the 45 is basically a listing number. It’s the component that terminates the Ethernet cable, allowing it to interface with networking hardware.
What is an RJ45 Connector Used For?

The primary use of an RJ45 connector is in Ethernet networking. These connectors are crucial for establishing wired connections between devices in local area networks (LANs), facilitating internet access, file sharing, and other network-based communications.
RJ45 connectors are also used in telephone systems and other forms of data communication, although their most recognized function remains in networking.

--> the first network is 192.168.1.3/24
Understanding the Network: 192.168.1.3/24

When analyzing an IP address such as 192.168.1.3/24, it is important to understand how to determine the subnet mask, total and usable addresses, and how the network and broadcast addresses are calculated. Below is a clear and detailed explanation suitable for documentation or report purposes.

  1. CIDR Notation and Subnet Mask

  The /24 in the notation indicates that 24 bits are allocated for the network portion of the address. In binary, this translates to:
  ```
  11111111.11111111.11111111.00000000
  ```
  which corresponds to the subnet mask:
  ```
  255.255.255.0
  ```
  2. calculate the total and usable ips
  The number of bits left for host devices is:
  ```
  32 total bits - 24 network bits = 8 host bits
  ```
  using the formula 2^(host bits) - 2 = usable ips
  ```
  2^8 - 2 = 256 - 2 = 254 usable ips
  ```

  3. Determien the block size.
  For further network calculations we first get the block size:
  ```
  block size = 256 - last octet of subnet mask
             = 256 - 0
             = 256
  ```
  4. calculate the network addresss:
  the network address is the first address in the subnet and cannot be assigned to a host. It is found by rounding the last octet of the ip down the nearest multiple of the block size:
  ```
  network address = ip address - (ip address % block size)
                  = 192.168.1.3 - (192.168.1.3 % 256)
                  = 192.168.1.0
  ```
  5. the broadcast address.
  the broadcast address is use to communicate with all the devices within the subnet.
  ```
  broadcast address =  network address + (block size - 1)
                  = 192.168.1.0 + (256 - 1)
                  = 192.168.1.255
  ```

  6. The ip range:
  the ip range is the range of ip addresses that can be assigned to devices within the subnet.
  ```
  ip range = network address + 1 to broadcast address - 1
          = 192.168.1.1 to 192.168.1.254
  ```

--> the second network is 192.168.13.82/29
- its subnet mask is 255.255.255.248
- number of usable ips is 6
- the Network address is 192.168.13.80
- the broadcast address is 192.168.13.87
- the ip range is 192.168.13.81 to 192.168.13.86

--> the third network is 192.168.13.254/29
- its subnet mask is 255.255.255.248
- number of usable ips is 6
- the Network address is 192.168.13.248
- the broadcast address is 192.168.13.255
- the ip range is 192.168.13.249 to 192.168.13.254

## ex02
-> the objective was to build this Network.
![ex02](pics/ex02.jpg)

### components
-build two networks
* the first network is a switch connected to 5 pcs using the straight coaxial cable
  - the ip is 192.168.1.5/29
  - the subnet mask is 255.255.255.248
  - the number of usable ips is 6
  - the network address is 192.168.1.0
  - the broadcast address is 192.168.1.7
  - the ip range is 192.168.1.1 to 192.168.1.6
* the second network is a hub connected to 5 pcs using the straight coaxial cable
  - the ip is 192.168.1.193/27
  - the subnet mask is 255.255.255.224
  - the number of usable ips is 30
  - the network address is 192.168.1.192
  - the broadcast address is 192.168.1.223
  - the ip range is 192.168.1.193 to 192.168.1.222

  1. Hub

  Definition:
  A hub is a basic networking device that connects multiple devices in a network. It simply broadcasts incoming data to all connected devices, regardless of the destination.

  Key Points / Uses:

  Works as a central connection point for devices in a LAN (Local Area Network).

  Used mainly in small, simple networks.

  Does not filter traffic; all devices see all data.

  OSI Layer:

  Layer 1 – Physical Layer: Deals with raw bit transmission.

  Hubs have no knowledge of MAC addresses or data packets.

  2. Switch

  Definition:
  A switch is a more advanced device that connects multiple devices in a network but sends data only to the device it is intended for.

  Key Points / Uses:

  Efficiently manages data traffic.

  Reduces network collisions.

  Can support VLANs and manage MAC address tables.

  Common in modern LANs, from small offices to large enterprises.

  OSI Layer:

  Layer 2 – Data Link Layer (most common): Uses MAC addresses to forward frames.

  Some switches (Layer 3 switches) also operate at Layer 3 – Network Layer, routing packets based on IP addresses.

  3. Key Differences: Hub vs Switch
  Feature	Hub	Switch
  OSI Layer	Layer 1 (Physical)	Layer 2 (Data Link), some Layer 3
  Data Handling	Broadcasts to all ports	Sends only to destination port
  Traffic Efficiency	Low (more collisions)	High (less collisions)
  MAC Address Table	None	Maintains MAC table
  Cost	Cheaper	More expensive
  Use Case	Small/simple networks	Modern networks

## ex03
-> the objective was to build this Network.
![ex03](pics/ex03.jpg)
### components

 - Switch
 - 6 pcs
 - a HTTPS server
 - a FTP server
 - a DNS server
 - a DHCP serve
 --> the main network is 192.168.1.0/24

 ### HTTP and HTTPS

 HTTP stands for HyperText Transfer Protocol. It is invented by Tim Berner. HyperText is the type of text that is specially coded with the help of some standard Markup language called HyperText Markup Language (HTML). HTTP provides a standard between a web browser and a web server to establish
 communication.

#### Characteristics of HTTP
HTTP is IP based communication protocol that is used to deliver data from server to client or vice-versa.
Any type of content can be exchanged as long as the server and client are compatible with it.
It is a request and response protocol based on client and server requirements.

HTTP request is a kind of message a client (in most cases, a web browser) sends to the server demanding some specific resources. It comprises of several elements like the request method (GET, POST and etc. ), the headers and occasionally the body carrying the data. This is the request part where the client outlines a request to the server and what they want.

 Http response is a message sent by the server to the client in response to an Http request. In simple terms, it has status code that describes the result of a request; header, which is information about the response; and the body, which is the actual response or an error message.
 How Does the HTTP Protocol Work?

 This means that the HTTP protocol uses a forms of a request and response operational mode. When a client wants to retrieve information, it uses http request to the servers as shown in the following stages.
 The request is received by the server and in the form of an HTTP response the server returns the data which the client requested or an error message.
 This takes place over the internet using port 80 by default, to assist in the identification of this protocol it is often referred to as the http or the hip protocol.

 What is HTTPS?

 HTTPS stands for Hyper Text Transfer Protocol Secure. HTTP Secure (HTTPS), could be a combination of the Hypertext Transfer Protocol with the SSL/TLS convention to supply encrypted communication and secure distinguishing proof of an arranged web server. HTTPS is more secure than HTTP because HTTPS is certified by the SSL(Secure Socket Layer). Whatever website you are visiting on the internet, if its URL is HTTP, then that website is not secure.

 Characteristics of HTTPS

HTTPS encrypts all message substance, including the HTTP headers and the request/response data. The verification perspective of HTTPS requires a trusted third party to sign server-side digital certificates.
HTTPS is presently utilized more frequently by web clients than the first non-secure HTTP, fundamentally to ensure page genuineness on all sorts of websites, secure accounts and to keep client communications.

 In short, both of these are protocols using which the information of a particular website is exchanged between the Web Server and Web Browser. But there are some differences between these two. A concise difference between HTTP and HTTPS is that HTTPS is much more secure compared to HTTP.
 How Does the HTTPS Protocol Work?

 HTTPS can be said to be similar to the HTTP only that it also provides a level of security. It first creates a connection between the client and server over SSL/TLS, which enhances security by encrypting the Client and server communication. When a client makes a request for a resource using the https then the server and the client agree on the encryption keys that will be used in encrypting the data that will be transmitted in that particular session. This makes sure that data being exchanged between them is encrypted and coded hence cannot be intercepted.

Differences between HTTP and HTTPS
* HTTPS is more secure than HTTP.
* HTTPS uses SSL/TLS to encrypt data.
* HTTPS requires a trusted third party to sign server-side digital certificates.
* HTTP works at the Application while HTTPS works at the Transport Layer.

##### how to configure the https server
-> we first assign a static ip address to the server(the one we chose as our https server)
- in this case the ip address is 192.168.1.99
- we then click on services then on https
- we then click on the https service and enable it
- we can also modify a page to display a custom message while we configure the server address to the DNS server.

### server
A server is a powerful computer or software system that provides services, data, or resources to other computers, called clients, over a network (like the internet or a local network).

What does a server do?
* Stores and manages data (like websites, apps, files, or databases)
* Processes client requests (e.g., loading a web page)
* Responds with the requested information or action

### DNS server
The DNS is a system of records of domain names and IP addresses that allows browsers to find the right IP address that corresponds to a hostname URL entered into it. When we try to access a website, we generally type in their domain names into the web browser. Web browsers however need to know the exact IP addresses to load content for the website. The DNS is what translates the domain names to the IP addresses so that the resources can be loaded from the website’s server.

##### how to configure the dns server
- we first assign a static ip address to the server(the one we chose as our dns server)
- in this case the ip address is 192.168.1.101
- we then click on services then on dns
- we then click on the dns service and enable it
- we then add the domain name to the name input and the we add its ip address to the ip address input.(this counts as a type record)
- we then click on the save button to save the changes.
--> types of DNS records
* A record: maps domain name to an IPv4 address
* AAAA record: maps domain name to an IPv6 address
* CNAME record: maps domain name to another domain name
* MX record: maps domain name to mail server
* TXT record: maps domain name to text data
* NS record: maps domain name to name server
* SOA record: maps domain name to start of authority record
* PTR record: maps ip address to domain name
* SPF record: maps domain name to sender policy framework record
* SRV record: maps domain name to service record

### DHCP server(Dynamic  host control Protocol)
A DHCP server is a server that assigns IP addresses to devices on a network. It is a type of server that is used to manage the IP addresses of devices on a network. DHCP servers are used to assign IP addresses to devices on a network, and to manage the IP addresses of devices on a network.

What does a DHCP server do?
* Assigns IP addresses to devices on a network
* Manages the IP addresses of devices on a network

##### configure
- we first assign a static ip address to the server(the one we chose as our dhcp server)
- in this case the ip address is 192.168.1.10w
- we then click on services then on dhcp.
- we conifure the name , the default-gateway, the dns-server(192.168.1.99) the start ip (192.168.1.1) the subnet mask (255.255.255.0) maximum number of users.
- we then click add and save.

### FTP server
An FTP server is a software application that runs on a computer to facilitate the transfer of files between a client and a server over a network using the File Transfer Protocol (FTP).

How FTP Works

FTP operates on a client-server model and utilizes two separate connections between the client and the server:

Control Connection (Port 21): This connection is established first and remains open for the duration of the session. It is used to send commands (like upload, download, change directory, or authentication details) from the client to the server and receive replies.

Data Connection (Port 20 in Active Mode, or a negotiated port in Passive Mode): This connection is opened only when data (the actual file content) needs to be transferred and is closed after the transfer is complete.

Protocols and the OSI Model

The primary protocol used for file transfer is FTP, which resides at the Application Layer (Layer 7) of the OSI model, as it provides services directly to the user's application (the FTP client).

FTP relies on the following protocols for underlying network communication:

Transmission Control Protocol (TCP): Used by both the control and data connections to ensure reliable, connection-oriented data delivery. TCP is found at the Transport Layer (Layer 4).

#### TCP & UDP
Both TCP and UDP are fundamental protocols operating at the Transport Layer (Layer 4) of the OSI model. They handle the communication between applications running on different hosts, taking data from the Application Layer and adding information to ensure it reaches the correct process.

Definitions

    Transmission Control Protocol (TCP): A connection-oriented protocol that establishes a reliable, error-checked, and ordered data stream between two applications. It is often described as a meticulous service that guarantees the delivery of every single byte of data in the correct sequence. It achieves this using a three-way handshake to set up a connection, and then uses acknowledgments (ACKs) and retransmission mechanisms.

User Datagram Protocol (UDP): A connectionless protocol that sends data packets, called datagrams, without first establishing a dedicated connection or guaranteeing delivery. It is a simple, fast, and lightweight protocol that prioritizes speed over reliability, often described as a "fire-and-forget" method.

Key Differences Between TCP and UDP

Both the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP) operate at the Transport Layer of the OSI model, but they offer distinct services.

TCP is a connection-oriented protocol, meaning it must first establish a formal connection with a three-way handshake before data transfer begins, and then formally tear it down. Its core feature is reliability: it guarantees in-order delivery of data segments, ensures data integrity through error-checking, and handles retransmission of any lost packets. To prevent the sender from overwhelming the receiver, TCP also implements flow control. Due to these numerous reliability mechanisms, TCP has higher overhead and is generally slower. It is the protocol of choice for applications where completeness is critical, such as Web browsing (HTTP/HTTPS) and File Transfer (FTP).

In contrast, UDP is a connectionless protocol, simply sending data packets, called datagrams, without any prior setup. It is unreliable because it offers no guarantee of delivery or data ordering; packets may be lost or arrive out of sequence, and there is no retransmission mechanism or built-in flow control. Its primary advantage is its speed and low overhead. This makes UDP ideal for applications where timely delivery is more important than absolute completeness, like Live Video/Audio Streaming, Online Gaming, and Voice over IP (VoIP).

### Port

A port in networking is a virtual endpoint or a logical address within an operating system that identifies a specific application or service running on a computer.

    Function: While an IP address identifies the device (the computer or host) on the network, the port number identifies the specific process or service (like a web server, an email client, or a game) running on that device that should receive the network traffic.

Location: Ports operate at the Transport Layer (Layer 4) of the OSI model, alongside TCP and UDP. Every TCP and UDP packet header contains a Source Port and a Destination Port number.

Addressing: A full network address, often called a socket, is a combination of the IP address and the port number (e.g., 192.168.1.1:80). This combination ensures that data not only reaches the correct computer but also gets handed off to the correct application waiting for it.

Port Numbers: Ports are 16-bit numbers, ranging from 0 to 65,535. They are divided into three ranges:

    Well-Known Ports (0–1023): Reserved for the most common public services (e.g., HTTP is port 80, HTTPS is port 443).

Registered Ports (1024–49151): Can be used by user applications or processes.

Dynamic/Private Ports (49152–65535): Used by clients for temporary outgoing sessions.

## ex04
-> the objective of this exercise is to build this network.
![ex04](pics/ex04.jpg)

### components
-1 router, 2 pcs( the pcs are connected to the router with a crossover cable)
This connection is possible because, in traditional Ethernet wiring standards, both PCs and routers are configured as MDI (Medium Dependent Interface) devices or Data Terminal Equipment (DTE). This means the dedicated Transmit (TX) pins on a PC's network card are wired identically to the Transmit (TX) pins on a router's interface port. When you connect two electrically identical MDI ports directly, the TX pins on one side connect to the TX pins on the other, and the Receive (RX) pins connect to the RX pins, preventing communication (a "talking to talking" and "listening to listening" scenario). A crossover cable solves this by physically swapping the TX and RX wire pairs between the two ends, ensuring that the signal transmitted by the PC successfully lands on the router's receive circuit, and vice-versa, thereby establishing a working link between the two similar devices.

#### What is a router?

A router is a device that connects two or more packet-switched networks or subnetworks. It serves two primary functions: managing traffic between these networks by forwarding data packets to their intended IP addresses, and allowing multiple devices to use the same Internet connection.

the main difference between a router and a switch is that a router is responsible for routing data packets between different networks, while a switch is responsible for routing data packets within a single network. A router uses routing protocols to determine the best path for data packets to travel between networks, while a switch uses MAC addresses to determine the best path for data packets to travel within a single network. A router also has a larger memory capacity and more advanced processing power than a switch, allowing it to handle more complex routing tasks and manage larger networks.

-> The routers are located in layer 3 of the OSI model.


#### Default Gateway:
  * The default gateway is the node that forwards the packet from the source to other networks when there is no routing information about the destination i.e. host (or router) does not know where the destination is present.
  * A default gateway is a route to which information is passed when the device does not know where the destination is present.
  * It is used when there is no routing information available about the destination.
  * It is a node that allows the communication of computers on different networks.
  * 'Default' here means the default route which is to be taken when the host does not know where the destination is.

##### configure
-> the first pc has been given a network of 192.168.1.2/30
- its subnet is 255.255.255.252
- its gateway is 192.168.1.1(the router entry point)
- the network is 192.168.1.0
- number of hosts is 2
- the pc is 192.168.1.2(we configure static ip address)

-> the second pc has been given a network of 192.168.2.2/30
- its subnet is 255.255.255.252
- its gateway is 192.168.2.1(the router entry point)
- the network is 192.168.2.0
- number of hosts is 2
- the pc is 192.168.2.2(we configure static ip address)

--> we click the router and enter the cli mode (use execution mode):
- we disable all helpful messages and enter the command 'enable' which enters to privileged mode
- we enter the command 'configure terminal' which enters to configuration mode
- we enter the command 'interface ethernet 0/0' which enters to interface mode
- we enter the command 'ip address 192.168.1.1 255.255.255.252' which configures the ip address of the router
- we enter the command 'no shutdown' which enables the interface(the first network)
- we enter the command 'exit' which exits from interface mode
- we enter the command 'interface ethernet 0/1' which enters to interface mode
- we enter the command 'ip address 192.168.2.1 255.255.255.252' which configures the ip address of the router
- we enter the command 'no shutdown' which enables the interface
- we enter the command 'exit' which exits from interface mode(the second network)

## ex05
--> the objective is to build this network
![ex05.jpg](pics/ex05.jpg)

### component
- 1 router , 2 switches , 10 PCs
--> the first network is 192.168.1.6/29
- the subnet mask is 255.255.255.248
- the network ip is 192.168.1.0
- number of usable hosts is 6
- ip range is 192.168.1.2-192.168.1.6
- default gateway is 192.168.1.1
--> the second network is 192.168.1.194/27
-  the subnet mask is 255.255.255.224
- the network ip is 192.168.1.192
- number of usable hosts is 30
- ip range is 192.168.1.194-192.168.1.222
- default gateway is 192.168.1.193

--> we configure the router (same way as above) each with the default gateway ip of the interface connected to the network.

## ex06
--> goal was to build this network
![ex06.jpg](pics/ex06.jpg)

#### components
- 2 routers, 2 pcs , 1 serial cable

A serial cable is used to connect two routers primarily because it implements a point-to-point, synchronous physical link that matches classic WAN interface requirements and provides predictable, controllable behavior for routing between distant networks. Key reasons and implications:

Technical reasons

    Point-to-point connectivity: Serial links create a direct, exclusive connection between two devices—ideal for WAN circuits where only two endpoints communicate.
    Synchronous transmission: Many serial WAN protocols (e.g., PPP, HDLC) use synchronous framing and clocking, which simplifies error detection, framing, and flow control over long-haul links.
    Layering and protocol support: WAN protocols over serial (PPP, HDLC, Frame Relay, etc.) provide features routers need: link-quality monitoring, authentication, multilink aggregation, and optional compression/encryption.
    Deterministic behavior: Serial links offer stable bandwidth and latency characteristics compared with shared-media LAN links; useful for predictable routing metrics and QoS.
    Physical and electrical compatibility: Historically, serial interfaces (V.35, RS-232, V.36/X.21, EIA/TIA-232) matched carrier demarcation equipment (modems, CSU/DSUs, leased-line interfaces) used for T1/E1, EIA circuits and analog/digital lines.

Operational and historical context

    Leased-line/WAN usage: Carriers historically provided leased serial circuits (T1, E1, analog) that required serial interfaces on routers and CSU/DSU conversion; a serial cable connects the router’s WAN interface to that equipment or directly to another router over a serial link.
    Simplicity for routing labs and point-to-point links: In labs or legacy deployments, a serial null-modem cable can directly join two routers’ serial ports to emulate a WAN link without extra hardware.
    Protocol features: PPP over serial adds link negotiation (LCP), authentication (PAP/CHAP), and IPCP for IP addressing—features not native to raw Ethernet.

When serial is chosen vs alternatives

    Use serial when you need a dedicated point-to-point WAN link, when the carrier provides a T1/E1/leased line, or when you require WAN-layer features (PPP, HDLC).
    Use Ethernet/IP/MPLS/Metro Ethernet when you need higher bandwidth, multipoint connectivity, or modern carrier Ethernet services; serial is now largely legacy for high-speed networks.

Practical note

    Today, serial physical links are less common in enterprise greenfield deployments—modern WANs use Ethernet, fiber, MPLS, or VPNs over broadband. Serial remains relevant for specific legacy circuits, lab exercises, and some carrier edge scenarios.

--> the first netwrok(pc1 - router 1) 192.168.1.2/24
- subnet mask: 255.255.255.0
- network address: 192.168.1.0
- gateway 192.168.1.1

--> the second network(pc2 - router 2) 192.168.2.1/24
- subnet mask: 255.255.255.0
- network address: 192.168.2.0
- gateway 192.168.2.1

--> the third network(router1 - router2) 10.10.0.1/30
- we configure the serial interface like any other interface
- subnet mask: 255.255.255.252
- network address: 10.10.0.0
- so router 1 gets 10.10.0.1 while router 2 gets 10.10.0.2

--> the main challenge was to configure the router so network 192.168.1.0 from router 1 can be discovered by router 2(same for the other network)
for router one we enter the router cli (configuration mode) and enter the following command
```
ip route <network ip> <subnet mask> <ip of entry interface>
```
the entry interface is the serial interface where the other router is connected
-- for router one it would be ip route 192.168.2.0 255.255.255.0 10.10.0.2
-- for router two it would be ip route 192.168.1.0 255.255.255.0 10.10.0.1

The routing table is a set of rules that directs where to send data packets over an IP network. Stored within the random access memory (RAM) of storage devices like network switches and routers, routing tables are individually unique, and each works as network address maps, storing source and destination IP addresses, routing information, and the addresses for default gateways. Ultimately, this helps computers communicate with other devices on different networks, expanding the distance of how networks can interact with each other.

How does a routing table work?

The goal of a routing table is to help routers determine the most effective routes for data packets. When sending data packets to host devices or other networks, routers consult routing tables to attain the IP addresses and best paths. Routing tables direct the packets to the appropriate neighboring router or next hop, eventually getting the packet to its intended destination. The entire process can happen incredibly fast, with a router consulting its routing table over a million times per second.

Network routing protocols help to keep routing tables updated and determine where data packets go. Two types of routing protocols exist to maintain the routing tables:

    Static routing protocols: Static routing protocols use routes that network administrators manually input, giving routers information on how to reach different network IDs within the more extensive network. This protocol works best with preconfigured routes on the same subnet but falters when communication expands beyond the subnet. Since routers do not share static routes, static routing can conserve overhead and bandwidth. Static routing protocols are typically best used in smaller networks, as every entry requires manual entry and updates to function.

    Dynamic routing protocols: Dynamic routing protocols, such as routing information protocol (RIP) and open shortest path first (OSPF), automatically create and maintain the routing table. They work automatically to communicate using routing protocols instead of a network administrator. It allows dynamic routing protocols to automatically change routes when better routes are available. This makes dynamic routing a better fit for larger organizations since automatic routing eliminates manual human interaction.

However, another protocol combines dynamic and static protocols since they connect interior autonomous systems to external networks.
Automatic routing

Automatic routing occurs when small networks contain one router. This low-level routing mechanism is helpful because it limits routing packets’ cycles and storage requirements. Automatic network routing involves fast packet switching, no-session awareness, and source routing through end nodes.

In automatic routing, the router handles all routing protocols without manually managing or maintaining the routing table. Automatic routing often works with networks that have a single router since they cannot add additional routing information that is not already available on the router.

Route determination

The routing table is important because it determines the network route data packets follow. Before route determination occurs, the packet is sent to the router and receives an IP address to help dictate the best route. The router receives this data packet and references it against the routing table, using the table to send the packet closer to its destination. Each router tries to get the package to the next hop, consulting the routing table of every router and trying to use the fewest hops. The packet reaches its destination when the destination IP address matches the network that receives it.
What comprises a routing table?

Data tables require specific information to send packets where they need to go. Let’s examine some of the information that comprises a routing table.

 * Network ID: A network ID contains the host ID and information on the route to the destination.

 * Destination address: A destination address is the final IP address for the device's network that requested the packet.

 * Subnet mask: A subnet mask is a 32-bit netmask that matches the destination address to the IP address, indicating whether or not the destination address is in the network. Subnetting can divide networks into smaller, more connected networks.

* Metric: The metric gives each route a value that determines some routes' preference level or priority over others. It does this by measuring how many hops each route contains to reach the intended destination, indicating the minimal number and most efficient route.

* Gateway: The gateway is the next hop available, revealing the routing information for the closest neighboring router to which the data packet forwards.


## ex07
--> the goal is to build this network
![ex07](pics/ex07.jpg)

### components
- two routers, 1 serial cable, 2 switches, 9pc and 1 laptop(pc)
--> the first network (5pcs -> switch -> router 1) 192.168.1.6/24
- the subnet mask is 255.255.255.0
- network Address 192.168.1.0
- number of hosts 254
- gateway 192.168.1.1

--> the second(like the first) 192.168.2.1/24
- the subnet mask is 255.255.255.0
- network Address 192.168.2.0
- number of hosts 254
- gateway 192.168.2.1

--> the third( router one to router two) 10.10.0.1/30
- the subnet mask is 255.255.255.252
- network Address 10.10.0.0
- number of hosts 2
- router one is 10.10.0.1 and the router two is 10.10.0.2

--> the ip route for the second network for the first is
```
ip route 192.168.2.0 255.255.255.0 10.10.0.2
```
and the first for the second
```
ip route 192.168.1.0 255.255.255.0 10.10.0.1
```

## ex08
--> the goal is to build this network
![ex08](pics/ex08.jpg)

### components
- 3 routers , 2 serial cables, 3 switches, 11pcs and 1 laptop(pc)
--> the first network (pcs -> switch -> router 1) 192.168.1.198/26
- the subnet mask is 255.255.255.192
- network Address 192.168.1.192
- number of hosts 62
- gateway 192.168.1.197

--> the second network( pcs -> switch -> router 2) 192.168.2.1/24
- the subnet mask is 255.255.255.0
- network Address 192.168.2.0
- number of hosts 254
- gateway 192.168.2.1

--> the third network( pcs -> switch -> router 3) 192.168.3.164/28
- the subnet mask is 255.255.255.240
- network Address 192.168.3.160
- number of hosts 14
- gateway 192.168.3.161

--> fourth network( router 1 to router 2) 10.10.0.1/30
- the subnet mask is 255.255.255.252
- network Address 10.10.0.0
- number of hosts 2

--> fifth network (router 2 to router 2) 10.10.1.2/30
- the subnet mask is 255.255.255.252
- network Address 10.10.1.0
- number of hosts 2

ip route for network 2 and 3 for network 1
```
ip route 192.168.2.0 255.255.255.0 10.10.0.2
ip route 192.168.3.160 255.255.255.240 10.10.0.2
```

ip route for network 1 for network 2
```
ip route 192.168.1.192 255.255.255.192 10.10.0.1
```

ip route for network 3 for network 2
```
ip route 192.168.3.160 255.255.255.240 10.10.1.2

```

ip route of network 1 and 2 for network 3
```
ip route 192.168.1.192 255.255.255.192 10.10.1.1
ip route 192.168.2.0 255.255.255.0 10.10.1.1
```
