import express from 'express';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;
const rootDir = process.cwd();

// Specialized handler for Next.js image optimization static exports
app.use((req, res, next) => {
  // Check if this is an image request in _next/image
  if (req.path.startsWith('/_next/image')) {
    const imagesDir = path.join(rootDir, '_next', 'image');
    if (fs.existsSync(imagesDir)) {
      const files = fs.readdirSync(imagesDir);
      
      // Try 1: Exact raw filename from originalUrl
      const rawRequest = req.originalUrl.replace(/^\/_next\/image\/?/, '');
      if (files.includes(rawRequest)) {
        return res.sendFile(path.join(imagesDir, rawRequest));
      }

      // Try 2: Query param reconstruction if parsed as query
      if (req.query.url) {
        const targetUrl = encodeURIComponent(req.query.url);
        const w = req.query.w;
        const q = req.query.q || '75';
        
        const candidate1 = `url=${targetUrl}&w=${w}&q=${q}`;
        if (files.includes(candidate1)) {
          return res.sendFile(path.join(imagesDir, candidate1));
        }

        // Search for partial match on filename
        const filename = path.basename(req.query.url);
        const matched = files.find(f => f.includes(filename) && (w ? f.includes(`w=${w}`) : true));
        if (matched) {
          const ext = path.extname(matched || rawRequest || req.query.url || '').toLowerCase();
        const mimeTypes = {
          '.png': 'image/png',
          '.jpg': 'image/jpeg',
          '.jpeg': 'image/jpeg',
          '.webp': 'image/webp',
          '.svg': 'image/svg+xml',
          '.ico': 'image/x-icon'
        };
        if (mimeTypes[ext]) {
          res.setHeader('Content-Type', mimeTypes[ext]);
        }
        return res.sendFile(path.join(imagesDir, matched));
        }
      }

      // Try 3: Search by decoded path segment
      const urlDecoded = decodeURIComponent(req.originalUrl);
      const matchedByUrl = files.find(f => {
        const decodedFile = decodeURIComponent(f);
        return urlDecoded.includes(decodedFile) || f === req.path.split('/').pop();
      });
      if (matchedByUrl) {
        return res.sendFile(path.join(imagesDir, matchedByUrl));
      }
    }
  }
  next();
});

// Route for Home page
app.get(['/', '/home', '/home/', '/home.html'], (req, res) => {
  const indexPath = path.join(rootDir, 'index.html');
  if (fs.existsSync(indexPath)) {
    return res.sendFile(indexPath);
  }
  res.status(404).send('Not Found');
});

// Route for /products catalog
app.get(['/products', '/products/', '/products/index.html', '/products.html'], (req, res) => {
  const productsPath = path.join(rootDir, 'products', 'index.html');
  if (fs.existsSync(productsPath)) {
    return res.sendFile(productsPath);
  }
  const productsFile = path.join(rootDir, 'products.html');
  if (fs.existsSync(productsFile)) {
    return res.sendFile(productsFile);
  }
  res.sendFile(path.join(rootDir, 'index.html'));
});

// Route for specific product detail pages (e.g. /products/cinematic-birthday)
app.get('/products/:slug*', (req, res, next) => {
  const detailPath = path.join(rootDir, 'product-detail.html');
  if (fs.existsSync(detailPath)) {
    return res.sendFile(detailPath);
  }
  next();
});

// Serve all static files from project root
app.use(express.static(rootDir, {
  extensions: ['html', 'htm']
}));

// Fallback to index.html for SPA client-side routing
app.get('*', (req, res) => {
  const indexPath = path.join(rootDir, 'index.html');
  if (fs.existsSync(indexPath)) {
    res.sendFile(indexPath);
  } else {
    res.status(404).send('Not Found');
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on http://0.0.0.0:${PORT}`);
});
