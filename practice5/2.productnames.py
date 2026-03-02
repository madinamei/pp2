import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

product_pattern = r'\d+\.\s*\n([^\n]+)'
products = re.findall(product_pattern, text)

