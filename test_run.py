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
    time.sleep(4)
    page.wait_for_load_state("networkidle") # without this, cant click on login button


    # Act
    # Click button:has-text("Log In")
    # Needs the wait: load_state("networkidle")
    page.wait_for_selector('button:has-text("Log In")') # tem que descobrir por que isso nao funciona
    print("Pressing log in")
    page.locator('button:has-text("Log In")').click()




    # Click [data-testid="signUp\.switchToSignUp"]
    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()

    # Click [data-testid="switchToEmailLink"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()

    # Fill [data-testid="emailAuth"] input[type="email"]
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("lucasatsuo@gmail.com")
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("test123")

    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()





    # # Click [data-testid="switchToEmailLink"] [data-testid="buttonElement"]
    # page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()
    # # Click [data-testid="submit"] [data-testid="buttonElement"]
    # page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()


    # Assert
    """ Creating the validations, 
    """
    # The course showed assert method, but it is python-specific and Playwright has a new method
    # expect() which works better, explained on Section 9: 56. NEW! - expect() method
    # expect(page.locator("text=Email cannot be blank")).to_be_visible()
    try:
        page.wait_for_load_state("networkidle")
        exp_locator = page.locator("[aria-label='lucasatsuo account menu']")
        expect(exp_locator)
        page.locator("[aria-label='lucasatsuo account menu']").screenshot(path="result.png")
    except Exception as e:
        print(e)
        page.screenshot(path="Error.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
