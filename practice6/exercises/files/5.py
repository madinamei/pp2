import os

filename = "copy_sample.txt"

# Safe delete
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted safely.")
else:
    print("File does not exist.")