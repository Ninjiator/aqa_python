from HillelAuto.Forms.RegistrationForm import RegistrationForm
from HillelAuto.Cores.TestUser import TestUser
import pytest


@pytest.mark.parametrize("password", [
    ("aaa"),
    ("SEGEDSPDF"),
    ("abcdefgh!"),
    ("abcdefgh!aiosdfmg[iopasmdf[pgioms][pdfjmg]p[oim"),
    ("1247312843"),
])
def test_negative_sign_up_password(home_page, password):
    registration_form = RegistrationForm(home_page).open_form().do_registration(user_password = password)
    assert registration_form.is_registration_failed_by_password_conditions() == True, "Registration is failed due to password error"


@pytest.mark.parametrize("name", [
    ("a"),
    ("MarkMichelJaksonJamisonDerrelLilianDanielHenderson")
])
def test_negative_sign_up_name_length(home_page, name):
    registration_form = RegistrationForm(home_page).open_form().do_registration(user_name = name)
    assert registration_form.is_registration_failed_by_name_length() == True, "Registration is failed due to name length"

@pytest.mark.parametrize("name", [
    ("Mark2"),
    ("1"),
    ("!@$@$"),
])
def test_negative_sign_up_name_invalid(home_page, name):
    registration_form = RegistrationForm(home_page).open_form().do_registration(user_name = name)
    assert registration_form.is_registration_failed_invalid_name() == True, "Registration is failed due to invalid name"


@pytest.mark.parametrize("name", [
    ("Mark_Michel_Jakson_Jamison_Derrel_2010"),
    ("@"),
])
def test_negative_sign_up_invalid_name_and_length(home_page, name):
    registration_form = RegistrationForm(home_page).open_form().do_registration(user_name = name)
    assert registration_form.is_registration_failed_invalid_name_and_length() == True, "Registration is failed due to invalid name and name length"


@pytest.mark.parametrize("mail", [
    ("test@gmail."),
    ("myPost.post"),
])
def test_negative_sign_up_mail(home_page, mail):
    registration_form = RegistrationForm(home_page).open_form().do_registration(user_mail = mail)
    assert registration_form.is_registration_failed_incorrect_mail() == True, "Registration is failed due to incorrect email"

