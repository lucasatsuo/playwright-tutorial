
class HomePage:
    # Video 63. 
    # file was moved to package tests_ui_layout
    def __init__(self, page):
        self.celebrate_header = page.locator("text=Celebrating Beauty and Style")
        self.celebrate_body = page.locator("text=playwright-practice was founded by a group of like-minded fashion")
