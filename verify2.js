const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  page.on('console', msg => console.log(`BROWSER CONSOLE: ${msg.type()} ${msg.text()}`));
  page.on('pageerror', error => console.log(`BROWSER ERROR: ${error.message}`));

  await page.goto('http://127.0.0.1:5000');

  // Wait a little bit for animations
  await page.waitForTimeout(3000);

  // Let's also check the opacity of a hero element
  const heroOpacity = await page.evaluate(() => {
    const el = document.querySelector('.gs-hero-text > *');
    return el ? window.getComputedStyle(el).opacity : 'element not found';
  });
  console.log('Hero Element Opacity:', heroOpacity);

  await page.screenshot({ path: 'verification_homepage5.png', fullPage: true });
  await browser.close();
})();
