# Script 2: FOSS Package Inspector

import os

PACKAGE = input("Enter package name: ")

# Check installation
result = os.system(f"dpkg -s {PACKAGE} > /dev/null 2>&1")

if result == 0:
    print(f"{PACKAGE} is installed.")
    os.system(f"dpkg -s {PACKAGE} | grep -E 'Version|Maintainer|Description'")
else:
    print(f"{PACKAGE} is NOT installed.")

# Case-like logic
if PACKAGE == "apache2":
    print("Apache: the web server that built the internet")
elif PACKAGE == "mysql-server":
    print("MySQL: backbone of many applications")
elif PACKAGE == "python3":
    print("Python: community-driven programming language")
elif PACKAGE == "vlc":
    print("VLC: plays everything freely")
else:
    print("Unknown package")
