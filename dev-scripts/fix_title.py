import sys
import re

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Replace the text loop HTML
    pattern = r'<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;">\s*<span style="color: #FFFFFF;">Explore</span>\s*<span style="color: #F80612;">Premium Templates</span>\s*</div>'
    replacement = r'''<span style="color: #FFFFFF;">Explore</span> <span style="color: #F80612;">Premium Templates</span>'''
    content = re.sub(pattern, replacement, content)

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Fixed {filename}")

process_file('products/index.html')
process_file('products.html')

