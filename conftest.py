import uuid
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import path_to_root_project, Path
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities





def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru or en")




@pytest.fixture(scope="function")
def driver(request):
    """Chrome page scale:
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')

    chrome_options.add_argument('--headless')
    """

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver = None
    options = Options()
    options.add_argument("start-maximized")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        d = DesiredCapabilities.CHROME
        options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})
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
    
    with open(str(path_to_root_project) + str(Path("/newfile.log")), 'w') as f:
        for log in driver.get_log('browser'):
        
            f.write(str(log) + "\n")
            
    driver.quit()
