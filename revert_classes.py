import os
import re

def rem_to_px(match):
    rem_str = match.group(1)
    rem_val = float(rem_str)
    px_val = rem_val * 16.0
    px_str = f"{px_val:g}px"
    return match.group(0).replace(rem_str + "rem", px_str)

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Match tailwind [12.5rem]
    content = re.sub(r'\[([0-9.]+)rem\]', rem_to_px, content)

    with open(filename, 'w') as f:
        f.write(content)
        
html_files = ["index.html", "products.html", "products/index.html", "products/detail.html"]
for f in html_files:
    if os.path.exists(f):
        process_file(f)
        print("Reverted", f)

