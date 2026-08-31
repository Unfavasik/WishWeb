import sys

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    old_block = """          <a href="/" class="flex items-center">
            <img alt="Wishly Logo" class="h-8 w-auto object-contain" src="/asset/top%20bar%20logo.webp">
          </a>"""

    new_block = """          <a href="/" class="flex items-center">
            <img alt="Wishly Logo" class="h-8 sm:h-10 w-auto object-contain transition-transform duration-300 hover:scale-105" src="/asset/top%20bar%20logo.webp">
          </a>"""

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

process_file('products.html')
process_file('products/index.html')
