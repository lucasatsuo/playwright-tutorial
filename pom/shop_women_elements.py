

class ShopWomen:
    # This Class was used on Video 62. to substitute the other method of 
    # selecting on test_home_page_layout
    # I did not understand completely the reason of the change, but is a new
    # methodology being promoted
    #
    # Video 63. 
    # file was moved to package tests_ui_layout
    def __init__(self, page):
        self.celebrating_beauty_header = page.locator("text=Celebrating Beauty and Style")
        self.celebrating_beauty_body = page.locator("text=playwright-practice was founded by a group of like-minded fashion devotees")
        self.celebrating_beauty_hdr = page.locator("text=Celebrating Beauty and Style")
        self.profile_arrow = page.locator('._1hHt1')
        self.profile_icon = page.locator('#defaultAvatar-comp-kqx7o7qv')
        self.cart_icon = page.locator('.bQgup')
        self.my_orders = page.locator('text=My Orders')
        self.my_orders_profile_box = page.locator('#SOSP_CONTAINER_CUSTOM_ID >> :nth-match(div,4)')

