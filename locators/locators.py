from selenium.webdriver.common.by import By

class RegisterPageLocators:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

class LoginPageLocators:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

class FilterPageLocators:
    FILTER_SECTION = (By.ID, "filter")
    SHOW_MORE_BUTTON = (By.XPATH, "//button[contains(text(),'Показать больше')]")

class BookingPageLocators:
    PERSON_SELECTOR = (By.ID, "person-count")
    CALCULATE_BUTTON = (By.ID, "calculate")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    DISCOUNT_INFO = (By.CLASS_NAME, "discount")