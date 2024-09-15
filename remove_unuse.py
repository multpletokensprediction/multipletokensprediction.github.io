import os
from pathlib import Path

# filename_list = [f.strip() for f in open('samples.txt').readlines()]
filename_list =[f.strip() for f in open('valle_samples.txt').readlines()]

dir = os.listdir("static/mos_samples")
root_dir = "static/mos_samples"
print(dir)
print(filename_list)
print(len(filename_list))
# for filename in filename_list:

# Remove unused file in gt
for filename in os.listdir(f"{root_dir}/vallef8"):
    if filename not in filename_list:
        os.remove(f"{root_dir}/vallef8/{filename}")
