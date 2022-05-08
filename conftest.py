import pytest
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import uuid


@pytest.fixture(scope="function")
def driver():
    """Chrome page scale:
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')

    chrome_options.add_argument('--headless')
    """

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)

    yield driver
    try:
        allure.attach(driver.get_screenshot_as_png(), name=f"Screenshot Picture/{str(uuid.uuid4())}", attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        print(f"Fail make screenshot {e}")
    driver.quit()


@pytest.fixture(scope="function")
def login_accaunt(driver):
    """Log in to the Site Login section"""

    accaunt_page = BasePage(driver)
    accaunt_page.open_sign_in()
