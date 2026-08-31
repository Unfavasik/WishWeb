import sys

with open('index.html', 'r') as f:
    content = f.read()

old_string = '<div class="inline-flex items-center gap-1 text-xs font-semibold text-brand group-hover:translate-x-0.5 transition-transform">'
new_string = '<div class="inline-flex items-center gap-1 text-xs font-semibold group-hover:translate-x-0.5 transition-transform" style="color: #F80612;">'

if old_string in content:
    content = content.replace(old_string, new_string)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success for index.html!")
else:
    print("Old string not found in index.html!")

