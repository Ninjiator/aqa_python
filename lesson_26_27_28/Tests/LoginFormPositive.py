from HillelAuto.Forms.LoginForm import LoginForm


def test_positive_sign_in(home_page):
    login_form = LoginForm(home_page).open_form().do_login()
    assert login_form.is_login_success() == True, "Login is failed"