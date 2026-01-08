from playwright.sync_api import sync_playwright

from HillelAuto.HomePage import HomePage


def test_smoke_before_sign_up():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        home_page = HomePage(page)
        home_page.open_page()
        assert home_page.is_home_page_opened() is True, "Home Page is opened"

        home_page.click_on_sign_up()

        assert home_page.is_registration_form_opened() is True, "Registration form is opened"


