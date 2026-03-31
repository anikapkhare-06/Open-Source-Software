## Open Source Audit Project

## Student Details

* **Name:** Anika Khare
* **Registration Number:** 24BAI10059
* **Course:** Open Source Software


## Chosen Software

**Python Programming Language**


##  Project Overview

This project focuses on analyzing Python as an open-source software. It explores its origin, philosophy, licensing, and role in the Linux ecosystem.

Additionally, five scripts have been developed to demonstrate practical Linux and open-source concepts such as system information, package inspection, disk auditing, log analysis, and user interaction.


#  System Requirements

Ensure your system meets the following requirements:

* Linux Operating System (Ubuntu recommended)
* Bash Shell
* Python 3 installed
* Basic Linux command support


#  Environment Setup

## Step 1: Verify Python Installation

Run the following command:

```bash
python3 --version
```

If Python is not installed, install it using:

```bash
sudo apt update
sudo apt install python3
```


## Step 2: Verify Required Tools

Ensure the following commands are available:

```bash
dpkg --version
ls --version
du --version
```

If not, update your system packages:

```bash
sudo apt update && sudo apt upgrade
```


#  Project Setup

## Step 1: Clone the Repository

```bash
git clone <https://github.com/anikapkhare-06/Open-Source-Software>
```

## Step 2: Navigate to Project Directory

```bash
cd oss-audit-[24BAI10059]
```


#  Configuration

Before running the scripts, ensure:

* All `.sh` files are present in the same directory
* Python 3 is properly installed
* Execution permissions are granted

Grant permissions using:

```bash
chmod +x script1.sh script2.sh script3.sh script4.sh script5.sh
```


#  Execution Guide

##  Script 1 — System Identity Report

```bash
./script1.sh
```

**Output:**

* Kernel version
* Current user
* System uptime
* Date and time


##  Script 2 — FOSS Package Inspector

```bash
./script2.sh
```

**Input:**

* Package name (e.g., python3, apache2)

**Output:**

* Installation status
* Version and description


##  Script 3 — Disk and Permission Auditor

```bash
./script3.sh
```

**Output:**

* Directory size
* Permissions
* Ownership details


##  Script 4 — Log File Analyzer

```bash
./script4.sh /var/log/syslog error
```

**Input:**

* Log file path
* Keyword (optional)

**Output:**

* Count of keyword occurrences
* Last 5 matching lines


##  Script 5 — Open Source Manifesto Generator

```bash
./script5.sh
```

**Input:**

* Three user responses

**Output:**

* A text file containing the generated manifesto


#  Project Structure

```
oss-audit-[24BAI10059]/
│
├── README.md
├── script1.sh
├── script2.sh
├── script3.sh
├── script4.sh
├── script5.sh
└── Project_Report.pdf
```


#  Important Notes

* These scripts are designed to run on a Linux system
* Ensure correct file paths are used (especially in Script 4)
* Python 3 must be installed before execution


#  Conclusion

This project provides a deeper understanding of open-source software and its practical implementation in a Linux environment. The scripts demonstrate automation, system monitoring, and user interaction, reflecting real-world applications of open-source tools.


   *Thank you for reviewing this project!*
