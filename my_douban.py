from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # Create a new context with the saved storage state.
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://movie.douban.com/")
    page.get_by_placeholder("搜索电影、电视剧、综艺、影人").click()
    page.get_by_placeholder("搜索电影、电视剧、综艺、影人").fill("123")
    page.get_by_role("button", name="搜索").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
