from HillelAuto.Forms.RegistrationForm import RegistrationForm
from HillelAuto.Pages.HomePage import HomePage


def test_open_home_page(pw_page):
    home_page = HomePage(pw_page).open_page()
    assert home_page.is_home_page_opened() is True, "Home Page is opened"


def test_open_sign_up_form(home_page):
    registration_form = RegistrationForm(home_page).open_form()
    assert registration_form.is_registration_form_opened() is True, "Registration Form is opened"

