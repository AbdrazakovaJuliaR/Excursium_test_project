import pytest
from pages.register_page import RegisterPage
from settings import BASE_URL, EMAIL, PASSWORD
from conftest import driver

def test_registration(driver):
    page = RegisterPage(driver)
    page.open(f"{BASE_URL}/register")
    page.register(EMAIL, PASSWORD)
    assert "confirm" in driver.current_url.lower()

