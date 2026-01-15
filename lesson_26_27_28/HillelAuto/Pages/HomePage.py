from playwright.sync_api import Page, expect


class HomePage:
    sign_up_button_locator = "role=button[name='Sign up']"

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
        self.url = self.base_url

    def open_page(self) -> None:
        self.page.goto(self.url)

    def is_home_page_opened(self) -> bool:
        try:
            expect(self.page.locator(self.sign_up_button_locator)).to_have_text('Sign up', timeout=1000)
            if self.page.url == self.url:
                return True
            else:
                return False
        except AssertionError:
            return False

    def click_on_sign_up(self) -> None:
        sign_up = self.page.locator(self.sign_up_button_locator)
        sign_up.click()
        self.page.wait_for_timeout(1000)



