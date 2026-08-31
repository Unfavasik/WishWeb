import sys
import re

with open('index.html', 'r') as f:
    content = f.read()

pattern = r'(<section\s+aria-labelledby="hero-heading"\s+class="relative flex min-h-\[80vh\] items-center justify-center overflow-hidden px-4 py-12"\s*>)'
video_html = '''\\1
        <!-- Hero Background Video -->
        <video 
          autoplay 
          loop 
          muted 
          playsinline 
          class="absolute inset-0 h-full w-full object-cover z-0 opacity-40"
          style="pointer-events: none;"
        >
          <source src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260422_112520_ee819691-f2e8-4c54-bb77-3fb72c84eaa5.mp4" type="video/mp4" />
        </video>
        <!-- Overlay to ensure text readability -->
        <div class="absolute inset-0 bg-black/50 z-0 pointer-events-none"></div>
'''

if re.search(pattern, content):
    new_content = re.sub(pattern, video_html, content)
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Replaced!")
else:
    print("Not found.")
