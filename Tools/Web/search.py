from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False, slow_mo=700)
    page = browser.new_page()
    page.goto("")
    page.screenshot(path="example.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)