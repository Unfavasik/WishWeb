import re
import sys

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # Find where <nav or <header id="main-header" begins
    if "detail.html" in filepath:
        start_pattern = r'<header id="main-header"'
        end_pattern = r'</header>'
    else:
        start_pattern = r'<nav(?! aria-label)[^>]*>' # avoid company/footer navs
        end_pattern = r'</nav>'

    # First find all navs to see if we're matching the right one
    navs = list(re.finditer(start_pattern + r'.*?' + end_pattern, content, re.IGNORECASE | re.DOTALL))
    
    # We want to replace the FIRST one (which is the main topbar)
    if navs:
        match = navs[0]
        replacement = '<wishly-topbar></wishly-topbar>'
        content = content[:match.start()] + replacement + content[match.end():]

        # Add the script just before </body>
        if "components/topbar.js" not in content:
            script_tag = '\n<script src="/components/topbar.js"></script>\n'
            content = content.replace('</body>', script_tag + '</body>')

        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No match in {filepath}")

for f in ["index.html", "products.html", "products/index.html", "products/detail.html"]:
    process_file(f)
