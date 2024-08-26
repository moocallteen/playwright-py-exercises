from playwright.sync_api import sync_playwright

def test_open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        print("Chrome page", page.url)
        print(page.title())
        page.wait_for_timeout(3000)
        browser.close() 