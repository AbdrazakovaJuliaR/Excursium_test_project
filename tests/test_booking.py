from pages.excursion_page import ExcursionPage
from settings import BASE_URL
from conftest import driver


def test_calculator_discount(driver):
    page = ExcursionPage(driver)
    page.open(f"{BASE_URL}/excursion/1")
    page.set_person_count(10)
    page.calculate_price()
    discount = page.get_discount_info()
    assert "Скидка" in discount

def test_calculator_invalid_person_count(driver):
    page = ExcursionPage(driver)
    page.open(f"{BASE_URL}/excursion/1")
    page.set_person_count(1000)
    page.calculate_price()
    error = page.get_error_message()
    assert "допустимый диапазон" in error

