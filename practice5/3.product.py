import re

with open ("raw.txt" , "r" , encoding = "utf-8") as f:
    text = f.readlines()

for i in range(len(text)):
    tex = text[i].strip()
    if re.match(r"^\d+\.$" , tex):
        product = text[i+1].strip()
        print(product)
        print("Всего товаров:",len(product))