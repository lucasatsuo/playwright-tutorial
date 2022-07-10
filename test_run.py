from playwright.sync_api import Playwright, sync_playwright, expect

# Test generated using command 
# > playwright codegen https://symonstorozhenko.wixsite.com/website-1
#
# Timeout can be extended
# > playwright codegen --timeout=60000 https://my-website-url.com/slugID
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # Click button:has-text("Log In")
    page.locator("button:has-text(\"Log In\")").click()

    # Click [data-testid="switchToEmailLink"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()

    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
