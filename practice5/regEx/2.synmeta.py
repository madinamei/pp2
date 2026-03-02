import re

txt = "The rain in Spain"

x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"

x = re.findall("\d", txt)
print(x)

txt = "hello planet"

x = re.findall("he..o", txt)
print(x)

txt = "hello planet"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

x = re.findall("he.*o", txt)

print(x)

x = re.findall("he.+o", txt)

print(x)

x = re.findall("he.?o", txt)

print(x)

x = re.findall("he.{2}o", txt)

print(x)

txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")