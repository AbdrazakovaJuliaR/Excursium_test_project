from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LandingPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@href, '/login')]")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(@href, '/register')]")
    MAIN_BANNER = (By.CLASS_NAME, "main-banner")  # предположительно

class LandingPage(BasePage):
    def go_to_login(self):
        self.click(LandingPageLocators.LOGIN_BUTTON)

    def go_to_register(self):
        self.click(LandingPageLocators.REGISTER_BUTTON)

    def is_banner_visible(self):
        return self.is_element_present(LandingPageLocators.MAIN_BANNER)
