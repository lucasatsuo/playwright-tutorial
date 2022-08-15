from playwright.sync_api import Playwright, sync_playwright, expect
from home_page_elements import HomePage


def about_us_section_verbiage(playwright: Playwright):
    # Video 61. Page Object Model
    # We separated the expect text to a Class on home_page_elements, so if the text
    # changes, it will be easy to maintain
    #
    # Video 62. 
    # https://playwright.dev/python/docs/pom
    #
    # Video 63. 
    # file was moved to package tests_ui_layout
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://symonstorozhenko.wixsite.com/website-1')
    shop_women = shop_women(page)

    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()


with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)