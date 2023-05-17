import time
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://movie.douban.com/')
    # Continue with the test
    time.sleep(40)
    # 保存storage state 到指定的文件
    storage = context.storage_state(path="state.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
