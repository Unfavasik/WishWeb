class WishlyTopBar extends HTMLElement {
  connectedCallback() {
    const currentPath = window.location.pathname;
    const isHome = currentPath === '/' || currentPath === '/index.html' || currentPath === '/home.html';
    const isProducts = currentPath.startsWith('/products');

    this.innerHTML = `
      <nav class="sticky top-0 z-50 transition-all duration-500 border-b border-white/5 bg-white/[0.02] backdrop-blur-md">
        <div class="mx-auto flex h-16 max-w-6xl items-center justify-between px-4 sm:px-6">
          <a href="/" class="group flex items-center outline-none cursor-pointer pl-1 sm:pl-2" tabindex="0" id="brand-logo-btn">
            <img alt="Wishly Logo" style="height: clamp(3.375rem, 7.5vw, 4.125rem); width: auto;" class="object-contain transition-transform duration-300 group-hover:scale-105" src="/asset/top%20bar%20logo.webp">
          </a>
          <div class="hidden md:flex items-center gap-1 rounded-full border border-white/[0.07] bg-white/[0.03] p-1.5 backdrop-blur-md shadow-[inset_0_1px_0_rgba(255,255,255,0.05)]">
            <a class="relative px-4 py-1.5 text-sm font-medium transition-colors outline-none group" href="/">
              <div class="absolute inset-0 rounded-full bg-white/10 ${isHome ? 'shadow-[inset_0_1px_0_rgba(255,255,255,0.15)]' : 'opacity-0 group-hover:opacity-100'} transition-opacity"></div>
              <span class="relative z-10 ${isHome ? 'text-white' : 'text-white/50 group-hover:text-white'} transition-colors duration-200">Home</span>
            </a>
            <a class="relative px-4 py-1.5 text-sm font-medium transition-colors outline-none group" href="/products">
              <div class="absolute inset-0 rounded-full bg-white/10 ${isProducts ? 'shadow-[inset_0_1px_0_rgba(255,255,255,0.15)]' : 'opacity-0 group-hover:opacity-100'} transition-opacity"></div>
              <span class="relative z-10 ${isProducts ? 'text-white' : 'text-white/50 group-hover:text-white'} transition-colors duration-200">Products</span>
            </a>
          </div>
          <button onclick="if(window.openCountryModal) window.openCountryModal()" class="hidden md:flex items-center gap-2 px-3.5 py-2 rounded-full border border-white/[0.07] bg-white/[0.03] hover:bg-white/[0.08] backdrop-blur-md transition-all duration-200 outline-none group" tabindex="0">
            <span class="text-sm text-white/50">Select Country</span>
          </button>
          <div class="md:hidden flex items-center gap-2">
            <button onclick="if(window.openCountryModal) window.openCountryModal()" class="flex items-center justify-center h-10 w-10 rounded-full border border-white/20 bg-gradient-to-br from-white/10 to-white/5 shadow-[inset_0_1px_0_rgba(255,255,255,0.15),0_4px_12px_rgba(0,0,0,0.3)] hover:bg-white/10 text-white/80 outline-none" tabindex="0">
              <span class="text-xs">🌐</span>
            </button>
            <button id="btn-mobile-menu" aria-label="Open menu" class="inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm font-medium ring-offset-transparent transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand/45 focus-visible:ring-offset-0 disabled:pointer-events-none disabled:opacity-50 hover:text-foreground backdrop-blur-sm rounded-full hover:bg-white/10 text-white/80 h-10 w-10 border border-white/10 bg-white/[0.02]">
              <svg id="icon-menu-open" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-menu h-5 w-5" style="opacity: 1;">
                <line x1="4" x2="20" y1="12" y2="12"></line>
                <line x1="4" x2="20" y1="6" y2="6"></line>
                <line x1="4" x2="20" y1="18" y2="18"></line>
              </svg>
              <svg id="icon-menu-close" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-x h-5 w-5 hidden">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
        </div>
        
        <!-- Mobile Drawer Menu -->
        <div id="mobile-menu-drawer" class="hidden border-b border-white/10 bg-[#0c0d12]/98 backdrop-blur-2xl px-4 py-5 transition-all md:hidden">
          <div class="flex flex-col gap-3">
            <a href="/" class="flex items-center justify-between py-2 text-base ${isHome ? 'font-semibold text-blue-400' : 'font-medium text-white/70 hover:text-white'} border-b border-white/5">
              <span>Home</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
            </a>
            <a href="/products" class="flex items-center justify-between py-2 text-base ${isProducts ? 'font-semibold text-blue-400' : 'font-medium text-white/70 hover:text-white'} border-b border-white/5">
              <span>Website Templates</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
            </a>
            <a href="/about-us" class="flex items-center justify-between py-2 text-base ${currentPath === '/about-us' ? 'font-semibold text-blue-400' : 'font-medium text-white/70 hover:text-white'} border-b border-white/5">
              <span>About Us</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
            </a>
            <div class="pt-2 flex items-center justify-between">
              <span class="text-xs text-white/50">Need Custom Website?</span>
              <a href="https://wa.me/918092464955?text=Hi%20Webkaizen%2C%20I%20want%20to%20order%20a%20website%20template." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 text-xs font-semibold hover:bg-emerald-500/30">
                <span>WhatsApp Us</span>
              </a>
            </div>
          </div>
        </div>
      </nav>
    `;

    // Attach event listener for mobile menu toggle
    const btnMobileMenu = this.querySelector('#btn-mobile-menu');
    const drawer = this.querySelector('#mobile-menu-drawer');
    const iconOpen = this.querySelector('#icon-menu-open');
    const iconClose = this.querySelector('#icon-menu-close');

    if (btnMobileMenu && drawer) {
      btnMobileMenu.addEventListener('click', () => {
        const isHidden = drawer.classList.contains('hidden');
        if (isHidden) {
          drawer.classList.remove('hidden');
          iconOpen.classList.add('hidden');
          iconClose.classList.remove('hidden');
        } else {
          drawer.classList.add('hidden');
          iconOpen.classList.remove('hidden');
          iconClose.classList.add('hidden');
        }
      });
    }
  }
}

customElements.define('wishly-topbar', WishlyTopBar);
