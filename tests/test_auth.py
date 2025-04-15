from pages.landing_page import LandingPage
from settings import BASE_URL
from conftest import driver

def test_open_landing_and_navigate_to_login(driver):
    page = LandingPage(driver)
    page.open(BASE_URL)
    assert page.is_banner_visible()
    page.go_to_login()
    assert "/login" in driver.current_url

def test_open_landing_and_navigate_to_register(driver):
    page = LandingPage(driver)
    page.open(BASE_URL)
    assert page.is_banner_visible()
    page.go_to_register()
    assert "/register" in driver.current_url
