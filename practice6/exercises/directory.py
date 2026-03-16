import os
import shutil
from pathlib import Path

# Create folders
Path("workspace/files/texts").mkdir(parents=True, exist_ok=True)

# Create sample file
with open("workspace/example.txt", "w") as f:
    f.write("Example text")

# List directory
print(os.listdir("workspace"))

# Find txt files
for file in Path("workspace").rglob("*.txt"):
    print("Found:", file)

# Copy file
shutil.copy("workspace/example.txt",
            "workspace/files/texts/example.txt")

# Move file
shutil.move("workspace/example.txt",
            "workspace/moved_example.txt")