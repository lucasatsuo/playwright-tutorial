from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.youtube.com/
    page.goto("https://www.youtube.com/")

    # Click [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").click()

    # Click text=Explore Explore >> #icon
    page.locator("text=Explore Explore >> #icon").click()
    # expect(page).to_have_url("https://www.youtube.com/feed/explore")

    # Click [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").click()

    # Click ytd-mini-guide-renderer[role="navigation"] >> text=Shorts Shorts >> #icon
    # with page.expect_navigation(url="https://www.youtube.com/shorts/8Lt1hJnEcq0"):
    with page.expect_navigation():
        page.locator("ytd-mini-guide-renderer[role=\"navigation\"] >> text=Shorts Shorts >> #icon").click()

    # Click [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").click()

    # Click text=Subscriptions Subscriptions >> #icon
    page.locator("text=Subscriptions Subscriptions >> #icon").click()
    # expect(page).to_have_url("https://www.youtube.com/feed/subscriptions")

    # Click [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").click()

    # Click text=Library Library >> #icon
    page.locator("text=Library Library >> #icon").click()
    # expect(page).to_have_url("https://www.youtube.com/feed/library")

    # Click [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").click()

    # Click text=History History >> #icon
    page.locator("text=History History >> #icon").click()
    # expect(page).to_have_url("https://www.youtube.com/feed/history")

    # Click [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
