import re
import json

with open ("raw.txt" , "r" , encoding = "utf-8") as f:
    text = f.read()
datetime_pattern = r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})'
datetime_match = re.search(datetime_pattern, text)

date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None