import re
import json

with open("raw.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

prices = re.findall(r'\d[\d ]*,\d{2}', text)

price_values = [
    float(p.replace(" ", "").replace(",", "."))
    for p in prices
]

products = re.findall(r'\d+\.\s*\n([^\n]+)', text)

total_amount = sum(price_values)

dt = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})', text)
date = dt.group(1) if dt else None
time = dt.group(2) if dt else None

pm = re.search(r'(Банковская карта|Наличные)', text)
payment_method = pm.group(1) if pm else "Unknown"

result = {
    "products": products,
    "prices": price_values,
    "calculated_total": round(total_amount, 2),
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(result, indent=4, ensure_ascii=False))