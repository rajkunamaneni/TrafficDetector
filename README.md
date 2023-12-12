# Traffic Detector for Network Intrusion
**Authors: Georgy Zaets, Raj Kunamaneni, Guneet Mummaneni, Jared Pugh**

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

### 2) Open the Terminal and run the bash script as follows:
```bash
chmod +x start.sh
./start.sh
```
This bash script (start.sh) has been provided to enable the installation of various programs and tools used to log information that is processed by the open-source security toolkit.

## :zap: How to run 

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

## Configurability:

As an open source toolkit, the start.sh shell script was designed to be easily configurable. To implement new programs and utilities into the toolkit to optimize security coverage, one needs to only insert lines indicating tools to be installed. This enables simplicity with little overhead in terms of mental effort.

Users can customize the shell script to provide more information regarding the status of the installation process. Flags to suppress information and prompts can be disabled if the user desires.

For more information, users can check man pages for Unix-based systems to learn the fine details of all commands.
