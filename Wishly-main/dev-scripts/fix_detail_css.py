import sys
import re

with open('products/detail.html', 'r') as f:
    content = f.read()

pattern = r'/\* ==================================================\s*3\. BREADCRUMB & BACK LINK\s*================================================== \*/\s*\.breadcrumb-row \{[\s\S]*?\.back-btn-link:hover \{\s*color: #FFFFFF;\s*\}'

new_css = """/* ==================================================
       3. BREADCRUMB & BACK LINK
       ================================================== */
    .btn-back-home {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      height: 48px;
      max-height: 72px;
      padding: 0 20px;
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.15);
      background: rgba(255, 255, 255, 0.04);
      color: #F2F2F2;
      font-size: 16px;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.2s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    .btn-back-home:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.25);
    }"""

if re.search(pattern, content):
    content = re.sub(pattern, new_css, content)
    with open('products/detail.html', 'w') as f:
        f.write(content)
    print("Updated CSS in detail.html")
else:
    print("Pattern not found in detail.html")
