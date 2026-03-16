import shutil

# Copy file
shutil.copy("sample.txt", "copy_sample.txt")

# Create backup
shutil.copy("sample.txt", "backup_sample.txt")

print("File copied and backup created.")