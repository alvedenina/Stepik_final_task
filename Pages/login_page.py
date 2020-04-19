from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.current_url()
        assert self.is_element_present(*MainPageLocators.Login_url), "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.Login_form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.Register_form), "Register form is not presented"