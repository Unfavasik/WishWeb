import sys

with open('products/detail.html', 'r') as f:
    content = f.read()

# Replace HTML
old_html = """      <!-- 3. Breadcrumb Section -->
      <nav class="breadcrumb-row" aria-label="Breadcrumb">
        <a href="/">Home</a>
        <span>/</span>
        <a href="/products">Templates</a>
        <span>/</span>
        <span id="breadcrumb-title" style="color:#e2e8f0; font-weight:500;">Cinematic-Birthday</span>
      </nav>

      <!-- Back to Templates link -->
      <div class="back-btn-row">
        <a href="/products" class="back-btn-link">
          <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
          <span>Back to Templates</span>
        </a>
      </div>"""

new_html = """      <!-- 3. Breadcrumb Section -->
      <div class="flex flex-wrap items-center gap-2 text-[16px] text-[#73737C] mb-4">
        <a href="/" class="hover:text-white transition-colors text-[#A7A7AE]">Home</a>
        <span class="text-[#73737C]">/</span>
        <a href="/products" class="hover:text-white transition-colors text-[#A7A7AE]">Templates</a>
        <span class="text-[#73737C]">/</span>
        <span id="breadcrumb-title" class="text-[#FFFFFF] font-medium truncate max-w-[150px] sm:max-w-none">Cinematic-Birthday</span>
      </div>

      <!-- Back to Templates link -->
      <div class="mb-6">
        <a href="/products" class="btn-back-home">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="m12 19-7-7 7-7"/>
            <path d="M19 12H5"/>
          </svg>
          <span>Back to Templates</span>
        </a>
      </div>"""

if old_html in content:
    content = content.replace(old_html, new_html)
else:
    print("Old HTML not found.")


old_css = """    .breadcrumb-row {
      font-size: 11.5px;
      color: #717684;
      display: flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 4px;
    }
    .breadcrumb-row a {
      color: #717684;
      text-decoration: none;
      transition: color 0.15s ease;
    }
    .breadcrumb-row a:hover {
      color: #cbd5e1;
    }
    .back-btn-row {
      margin-bottom: 12px;
    }
    .back-btn-link {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 13px;
      color: #9499a8;
      text-decoration: none;
      transition: color 0.15s ease;
      font-weight: 500;
    }
    .back-btn-link:hover {
      color: #FFFFFF;
    }"""

new_css = """    /* Back Button */
    .btn-back-home {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      height: 48px;
      max-height: 72px;
      padding: 0 20px;
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.15);
      background: rgba(255, 255, 255, 0.04);
      color: #F2F2F2;
      font-size: 16px;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.2s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    .btn-back-home:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.25);
    }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Old CSS not found.")

with open('products/detail.html', 'w') as f:
    f.write(content)

print("Updated detail.html")
