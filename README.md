# Basic Network Sniffer

## Overview

This project is a Python-based Network Sniffer developed as part of the CodeAlpha Cyber Security Internship. The program captures network packets and displays useful information such as source and destination IP addresses, protocols, port numbers, and packet payloads.

## Features

* Captures live network packets
* Displays Source IP Address
* Displays Destination IP Address
* Identifies protocols such as TCP, UDP, and ICMP
* Displays Source and Destination Port Numbers
* Extracts packet payload information
* Helps understand network communication and packet structures

## Technologies Used

* Python 3
* Scapy Library
* Npcap (Windows)

## Installation

1. Install Python 3.
2. Install Scapy:

pip install scapy

3. Install Npcap for packet capturing on Windows.

## Usage

Run the following command:

python network_sniffer.py

The program will capture network packets and display packet details in the terminal.

## Sample Output

* Source IP: 172.16.161.78
* Destination IP: 20.42.65.84
* Protocol: TCP
* Source Port: 52013
* Destination Port: 443
* Payload: Packet Data

## Learning Outcomes

Through this project, I learned:

* Basics of network packet analysis
* TCP/IP communication
* Packet sniffing using Scapy
* Network protocols and ports
* Traffic monitoring techniques

## Disclaimer

This project is developed strictly for educational and ethical purposes. It should only be used on authorized networks and systems.
