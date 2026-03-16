import os
if os.path.exists("demofil.txt"):
  os.remove("demofil.txt")
else:
  print("The file does not exist")