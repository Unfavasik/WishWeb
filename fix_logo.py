import re

with open("index.html", "r") as f:
    content = f.read()

# find the button that has id="brand-logo-btn"
# we will replace everything inside it.
pattern = re.compile(r'(<button[^>]*id="brand-logo-btn"[^>]*>).*?(</button>)')
match = pattern.search(content)

if match:
    # also remove gap-2.5 from the button classes
    start_tag = match.group(1).replace("gap-2.5", "")
    new_btn = start_tag + '<img alt="Wishly Logo" class="h-8 sm:h-10 w-auto object-contain transition-transform duration-300 group-hover:scale-105" src="/asset/top%20bar%20logo.webp">' + match.group(2)
    content = content[:match.start()] + new_btn + content[match.end():]
    with open("index.html", "w") as f:
        f.write(content)
    print("Replaced!")
else:
    print("Not found!")
