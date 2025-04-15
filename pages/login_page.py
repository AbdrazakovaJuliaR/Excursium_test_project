from locators.locators import LoginPageLocators as Locators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, email, password):
        self.fill(Locators.EMAIL, email)
        self.fill(Locators.PASSWORD, password)
        self.click(Locators.LOGIN_BUTTON)

