from HillelAuto.Forms.RegistrationForm import RegistrationForm
from HillelAuto.Pages.HomePage import HomePage
from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture(scope='session')
def pw_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page

@pytest.fixture()
def home_page(brand_new_page):
    home_page = HomePage(brand_new_page)
    home_page.open_page()
    return home_page

@pytest.fixture()
def brand_new_page(pw_page):
    browser = pw_page.context.browser
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()