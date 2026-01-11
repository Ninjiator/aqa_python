from HillelAuto.Pages.HomePage import HomePage
from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture(scope='session')
def pw_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page

# def my_profile_page(pw_page):
#     home_page = HomePage(pw_page)
#     home_page.open_page()
#
#     if home_page.is_home_page_opened():
#         return RegistrationPage(pw_page).do_registration()
