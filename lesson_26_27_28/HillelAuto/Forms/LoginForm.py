from playwright.sync_api import Page, expect
from HillelAuto.Pages.HomePage import HomePage
from utils.settings import d_settings


class LoginForm:
    sign_in_button_locator = "role=button[name='Sign In']"
    sign_in_mail_field_locator = "#signinEmail"
    sign_in_password_field_locator = "#signinPassword"
    my_profile_button_locator = "button.user-nav_toggle"
    login_button = "role=button[name='Login']"

    def __init__(self, home_page : HomePage):
        self.home_page = home_page
        self.page = self.home_page.page

    def open_form(self):
        self.page.locator(self.sign_in_button_locator).click()
        return self

    def do_login(self):
        self.page.locator(self.sign_in_mail_field_locator).fill(d_settings.USER_MAIL)
        self.page.locator(self.sign_in_password_field_locator).fill(d_settings.USER_PASS)
        self.page.locator(self.login_button).click()
        return self

    def is_login_success(self):
        try:
            expect(self.page.locator(self.my_profile_button_locator)).to_have_text('My profile', timeout=1000)
            return True
        except AssertionError:
            return False