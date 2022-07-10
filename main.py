from playwright.sync_api import Playwright, sync_playwright, expect


# run é um objeto que herda de Playwright??...
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    PassFlag = 'PASS'

    # Open new page
    page = context.new_page()

    # Go to https://www.youtube.com/
    page.goto("https://www.youtube.com/")

    # Click [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").click()

    # Fill [placeholder="Search"]
    page.locator("[placeholder=\"Search\"]").fill("O show do césar")

    # Click #search-icon-legacy
    page.locator('xpath=//*[@id="search-icon-legacy"]').click()
    try:
        expect(page).to_have_url("https://www.youtube.com/results?search_query=O+show+do+c%C3%A9sar")
    except Exception as e:
        PassFlag = "FAIL"
        print(e)

    print("O programa rodou até aqui")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
