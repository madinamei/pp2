import re
import json

with open ("raw.txt" , "r" , encoding = "utf-8") as f:
    text = f.read()

payment_pattern = r'(Банковская карта|Наличные)'
payment_match = re.search(payment_pattern, text)

payment_method = payment_match.group(1) if payment_match else "Unknown"
