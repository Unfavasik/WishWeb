import os

files = ['index.html', 'products.html', 'product-detail.html']
style_block = "\n    <style>\n      html { font-size: 80%; }\n    </style>\n"

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        
        if "html { font-size: 80%; }" not in content:
            content = content.replace("</head>", style_block + "</head>")
            
            with open(f, 'w') as file:
                file.write(content)
            print(f"Updated {f}")
        else:
            print(f"Already updated {f}")
