from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        console_messages = []
        page.on("console", lambda msg: console_messages.append(f"{msg.type}: {msg.text}"))
        page.on("pageerror", lambda err: console_messages.append(f"ERROR: {err}"))

        page.goto("http://127.0.0.1:5000/")
        page.wait_for_timeout(3000)

        hero_opacity = page.evaluate('''() => {
            const el = document.querySelector('.gs-hero-text > *');
            return el ? window.getComputedStyle(el).opacity : 'element not found';
        }''')

        print(f"Hero opacity: {hero_opacity}")

        page.screenshot(path="verification_homepage5.png", full_page=True)
        browser.close()

if __name__ == "__main__":
    run()
