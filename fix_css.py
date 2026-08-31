import re

def process_css(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # We want to match: :123px or : 123px or -123px
    # But only inside the curly braces of a CSS rule?
    # A simpler way: we know CSS values come after a colon or space, and we want to avoid selectors and @media.
    # Actually, we can just look for things like `width: 340px`, `height:160px`, `transform: translateY(24px)`, etc.
    # What if we only replace specific known large pixel values that are causing issues?
    # The prompt says: "Check for fixed pixel values that are causing oversized layouts and normalize them where appropriate."
    
    # Let's just do a smart regex replacement:
    # Match any `px` that is preceded by a colon, space, or minus sign, and is NOT part of a CSS selector.
    # Selectors in tailwind often have `\[340px\]`. So if it is preceded by `[`, don't replace.
    # If it is inside `@media (...)`, don't replace.
    
    def px_to_rem(match):
        prefix = match.group(1)
        px_val = float(match.group(2))
        suffix = match.group(3)
        
        # Keep small px values as px (borders, etc)
        if px_val <= 2:
            return match.group(0)
            
        rem_val = px_val / 16.0
        rem_str = f"{rem_val:g}rem"
        return f"{prefix}{rem_str}{suffix}"
        
    # Regex: 
    # Group 1: prefix (colon, space, minus, comma, or parenthesis)
    # Group 2: number
    # Group 3: suffix (anything that is not a letter, to ensure we don't match something weird)
    # We will avoid replacing anything inside brackets `[` by negative lookbehind, but Python's re doesn't support variable length lookbehind.
    # Since we are matching `prefix`, if prefix is `[`, we can just return the original.
    
    def replacer(match):
        prefix = match.group(1)
        px_val = float(match.group(2))
        
        # Don't replace if prefix is '[' (meaning it's part of a class name like `w-[340px]`)
        if '[' in prefix:
            return match.group(0)
            
        if px_val <= 2:
            return match.group(0)
            
        rem_val = px_val / 16.0
        rem_str = f"{rem_val:g}rem"
        return f"{prefix}{rem_str}"
        
    # Match e.g., `: 340px`, `:340px`, ` 340px`, `-340px`, `(340px`
    # We want to avoid replacing breakpoints like `min-width: 640px`.
    # Tailwind breakpoints: 640, 768, 1024, 1280, 1536.
    
    def replacer_advanced(match):
        full_match = match.group(0)
        # Avoid media queries manually
        for bp in ['640px', '768px', '1024px', '1280px', '1536px']:
            if bp in full_match:
                return full_match
                
        # We need to capture the exact string and replace the px part.
        # But wait, it's easier to just search for `property: valuepx` and replace.
        pass

    # A better approach: split by `{` and `}` to only process the content inside blocks.
    parts = re.split(r'({|})', content)
    inside_block = False
    
    for i, part in enumerate(parts):
        if part == '{':
            inside_block = True
        elif part == '}':
            inside_block = False
        else:
            if inside_block:
                # We are inside a CSS block. We can safely replace all `[0-9.]*px` EXCEPT if they are small (<=2px).
                def inline_px(m):
                    px = float(m.group(1))
                    if px <= 2:
                        return m.group(0)
                    return f"{px/16.0:g}rem"
                
                parts[i] = re.sub(r'\b([0-9.]+)px\b', inline_px, part)

    new_content = "".join(parts)
    with open(filename, 'w') as f:
        f.write(new_content)

process_css('_next/static/css/3f8cdf90cad42ec8.css')
