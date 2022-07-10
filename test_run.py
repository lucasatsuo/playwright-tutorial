from asyncio import wait_for
from playwright.sync_api import Playwright, sync_playwright, expect
import time

# Test generated using command 
# > playwright codegen https://symonstorozhenko.wixsite.com/website-1
#
# Timeout can be extended
# > playwright codegen --timeout=60000 https://my-website-url.com/slugID
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Arrange (AAA test model: Arrange, Act, Assert)
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")


    # Act
    # Click button:has-text("Log In")
    time.sleep(4)
    print("Pressing log in")
    page.wait_for_selector('button:has-text("Log In")') # tem que descobrir por que isso nao funciona
    page.locator('button:has-text("Log In")').click()
    # Click [data-testid="switchToEmailLink"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()


    # Assert
    """ Creating the validations, 
    """
    # The course showed assert method, but it is python-specific and Playwright has a new method
    # expect() which works better, explained on Section 9: 56. NEW! - expect() method
    expect(page.locator("text=Email cannot be blank")).to_be_visible()
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
