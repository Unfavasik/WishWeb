import sys

files = ['index.html', 'products.html', 'products/index.html']
old_str = '<img alt="Wishly Logo" class="h-8 sm:h-10 w-auto object-contain transition-transform duration-300 hover:scale-105" src="/asset/top%20bar%20logo.webp">'
new_str = '<img alt="Wishly Logo" class="h-7 w-auto object-contain transition-transform duration-300 hover:scale-105" src="/asset/top%20bar%20logo.webp">'

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
            print(f"String not found in {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

