import sys
import re

def extract_footer(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    # Extract the footer tag and its content
    match = re.search(r'(<footer\b[^>]*>.*?</footer>)', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def replace_footer(filename, new_footer):
    with open(filename, 'r') as f:
        content = f.read()
        
    pattern = r'<footer\b[^>]*>.*?</footer>'
    new_content = re.sub(pattern, new_footer, content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Updated footer in {filename}")

new_footer = extract_footer('index.html')
if new_footer:
    replace_footer('products.html', new_footer)
    replace_footer('products/index.html', new_footer)
else:
    print("Could not find footer in index.html")
