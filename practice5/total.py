import re

with open ("raw.txt" , "r" , encoding = "utf-8") as f:
    text = f.readlines()

for i in range(len(text)):
    if text[i].strip() == "ИТОГО:":
        total = text[i + 1].strip()
        print("TOTAL:", total)
