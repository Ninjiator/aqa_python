from HillelAuto.Forms.RegistrationForm import RegistrationForm
from HillelAuto.Pages.HomePage import HomePage
from HillelAuto.Cores.TestUser import TestUser
import pytest

def test_open_home_page(pw_page):
    home_page = HomePage(pw_page)
    home_page.open_page()
    assert home_page.is_home_page_opened() is True, "Home Page is opened"


def test_open_sign_up_form(home_page):
    registration_form = RegistrationForm(home_page)
    registration_form.open_form()
    assert registration_form.is_registration_form_opened() is True, "Registration Form is opened"

# @pytest.mark.parametrize("user_name, surname, mail, password, repeat_password",
#                          [("Oleksiis", "Jaksons", "JaksonOleksiis@gmail.com", "Ks@1wdfnmd2s", "Ks@1wdfnmd2s")])



def test_positive_sign_up(home_page):
    registration_form = RegistrationForm(home_page)
    test_user = TestUser()

    registration_form.open_form()
    registration_form.do_registration(test_user.name, test_user.last_name, test_user.mail, test_user.password)
    assert registration_form.is_registration_successful() == True, "Registration is Failed"


@pytest.mark.parametrize("password", [
    ("aaa"),
    ("SEGEDSPDF"),
    ("abcdefgh!"),
    ("abcdefgh!aiosdfmg[iopasmdf[pgioms][pdfjmg]p[oim"),
    ("1247312843"),
])
def test_negative_sign_up_password(home_page, password):
    registration_form = RegistrationForm(home_page)
    test_user = TestUser()

    registration_form.open_form()
    registration_form.do_registration(test_user.name, test_user.last_name, test_user.mail, password)
    assert registration_form.is_registration_failed_by_password() == True, "Registration is failed due to password error"

