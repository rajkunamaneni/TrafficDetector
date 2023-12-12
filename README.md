# Traffic Detector for Network Intrusion
**Authors: Georgy Zaets, Raj Kunamaneni, Guneet Mummaneni, Jared Pugh**

### Introduction:
In the age of pervasive computer security threats, safeguarding networks against eavesdropping and snooping attacks is more crucial than ever. This repository aims to address the challenges faced by non-tech-savvy individuals who struggle to comprehend and employ traditional open-source network security tools. Our goal is to create an extensible network toolkit directory that is accessible to all users, providing a lightweight yet effective solution for detecting and mitigating eavesdropping attacks. The toolkit was developed to run on Raspberry Pi Version 3B+ and later models, as well as any Debian based machine with equivalent or better hardware.

### Repository Structure:
```
code/: 
```
Clone the Repository:

```bash
git clone https://github.com/rajkunamaneni/TrafficDetector.git
```

### Hardware and Other Prerequisites:

One should be in possession of a Raspberry Pi (version 3). One can install Ubuntu Server using the Raspberry Pi's imaging software. This can be found here: https://www.raspberrypi.com/software/. Ubuntu Server is a lightweight framework compared to other alternatives, including Ubuntu Desktop.
Other prerequisites would include a SD card (32 GB is more than enough). An SD card with a fraction of the storage will also suffice.

Access to AWS hosting is also needed. In the future, there is potential to expand to other well-known hosting platforms (i.e. DigitalOcean, Cloudflare, etc.).

### Future Directions:

A bash script (start.sh) has been provided to enable the installation of various programs and tools used to log information that is processed by the open-source security toolkit.

Run the bash script as follows:

```bash
chmod +x start.sh
./start.sh
```

The programs should install without interference and minimal user input.

