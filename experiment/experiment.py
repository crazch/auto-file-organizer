from pathlib import Path
import os

# List Files inside path
p = Path('/home/ray/Projects/python/file-organizer')
file = list(p.glob('**/*.py'))
print(file)

# Check if path is exists
path_true = Path('/home').exists()
print(path_true)

# Looping Through Directory and Files
directory = os.fsencode(p)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".py"):
        # print(os.path.join(directory, filename))
        continue
    else:
        continue

