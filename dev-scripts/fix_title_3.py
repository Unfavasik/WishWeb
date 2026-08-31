import sys
import re

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    pattern = r'<h1 class="hero-title" style="margin-bottom: 16px; width: 100%; max-width: 100%; text-align: center; min-width: 0;">\s*<span style="color: #FFFFFF; font-size: 0.85em; font-weight: 600; opacity: 0.9;">Explore</span>\s*<span style="color: #F80612; font-size: 1.15em; text-shadow: 0 4px 32px rgba\(248,6,18,0\.4\);">Premium Templates</span>\s*</h1>'
    replacement = r'''<h1 class="hero-title" style="margin-bottom: 16px; width: 100%; max-width: 100%; text-align: center; min-width: 0; display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 8px 12px; line-height: 1.2;">
          <span style="color: #FFFFFF; font-weight: 600;">Explore</span> 
          <span style="color: #F80612; text-shadow: 0 4px 32px rgba(248,6,18,0.4);">Premium Templates</span>
        </h1>'''
    content = re.sub(pattern, replacement, content)

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Fixed {filename}")

process_file('products/index.html')
process_file('products.html')

