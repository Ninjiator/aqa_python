from playwright.sync_api import Page

class MyProfilePage:

    def __init__(self, page):
        self.page = page
        self.registration_form =