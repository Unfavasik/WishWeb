import sys
import re

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Replace the text loop HTML
    pattern = r'<div class="text-loop-container" id="templates-text-loop">[\s\S]*?<div class="text-loop-cursor"></div>\s*</div>'
    replacement = r'''<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;">
            <span style="color: #FFFFFF;">Explore</span>
            <span style="color: #F80612;">Premium Templates</span>
          </div>'''
    content = re.sub(pattern, replacement, content)
    
    # Remove initTextLoop() call
    content = re.sub(r'\binitTextLoop\(\);\s*', '', content)

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Fixed {filename}")

process_file('products/index.html')
process_file('products.html')

