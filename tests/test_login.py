from pages.login_page import LoginPage
from settings import BASE_URL, EMAIL, PASSWORD
from conftest import driver

def test_login_valid(driver):
    page = LoginPage(driver)
    page.open(f"{BASE_URL}/login")
    page.login(EMAIL, PASSWORD)
    assert "dashboard" in driver.current_url

