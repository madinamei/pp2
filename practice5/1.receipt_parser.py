import re
import json

with open ("raw.txt" , "r" , encoding = "utf-8") as f:
    text = f.read()

pattern = r'(?<!\d)(?:\d{1,3}(?:[ \u00A0]\d{3})*|\d+),\d{2}(?!\d)'
prices = re.findall(pattern , text)

print("Все цены:" , " ".join(prices))
print("Найдено цен:",len(prices))
