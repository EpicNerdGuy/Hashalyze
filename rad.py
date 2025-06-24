import os
import shutil

# Define your target structure
code_folder = "hashalyze"
dist_folder = "dist"

# Files that go into code folder
code_files = ["cli.py", "main.py", "setup.py"]

# Dist-type folders
dist_items = ["build", "__pycache__"]

# Move code files to code_folder
os.makedirs(code_folder, exist_ok=True)
for file in code_files:
    if os.path.exists(file):
        shutil.move(file, os.path.join(code_folder, file))
        print(f"Moved {file} → {code_folder}/")

# Move .egg-info and dist junk
os.makedirs(dist_folder, exist_ok=True)
for item in dist_items + [f for f in os.listdir() if f.endswith(".egg-info")]:
    if os.path.exists(item):
        shutil.move(item, os.path.join(dist_folder, item))
        print(f"Moved {item} → {dist_folder}/")

print("\n✅ Folder organized successfully.")
