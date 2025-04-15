from locators.locators import BookingPageLocators as Locators
from pages.base_page import BasePage

class ExcursionPage(BasePage):
    def set_person_count(self, count):
        self.fill(Locators.PERSON_SELECTOR, str(count))

    def calculate_price(self):
        self.click(Locators.CALCULATE_BUTTON)

    def get_error_message(self):
        return self.driver.find_element(*Locators.ERROR_MESSAGE).text

    def get_discount_info(self):
        return self.driver.find_element(*Locators.DISCOUNT_INFO).text

