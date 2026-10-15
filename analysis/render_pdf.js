// Render paper HTML to PDF with page numbers. Run: node analysis/render_pdf.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const root = path.resolve(__dirname, '..');
  const browser = await chromium.launch({ executablePath: undefined });
  const page = await browser.newPage();
  await page.goto('file://' + path.join(root, 'paper', 'T2D_weight_loss_review.html'), { waitUntil: 'networkidle' });
  await page.pdf({
    path: path.join(root, 'paper', 'T2D_weight_loss_review.pdf'), format: 'A4', printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div style="font-size:7px;font-family:Arial;color:#777;width:100%;padding:0 17mm;text-align:right">Type 2 diabetes and attenuated weight loss during incretin-based therapy</div>',
    footerTemplate: '<div style="font-size:7px;font-family:Arial;color:#777;width:100%;text-align:center"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: '20mm', bottom: '18mm', left: '17mm', right: '17mm' },
  });
  await browser.close();
  console.log('pdf written');
})();
