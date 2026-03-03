import re
from playwright.sync_api import Page, expect, sync_playwright

def test_language_switcher():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to local server...")
        page.goto("http://localhost:5000")

        # Wait for hydration
        page.wait_for_selector("#lang-toggle")

        # Open dropdown
        print("Clicking lang toggle...")
        page.click("#lang-toggle")

        # Ensure dropdown is visible
        page.wait_for_selector("#lang-dropdown", state="visible")

        # Click the English option
        print("Selecting English...")
        page.click("button.lang-option[data-lang='en']")

        # Wait for the navigation to complete (it should go to /set_lang/en and redirect back)
        page.wait_for_load_state("networkidle")

        # Ensure the flag has been updated correctly in the UI
        flag_text = page.locator("#current-lang-flag").inner_text()
        print(f"Current flag after switching: {flag_text}")

        if "🇬🇧" in flag_text:
            print("Language switch to English successful!")
        else:
            print("Error: Flag did not update to English.")

        browser.close()

if __name__ == "__main__":
    test_language_switcher()