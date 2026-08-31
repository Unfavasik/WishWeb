import sys

with open('index.html', 'r') as f:
    content = f.read()

old_string = 'class="inline-flex items-center justify-center gap-2 whitespace-nowrap ring-offset-transparent transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand/45 focus-visible:ring-offset-0 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border border-brand/55 bg-gradient-to-br from-brand/90 via-brand/75 to-brand-dim/90 text-brand-foreground font-semibold shadow-[inset_0_1px_0_rgba(255,255,255,0.22),0_8px_32px_-6px_hsl(var(--brand)/0.55)] backdrop-blur-md hover:from-brand hover:via-brand/90 hover:to-brand-dim hover:shadow-[inset_0_1px_0_rgba(255,255,255,0.28),0_12px_40px_-4px_hsl(var(--brand)/0.6)] h-11 rounded-full px-8 text-base"'

new_string = 'class="inline-flex items-center justify-center gap-2 whitespace-nowrap ring-offset-transparent transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand/45 focus-visible:ring-offset-0 disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg]:size-4 [&amp;_svg]:shrink-0 border text-white font-semibold backdrop-blur-md hover:opacity-90 transition-opacity h-11 rounded-full px-8 text-base" style="background-color: #F80612; border-color: rgba(255,255,255,0.2); box-shadow: inset 0 1px 0 rgba(255,255,255,0.22), 0 8px 32px -6px rgba(248, 6, 18, 0.55);"'

if old_string in content:
    content = content.replace(old_string, new_string)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success!")
else:
    print("Old string not found!")

