import sys

with open('index.html', 'r') as f:
    content = f.read()

old_block = '<div class="space-y-4"><h3 class="text-lg font-semibold tracking-tight text-white">About <span class="text-white/60">Wishly</span></h3><p class="text-sm text-neutral-400 leading-relaxed">Hi, I\'m Prince — a web developer creating premium templates and fully responsive live websites for every special occasion.</p>'

new_block = '<div class="space-y-3"><a href="/" class="flex items-center"><img alt="Wishly Logo" class="h-8 sm:h-10 w-auto object-contain transition-transform duration-300 hover:scale-105" src="/asset/top%20bar%20logo.webp"></a><p class="text-sm text-neutral-400 leading-relaxed">Premium animated website templates for birthdays, anniversaries, and special moments.</p>'

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Updated index.html")
else:
    print("Not found in index.html")

