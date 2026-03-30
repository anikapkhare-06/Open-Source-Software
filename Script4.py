# Script 4: Log File Analyzer

import sys

if len(sys.argv) < 2:
    print("Usage: python script4.py <logfile> [keyword]")
    sys.exit()

logfile = sys.argv[1]
keyword = sys.argv[2] if len(sys.argv) > 2 else "error"

count = 0

try:
    with open(logfile, "r") as file:
        lines = file.readlines()

        if len(lines) == 0:
            print("File is empty. Retry later.")
            sys.exit()

        for line in lines:
            if keyword.lower() in line.lower():
                count += 1

    print(f"Keyword '{keyword}' found {count} times")

    print("\nLast 5 matching lines:")
    matches = [line for line in lines if keyword.lower() in line.lower()]
    for line in matches[-5:]:
        print(line.strip())

except FileNotFoundError:
    print("File not found.")
