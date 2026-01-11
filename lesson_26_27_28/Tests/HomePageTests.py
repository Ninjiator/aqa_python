from HillelAuto.Pages.HomePage import HomePage


def test_smoke_home_page(pw_page):

        home_page = HomePage(pw_page)
        home_page.open_page()
        assert home_page.is_home_page_opened() is True, "Home Page is opened"


def test_sign_up_form(pw_page):
    home_page = HomePage(pw_page)
    home_page.open_page()
    home_page.click_on_sign_up()

    assert home_page.is_registration_form_opened() is True, "Registration form is opened"