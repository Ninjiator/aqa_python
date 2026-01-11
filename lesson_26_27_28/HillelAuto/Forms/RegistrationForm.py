from HillelAuto.Cores.RegistrationFormLocators import RegistrationFormsLocators
from HillelAuto.Pages.HomePage import HomePage
from playwright.sync_api import expect

class RegistrationForm:

    def __init__(self, home_page: HomePage):
        self.home_page = home_page
        self.form_locators = RegistrationFormsLocators()


    def open_form(self):
        self.home_page.page.locator(self.home_page.sign_up_button_locator).click()
        self.home_page.page.wait_for_timeout(1000)

    def fill_user_name(self, user_name):
        pass

    def fill_user_last_name(self, user_last_name):
        pass

    def fill_user_mail(self, user_mail):
        pass

    def fill_user_password(self, user_password):
        pass

    def is_registration_form_opened(self) -> bool:
        try:
            expect(self.home_page.page.locator(self.form_locators.registration_text_locator)).to_have_text('Registration', timeout=1000)
            return True
        except AssertionError:
            return False

    def do_registration(self):
        # self.fill_user_name()
        # self.fill_user_last_name()
        # self.fill_user_mail()
        # self.fill_user_password()

    def is_registration_done(self):
        pass
