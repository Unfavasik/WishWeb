import sys
import glob

files = ['index.html', 'products.html', 'products/index.html']
old_str = '<img alt="Wishly Logo" class="h-7 w-auto object-contain transition-transform duration-300 hover:scale-105" src="/asset/top%20bar%20logo.webp">'
new_str = '<img alt="Wishly Logo" style="height: 28px; width: auto;" class="object-contain transition-transform duration-300 hover:scale-105" src="/asset/top%20bar%20logo.webp">'

for filepath in files:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"String not found in {filepath}. Checking for other matches...")
            # Let's search for similar tags
            import re
            pattern = r'<img alt="Wishly Logo"[^>]*src="/asset/top%20bar%20logo\.webp">'
            matches = re.findall(pattern, content)
            for m in matches:
                print(f"Found match: {m}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

