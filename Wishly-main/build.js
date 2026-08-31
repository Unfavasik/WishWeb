import fs from 'fs';
import path from 'path';

const distDir = './dist';

if (fs.existsSync(distDir)) {
  fs.rmSync(distDir, { recursive: true, force: true });
}
fs.mkdirSync(distDir);

const includeExts = ['.html', '.ico', '.png', '.jpg', '.webp', '.css', '.js', '.svg'];
const exactInclude = ['manifest.json'];
const excludeFiles = ['package.json', 'package-lock.json', 'bun.lock', 'metadata.json', 'server.js', 'build.js'];

const files = fs.readdirSync('.');
for (const file of files) {
  if (file === 'node_modules' || file === 'dist' || file === 'dev-scripts' || file.startsWith('.') || file.endsWith('.py')) {
    continue;
  }
  
  const stat = fs.statSync(file);
  if (stat.isDirectory()) {
    fs.cpSync(file, path.join(distDir, file), { recursive: true });
    console.log(`Copied directory ${file}/`);
  } else {
    if (excludeFiles.includes(file)) continue;
    
    const ext = path.extname(file);
    if (includeExts.includes(ext) || exactInclude.includes(file)) {
      fs.cpSync(file, path.join(distDir, file));
      console.log(`Copied file ${file}`);
    }
  }
}
console.log('Build completed successfully!');
