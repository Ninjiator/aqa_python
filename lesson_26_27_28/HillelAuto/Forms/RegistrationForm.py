from HillelAuto.Cores.RegistrationFormLocators import RegistrationFormsLocators
from playwright.sync_api import Page

class RegistrationForm:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
        self.sign_up_button_locator = "button.btn-primary"
        self.form_locators = RegistrationFormsLocators()


    def open_form(self):
        self.page.goto(self.base_url)
        self.page.locator(self.sign_up_button_locator).click()

    def fill_user_name(self, user_name):
        pass

    def fill_user_last_name(self, user_last_name):
        pass

    def fill_user_mail(self, user_mail):
        pass

    def fill_user_password(self, user_password):
        pass

    def do_registration(self):
        pass

    def is_registration_done(self):
        pass
