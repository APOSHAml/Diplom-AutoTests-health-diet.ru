import uuid
import logging
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import path_to_root_project, Path






def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru or en")
    logging.basicConfig(filename=str(path_to_root_project) + str(Path("/newfile.log")),
                    format='%(asctime)s %(message)s',
                    filemode='w')

@pytest.fixture(scope="function")
def driver(request):
    """Chrome page scale:
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')

    chrome_options.add_argument('--headless')
    """

    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver = None
    options = Options()
    options.add_argument("start-maximized")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options.add_argument(f"--lang={user_language}")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile().set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(options=options, firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    driver.implicitly_wait(15)

    yield driver
    print("\nquit browser..")
    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Screenshot Picture/{str(uuid.uuid4())}",
            attachment_type=allure.attachment_type.PNG,
        )

    except Exception as e:
        print(f"Fail make screenshot {e}")
    driver.quit()
