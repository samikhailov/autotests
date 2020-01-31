from .base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Invalid login page URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LOGIN_FORM), 'Login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*REGISTER_FORM), 'Register form not found'
