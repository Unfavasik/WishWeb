import os
import re

def px_to_rem(match):
    px_str = match.group(1)
    px_val = float(px_str)
    if px_val <= 2:
        return match.group(0)
    rem_val = px_val / 16.0
    rem_str = f"{rem_val:g}rem"
    return match.group(0).replace(px_str + "px", rem_str)

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Match tailwind [12px], [12.5px]
    content = re.sub(r'\[([0-9.]+)px\]', px_to_rem, content)
    
    def style_replacer(m):
        style_content = m.group(0)
        return re.sub(r'(?<=[:\s])([0-9.]+)px\b', px_to_rem, style_content)
        
    content = re.sub(r'<style[^>]*>.*?</style>', style_replacer, content, flags=re.DOTALL)
    content = re.sub(r'style="[^"]*"', style_replacer, content)

    with open(filename, 'w') as f:
        f.write(content)
        
html_files = ["index.html", "products.html", "product-detail.html"]
for f in html_files:
    if os.path.exists(f):
        process_file(f)
        print("Processed", f)
