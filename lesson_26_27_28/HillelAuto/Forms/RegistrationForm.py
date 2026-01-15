from HillelAuto.Cores.RegistrationFormLocators import RegistrationHelper
from HillelAuto.Pages.HomePage import HomePage
from playwright.sync_api import expect
from faker import Faker

class RegistrationForm:

    def __init__(self, home_page: HomePage):
        self.home_page = home_page
        self.page = home_page.page
        self.reg_helper = RegistrationHelper()


    def open_form(self):
        self.page.locator(self.home_page.sign_up_button_locator).click()
        self.page.wait_for_timeout(1000)

    def fill_user_name(self, user_name):
        self.page.locator(self.reg_helper.user_name).fill(user_name, timeout=1000)

    def fill_user_last_name(self, user_last_name):
        self.page.locator(self.reg_helper.user_last_name).fill(user_last_name, timeout=1000)

    def fill_user_mail(self, user_mail):
        self.page.locator(self.reg_helper.user_mail).fill(user_mail, timeout=1000)

    def fill_user_password(self, user_password):
        self.page.locator(self.reg_helper.user_password).fill(user_password, timeout=1000)

    def fill_user_password_repeat(self, user_password):
        self.page.locator(self.reg_helper.user_password_repeat).fill(user_password, timeout=1000)

    def is_registration_form_opened(self) -> bool:
        try:
            expect(self.page.locator(self.reg_helper.registration_text_locator)).to_have_text('Registration', timeout=1000)
            return True
        except AssertionError:
            return False

    def do_registration(self, user_name, user_last_name, user_mail, user_password, user_password_repeat = None):
        self.fill_user_name(user_name)
        self.fill_user_last_name(user_last_name)
        self.fill_user_mail(user_mail)
        self.fill_user_password(user_password)

        if user_password_repeat is None:
            self.fill_user_password_repeat(user_password)
        else:
            self.fill_user_password_repeat(user_password_repeat)

        if self.page.locator(self.reg_helper.register_button).is_enabled():
            self.page.locator(self.reg_helper.register_button).click(timeout=2000)
        self.page.wait_for_timeout(1000)

    def is_registration_successful(self):
        try:
            expect(self.page.locator(self.reg_helper.my_profile)).to_have_text('My profile', timeout=1000)
            return True
        except AssertionError:
            return False


    def is_registration_failed_by_password_conditions(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_password_text)).to_be_visible(timeout=1000)
            return True
        except AssertionError:
            return False

    def is_registration_failed_by_name_length(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_name_by_length)).to_be_visible(timeout=1000)
            return True
        except AssertionError:
            return False

    def is_registration_failed_invalid_name(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_name_invalid)).to_be_visible(timeout=1000)
            return True
        except AssertionError:
            return False

    def is_registration_failed_invalid_name_and_length(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_name_invalid) and self.page.get_by_text(self.reg_helper.error_name_by_length)).to_be_visible(timeout=1000)
            return True
        except AssertionError:
            return False

    def is_registration_failed_incorrect_mail(self):
        try:
            expect(self.page.get_by_text(self.reg_helper.error_mail_text)).to_be_visible(timeout=1000)
            return True
        except AssertionError:
            return False