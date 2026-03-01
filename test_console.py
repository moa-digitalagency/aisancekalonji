from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}"))

        page.goto("http://localhost:5000")
        page.wait_for_timeout(3000)

        browser.close()

if __name__ == "__main__":
    run()
