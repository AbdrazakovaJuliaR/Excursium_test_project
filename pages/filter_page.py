from locators.locators import FilterPageLocators as Locators
from pages.base_page import BasePage

class FilterPage(BasePage):
    def is_filter_open(self):
        return self.is_element_present(Locators.FILTER_SECTION)

    def expand_filter(self):
        self.click(Locators.SHOW_MORE_BUTTON)

