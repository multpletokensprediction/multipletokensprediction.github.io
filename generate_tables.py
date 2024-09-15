import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

src_dir = Path("static/topk4_samples")

# model_order = ["gt", "uslm1", "uslm8"]
# model_order = ["gt", "vallef1", "vallef8"]
model_order = ["TOPK3", "TOPK5", "TOPK7", "TOPK9", "TOPK15", "TOPK25"]


# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Load the template
template = env.get_template('table.html')

sample_name_list = [t.strip() for t in open("topk4_samples.txt").readlines()][::-1]

data = []
for sample_name in sample_name_list[:5]:
    row = []
    for model in model_order:
        sample_path = src_dir/model/sample_name
        row.append({"model": model, "path": sample_path})
    data.append(row)
# # Example model data
# data = [
#     {'name': 'Model 1', 'audio_file': 'audio/model1.mp3'},
#     {'name': 'Model 2', 'audio_file': 'audio/model2.mp3'},
#     {'name': 'Model 3', 'audio_file': 'audio/model3.mp3'},
# ]

# Render the template with model data
output = template.render(data=data)

# Write the generated HTML to a file
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, 'table.html'), 'w') as f:
    f.write(output)

print("Static HTML generated!")
