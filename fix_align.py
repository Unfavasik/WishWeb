import sys
import re

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Replace the text loop HTML
    pattern = r'<h1 class="hero-title" style="margin-bottom: 16px; width: 100%; max-width: 100%; text-align: center; min-width: 0; display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 8px 12px; line-height: 1\.2;">\s*<span style="color: #FFFFFF; font-weight: 600;">Explore</span>\s*<span style="color: #F80612; text-shadow: 0 4px 32px rgba\(248,6,18,0\.4\);">Premium Templates</span>\s*</h1>'
    replacement = r'''<h1 class="hero-title" style="margin-bottom: 16px; width: 100%; max-width: 100%; text-align: left; min-width: 0; display: flex; flex-wrap: wrap; justify-content: flex-start; align-items: center; gap: 8px 12px; line-height: 1.2;">
          <span style="color: #FFFFFF; font-weight: 600;">Website</span> 
          <span style="color: #F80612; text-shadow: 0 4px 32px rgba(248,6,18,0.4);">Templates</span>
        </h1>'''
    content = re.sub(pattern, replacement, content)
    
    # We also need to left align hero-description if it was centered in css.
    # Wait, in CSS `.hero-description` might not be centered. Let's see if there is `text-align: center`.
    # `.hero-description` had: font-size, line-height, color, margin, max-width.
    # We might just add an inline style `text-align: left;` to be safe.
    content = content.replace('<p class="hero-description">', '<p class="hero-description" style="text-align: left;">')

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Fixed {filename}")

process_file('products/index.html')
process_file('products.html')

