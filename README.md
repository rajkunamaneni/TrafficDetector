# Traffic Detector for Network Intrusion
**Authors: Georgy Zaets, Raj Kunamaneni, Guneet Mummaneni, Jared Pugh**

![TrafficDetector Logo](/extras/TrafficDetectorLogo.png)

## Introduction:
In the age of pervasive computer security threats, safeguarding networks against eavesdropping and snooping attacks is more crucial than ever. This repository aims to address the challenges faced by non-tech-savvy individuals who struggle to comprehend and employ traditional open-source network security tools. Our goal is to create an extensible network toolkit directory that is accessible to all users, providing a lightweight yet effective solution for detecting and mitigating eavesdropping attacks. The toolkit was developed to run on Raspberry Pi Version 3B+ and later models, as well as any Debian-based machine with equivalent or better hardware.

### Challenges in Eavesdropping Attacks:
Eavesdropping attacks can vary in form, including snooping and man-in-the-middle attacks. These attacks are becoming more sophisticated over time, often outpacing the defensive capabilities of traditional network security tools. We propose a lightweight solution that can effectively mitigate such attacks with easy-to-understand notifications for users.

### Problem with Anti-Virus Software and Our Solution:
Anti-virus software, though effective against viruses, can significantly slow down system performance when running network scans. Our solution involves shifting this workload to a dedicated network machine, like a Raspberry Pi, acting as a DNS server to monitor network traffic and alert users of any unauthorized data transfers.

## :wrench: Installation
### 1) Clone the Repository:

```bash
git clone https://github.com/rajkunamaneni/TrafficDetector.git
```

### 2) Open the Terminal and run the `start.sh` bash script. This bash script has been provided to enable the installation of various programs and tools used to log information that is processed by the open-source security toolkit. Sudo permissions are required to run the script. The script will prompt the user to enter their password to proceed with the installation. 

```bash
chmod +x start.sh
./start.sh
```

## :zap: How to run 

### `Snort`

Snort is an open-source network intrusion prevention system and intrusion detection system. It's capable of performing real-time traffic analysis and packet logging on IP networks. Snort is used to detect and prevent attacks such as buffer overflows, stealth port scans, CGI attacks, SMB probes, and OS fingerprinting attempts. Snort can be used to monitor network traffic and detect suspicious activity. 


Snort should already be installed if you have run the `start.sh` script. If not, you can install it manually using the following command:

```bash
sudo apt-get install snort
```

Configure Snort for your network. Edit the Snort configuration file:

```bash
sudo nano /etc/snort/snort.conf
```

Set the HOME_NET variable to your local network. For example, if your local network is 192.168.1.0/24, you would change the line to:

```bash
ipvar HOME_NET 192.168.1.0/24
```

Save and close the file.

To run Snort in console mode and see the network traffic:

```bash
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
```

Replace eth0 with your network interface name.

### `Wireshark`

Wireshark is a network protocol analyzer that can capture and display the data traveling back and forth on a network. It is used to troubleshoot network problems, analyze network traffic, and detect network intrusions. In regards to the toolkit's functionality, Wireshark can be used to capture packets and analyze them for suspicious activity. The command line version of Wireshark, Tshark, can be used to capture packets and save them to a file

Wireshark is included in the ```start.sh``` script. To install it manually:

```bash
sudo apt-get install wireshark
```

Tshark is a command-line version of Wireshark. It can be used to capture packets and save them to a file. It can also be used to read packets from a file and display them on the screen. Tshark is included in the ```start.sh``` script. To install it manually:

```bash
sudo apt-get install tshark
```

To capture packets using Wireshark:

```bash
sudo tshark -i eth0 -w ~/capture.pcap
```
Replace eth0 with your network interface and specify your desired output file.

### `Nmap`

Nmap is a free and open-source utility for network discovery and security auditing. It can be used to scan networks for open ports, detect operating systems, and find vulnerabilities. 

Nmap should be installed with the ```start.sh``` script. To install it manually:

```bash
sudo apt-get install nmap
```

Scanning a network using NMap allows you to find open ports and detect operating systems. This is useful for finding vulnerabilities in your network. It can also be used to find the IP address of a host on your network. For security of your network, you can use NMap to scan for open ports and close them if necessary. 

To scan a network or a host:

```bash
nmap [target]
```

Replace [target] with the IP address or hostname of your target. For example:

```bash
nmap 192.168.1.1
```

This procedure will scan the network and display the open ports and operating system of the target. The [target] can also be a hostname, such as google.com. Scanning a network or host can take a long time, so it is recommended to use the -T4 flag to speed up the scan. The flag -T4 will set the timing template to aggressive, in other words it will speed up the scan. For example using -T4 on google.com:

```bash
nmap -T4 google.com
```
 
This will speed up the scan and display the results faster. The -T4 flag can be used with any scan.

### `FPing`

FPing is a free and open-source utility for network discovery and security auditing. It is faster than `ping` because it sends multiple ICMP packets at once. It can be used to scan networks for open ports, detect operating systems, and find vulnerabilities. 

FPing should be installed with the ```start.sh``` script. To install it manually:

```bash
sudo apt-get install fping
```

To run FPing:

```bash
fping [target]
```

Replace [target] with the IP address or hostname of your target. For example:

```bash
fping google.com
```

This procedure will ping the target and display the results. The [target] can also be an IP address. The output of FPing is much simpler than `ping` because it whether or not the target is reachable. It does not display the round trip time or the number of packets sent and received.

## 📌 Note:

Ensure you have the necessary permissions and are compliant with legal regulations when using these tools.
Regularly update the tools to get the latest security features and bug fixes.

For detailed usage and advanced configurations, consult the respective man pages or online documentation:

[Tshark](https://www.wireshark.org/docs/man-pages/tshark.html)

[Snort](https://www.snort.org/documents)

[NMap](https://nmap.org/docs.html)

[FPing](https://fping.org/) 

## Hardware and Other Prerequisites:

Raspberry Pi Requirements: A Raspberry Pi (version 3B+ or later) is recommended. We recommend installing Ubuntu Server LTS, which can be downloaded from the Raspberry Pi Imager Software. This version is more resource-efficient compared to Ubuntu Desktop because it does not bloat the storage with GUI files.

However, Raspberry Pi is NOT required! Any PC that can run the latest Ubuntu Server LTS is valid. We recommend the following minimum requirements for the machine:

CPU: Intel Pentium or AMD Athlon dual-core processor (e.g., Intel Pentium Gold G6400 or AMD Athlon 3000G)

Motherboard: Any motherboard with onboard Wi-Fi/Ethernet or a dedicated External Wi-Fi Card

Memory (RAM): 4GB DDR4 RAM recommended (DDR3 also valid)
    
Storage: An 8 GB SD card should suffice, the bigger the better as the tool grows over time.

Access to AWS hosting is also needed. In the future, there is potential to expand to other well-known hosting platforms (i.e. DigitalOcean, Cloudflare, etc.).

## Current Progress:

Development of Bash Scripts: Created scripts for automating the installation of tools like SNORT and Wireshark.

SNORT Installation and Configuration: Successfully installed and tested SNORT for monitoring network traffic as well as set up AWS notifaction messaging.

Network Attack Simulations: Conducted simulations like DDOS and Port Scanning to test SNORT's detection capabilities.

## Future Directions:

Additional Tools: Looking into integrating other security tools to complement the current library.

Optimization for Raspberry Pi: Focusing on performance and resource efficiency for specifically Raspberry Pi devices.

User Experience Enhancement: Developing a simple, intuitive interface with clear notifications for security incidents as well as improving the UI for AWS notifications.

Data Presentation: Improvements to the AWS messaging format with a more user-friendly design, while still providing easy to integral information about the security of the network.

Better Hardware Support: Expanding to support other hardware platforms like RISC-V.

Reducing User Effort: Automating the installation process to reduce the amount of manual work required.

## Configurability:

As an open source toolkit, the start.sh shell script was designed to be easily configurable. To implement new programs and utilities into the toolkit to optimize security coverage, one needs to only insert lines indicating tools to be installed. This enables simplicity with little overhead in terms of mental effort.

Users can customize the shell script to provide more information regarding the status of the installation process. Flags to suppress information and prompts can be disabled if the user desires.

For more information, users can check man pages for Unix-based systems to learn the fine details of all commands.
