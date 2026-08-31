import sys
import re

with open('products/detail.html', 'r') as f:
    content = f.read()

pattern = r'function renderHeroVisual\(item\) \{[\s\S]*?return `\s*<div class="hero-preview-inner" style="justify-content:center; text-align:center;">[\s\S]*?</div>\s*`;\s*\}'

new_func = """function renderHeroVisual(item) {
      let imgSrc = '';
      if (item.id === 'cinematic-birthday' || item.previewType === 'cinematic-birthday') {
        imgSrc = '/product/c-birthday.png';
      } else if (item.id === 'birthday-p3') {
        imgSrc = '/product/birthday-p3.png';
      } else if (item.id === 'raksha-bandhan') {
        imgSrc = '/product/rakhi.png';
      }
      
      if (imgSrc) {
        return `<img src="${imgSrc}" alt="${item.title}" style="width:100%; aspect-ratio: 1.65/1; object-fit:cover; display:block;">`;
      }
      
      // Default fallback
      return `
        <div class="hero-preview-inner" style="justify-content:center; text-align:center; aspect-ratio: 1.65/1;">
          <div>
            <div style="font-size:22px; margin-bottom:4px;">✨ 🎂 🎉</div>
            <div style="font-size:15px; font-weight:700; color:#FFFFFF;">${item.title}</div>
            <div style="font-size:11px; color:#9ca3af; margin-top:2px;">${item.category} Template • Wishly</div>
          </div>
        </div>
      `;
    }"""

if re.search(pattern, content):
    content = re.sub(pattern, new_func, content)
    with open('products/detail.html', 'w') as f:
        f.write(content)
    print("Replaced renderHeroVisual in detail.html")
else:
    print("Pattern not found!")

