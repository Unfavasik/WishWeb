import os

files = ['products.html', 'product-detail.html']
for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        
        new_content = content.replace('href="/products/${item.id}"', 'href="/product-detail.html?id=${item.id}"')
        
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Updated {f}")
