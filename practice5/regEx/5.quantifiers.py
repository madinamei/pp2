import re

txt = "My code is 123"
x = re.search(r"\d{3}", txt)

if x:
    print("Found exactly 3 digits in a row")
else:
    print("No match")

txt = "caaandy"
x = re.search(r"a{2,}", txt)

if x:
    print("Found 2 or more 'a'")
else:
    print("No match")

txt = "Year 2025"
x = re.search(r"\d{2,4}", txt)

if x:
    print("Found 2 to 4 digits")
else:
    print("No match")

re.search(r"\b[a-zA-Z]{5}\b", "Hello world")

re.search(r"o{1,3}", "cooool")