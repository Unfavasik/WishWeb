import sys
import glob
import os
import re

html_files = []
for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.next' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

old_block = """          <a href="/" class="flex items-center gap-2.5">
            <span class="flex h-8 w-8 items-center justify-center overflow-hidden rounded-full border border-white/20 bg-white/10">
              <img alt="Wishly Logo" width="32" height="32" class="object-cover h-full w-full" src="/asset/top%20bar%20logo.webp">
            </span>
            <span class="text-base font-bold tracking-tight text-white font-brand">wishly</span>
          </a>"""

new_block = """          <a href="/" class="flex items-center">
            <img alt="Wishly Logo" class="h-8 w-auto object-contain" src="/asset/top%20bar%20logo.webp">
          </a>"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath} exact match")
    else:
        # Regex fallback
        pattern = r'<a href="/" class="flex items-center gap-2\.5">\s*<span class="flex h-8 w-8 items-center justify-center overflow-hidden rounded-full border border-white/20 bg-white/10">\s*<img alt="Wishly Logo" width="32" height="32" class="object-cover h-full w-full" src="/asset/top%20bar%20logo\.webp">\s*</span>\s*<span class="text-base font-bold tracking-tight text-white font-brand">wishly</span>\s*</a>'
        if re.search(pattern, content):
            content = re.sub(pattern, new_block, content)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Updated {filepath} with regex")

