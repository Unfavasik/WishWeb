import sys
import re

with open('products/detail.html', 'r') as f:
    content = f.read()

def replace_with_guard(match):
    id_name = match.group(1)
    return f"const el_{id_name.replace('-', '_')} = document.getElementById('{id_name}'); if (el_{id_name.replace('-', '_')}) el_{id_name.replace('-', '_')}.href"

# Replacing all document.getElementById('...').href
pattern = r"document\.getElementById\('([^']+)'\)\.href"
content = re.sub(pattern, replace_with_guard, content)

with open('products/detail.html', 'w') as f:
    f.write(content)
print("Added guards to detail.html hrefs")
