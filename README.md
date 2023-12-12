# Traffic Detector for Network Intrusion
**Authors: Georgy Zaets, Raj Kunamaneni, Guneet Mummaneni, Jared Pugh**

### Introduction:
In the age of pervasive computer security threats, safeguarding networks against eavesdropping and snooping attacks is more crucial than ever. This repository aims to address the challenges faced by non-tech-savvy individuals who struggle to comprehend and employ traditional open-source network security tools. Our goal is to create an extensible network toolkit directory that is accessible to all users, providing a lightweight yet effective solution for detecting and mitigating eavesdropping attacks. The toolkit was developed to run on Raspberry Pi Version 3B+ and later models, as well as any Debian-based machine with equivalent or better hardware.

### Repository Structure:
```
code/: 
```
Clone the Repository:

```bash
git clone https://github.com/rajkunamaneni/TrafficDetector.git
```

### Hardware and Other Prerequisites:

Raspberry Pi Requirements: A Raspberry Pi (version 3B+ or later) is recommended. We recommend installing Ubuntu Server LTS, which can be downloaded from the Raspberry Pi Imager Software. This version is more resource-efficient compared to Ubuntu Desktop because it does not bloat the storage with GUI files.

However, Raspberry Pi is NOT required! Any PC that can run the latest Ubuntu Server LTS is valid. We recommend the following minimum requirements for the machine:

CPU: Intel Pentium or AMD Athlon dual-core processor (e.g., Intel Pentium Gold G6400 or AMD Athlon 3000G)

Motherboard: Any motherboard with onboard Wi-Fi/Ethernet or a dedicated External Wi-Fi Card

Memory (RAM): 4GB DDR4 RAM recommended (DDR3 also valid)
    
Storage: An 8 GB SD card should suffice, the bigger the better as the tool grows overtime.

Access to AWS hosting is also needed. In the future, there is potential to expand to other well-known hosting platforms (i.e. DigitalOcean, Cloudflare, etc.).

### Future Directions:

A bash script (start.sh) has been provided to enable the installation of various programs and tools used to log information that is processed by the open-source security toolkit.

Run the bash script as follows:

```bash
chmod +x start.sh
./start.sh
```

The programs should install without interference and minimal user input.
