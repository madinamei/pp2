import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

txt = "Hello world!"
x = re.search("^Hello", txt)

if x:
    print("YES! Starts with Hello")
else:
    print("No match")

txt = "Hello world"
x = re.search("world$", txt)

if x:
    print("YES! Ends with world")
else:
    print("No match")

txt = "My number is 123"
x = re.search("[0-9]+", txt)

if x:
    print("YES! Contains numbers")
else:
    print("No match")

txt = "hello"
x = re.search("^[a-z]+$", txt)

if x:
    print("YES! Only lowercase letters")
else:
    print("No match")