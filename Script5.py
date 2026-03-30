# Script 5: Open Source Manifesto Generator

import datetime
import getpass

print("Answer 3 questions:\n")

tool = input("1. Tool you use daily: ")
freedom = input("2. Freedom means: ")
build = input("3. What will you build: ")

date = datetime.datetime.now().strftime("%d %B %Y")
filename = f"manifesto_{getpass.getuser()}.txt"

with open(filename, "w") as f:
    f.write(f"Date: {date}\n\n")
    f.write(f"I use {tool} daily.\n")
    f.write(f"For me, freedom means {freedom}.\n")
    f.write(f"I want to build {build} and share it openly.\n")
    f.write("I believe in open-source philosophy.\n")

print(f"\nManifesto saved in {filename}")

with open(filename, "r") as f:
    print(f.read())
