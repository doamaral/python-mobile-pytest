from os import getenv
from dotenv import load_dotenv
from page_objects.home_page import HomePage

from utils.mock_appium_driver import MockAppiumDriver
load_dotenv()


def test_driver_factory(setup: MockAppiumDriver):
    driver = setup
    print(f'This test is running over: {driver.get_platform_name()}')
    assert driver is not None
    assert driver.get_platform_name().lower() == getenv('PLATFORM').lower()
    home_page = HomePage(driver)
    home_page.click_login()
