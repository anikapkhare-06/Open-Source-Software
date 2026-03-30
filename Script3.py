# Script 3: Disk and Permission Auditor

import os

DIRS = ["/etc", "/var/log", "/home", "/usr/bin", "/tmp"]

print("Directory Audit Report")
print("----------------------")

for d in DIRS:
    if os.path.exists(d):
        size = os.popen(f"du -sh {d} 2>/dev/null").read().split()[0]
        perms = os.popen(f"ls -ld {d}").read().split()
        print(f"{d} => Permissions: {perms[0]} Owner: {perms[2]} | Size: {size}")
    else:
        print(f"{d} does not exist")

# Software config check (example Python)
config_path = "/etc/python3"

if os.path.exists(config_path):
    print(f"\nConfig Found: {config_path}")
    os.system(f"ls -ld {config_path}")
else:
    print("\nConfig directory not found")
