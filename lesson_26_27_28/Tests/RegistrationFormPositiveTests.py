from HillelAuto.Forms.RegistrationForm import RegistrationForm
from HillelAuto.Cores.TestUser import TestUser

def test_positive_sign_up(home_page):
    registration_form = RegistrationForm(home_page)
    test_user = TestUser()

    registration_form.open_form()
    registration_form.do_registration()
    assert registration_form.is_registration_successful() == True, "Registration is Failed"

