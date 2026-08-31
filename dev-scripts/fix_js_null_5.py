import sys
import re

with open('products/detail.html', 'r') as f:
    content = f.read()

content = content.replace("badgesContainer.innerHTML =", "if (badgesContainer) badgesContainer.innerHTML =")
content = content.replace("includedContainer.innerHTML =", "if (includedContainer) includedContainer.innerHTML =")
content = content.replace("document.getElementById('product-hero-preview').innerHTML =", "const previewEl = document.getElementById('product-hero-preview'); if (previewEl) previewEl.innerHTML =")
content = content.replace("grid.innerHTML =", "if (grid) grid.innerHTML =")
content = content.replace("stage.innerHTML =", "if (stage) stage.innerHTML =")

with open('products/detail.html', 'w') as f:
    f.write(content)
print("Added guards to detail.html innerHTMLs")
