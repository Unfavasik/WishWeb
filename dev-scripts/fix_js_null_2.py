import sys
import re

with open('products.html', 'r') as f:
    content = f.read()

def replace_with_guard(match):
    id_name = match.group(1)
    return f"const el_{id_name.replace('-', '_')} = document.getElementById('{id_name}'); if (el_{id_name.replace('-', '_')}) el_{id_name.replace('-', '_')}.textContent"

# Replacing all document.getElementById('...').textContent
pattern = r"document\.getElementById\('([^']+)'\)\.textContent"
content = re.sub(pattern, replace_with_guard, content)

with open('products.html', 'w') as f:
    f.write(content)
print("Added guards to products.html")
