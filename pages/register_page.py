from pages.base_page import BasePage
from locators.locators import RegisterPageLocators as Locators

class RegisterPage(BasePage):
    def register(self, email, password):
        self.fill(Locators.EMAIL, email)
        self.fill(Locators.PASSWORD, password)
        self.click(Locators.SUBMIT)
