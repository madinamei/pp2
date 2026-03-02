import re
import json

with open ("raw.txt" , "r" , encoding = "utf-8") as f:
    text = f.read()

result = {
    "products": products,
    "prices": price_values,
    "calculated_total": round(total_amount, 2),
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(result, indent=4, ensure_ascii=False))