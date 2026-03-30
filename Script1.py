# Script 1: System Identity Report
# Author: Himanshu Chaubey
# Course: Open Source Software

import os
import platform
import getpass
from datetime import datetime

# --- Variables ---
STUDENT_NAME = "Himanshu Chaubey"
SOFTWARE_CHOICE = "Python"

# --- System Info ---
kernel = platform.release()
user = getpass.getuser()
home = os.path.expanduser("~")

uptime = os.popen("uptime -p").read().strip()
distro = platform.system() + " " + platform.version()
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- Display ---
print("=" * 40)
print(f"Open Source Audit — {STUDENT_NAME}")
print("=" * 40)
print(f"Kernel  : {kernel}")
print(f"User    : {user}")
print(f"Home    : {home}")
print(f"Uptime  : {uptime}")
print(f"Distro  : {distro}")
print(f"Date    : {date_time}")
print("License : GNU General Public License (GPL)")
