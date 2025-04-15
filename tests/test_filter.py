from pages.filter_page import FilterPage
from settings import BASE_URL
from conftest import driver

def test_filter_expansion(driver):
    page = FilterPage(driver)
    page.open(f"{BASE_URL}/tours")
    assert page.is_filter_open()
    page.expand_filter()

