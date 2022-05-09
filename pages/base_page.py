from email.errors import MessageError
from pathlib import Path
from time import sleep

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

ignored_exceptions = (
    NoSuchElementException,
    StaleElementReferenceException,
)


css = By.CSS_SELECTOR
clas = By.CLASS_NAME
name = By.NAME
xpath = By.XPATH
tag = By.TAG_NAME
id_ = By.ID
link_ = By.LINK_TEXT


path_to_root_project = Path(__file__).resolve().parents[1]

with open(
    str(path_to_root_project) + str(Path("/login_user.txt")), "r", encoding="utf-8-sig"
) as fp:
    login_user = fp.read().rstrip()

with open(
    str(path_to_root_project) + str(Path("/passwd_user.txt")), "r", encoding="utf-8-sig"
) as fp:
    passwd_user = fp.read().rstrip()


URI = "https://health-diet.ru"

login_button = (By.CSS_SELECTOR, 'a[class="uk-button uk-button-outline-transparent"]')
login = (By.ID, "login")
passwd = (By.ID, "password")
submit_account = (By.CSS_SELECTOR, 'button[value="login"]')


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def open_sign_in(self, url: str):
        """Log in with the account."""

        self.get_url(url)
        if url == URI:
            self.click(login_button)
        self.send_keys(login, login_user)
        self.send_keys(passwd, passwd_user)
        self.click(submit_account)

    def find(self, locator: tuple):
        """Find element on the page."""

        iteration = 0
        element = 0
        while not element and iteration < 10:
            sleep(0.5)
            iteration += 1
            element = self.driver.find_element(locator[0], locator[1])

        return element

    def finds(self, locator: tuple):
        """Find elements on the page."""

        return self.driver.find_elements(locator[0], locator[1])

    def click(
        self,
        *locators,
        hold_seconds=0,
        x_offset=1,
        y_offset=1,
        clickable=True,
        count=1,
    ):
        """Wait and click the element."""

        for locator in locators:
            if clickable:
                element = self.wait_to_be_clickable(locator, timeout=0.1)
            element = self.find(locator)

            if element and count > 1:
                start = 1
                while start != count:
                    action = ActionChains(self.driver)
                    action.move_to_element_with_offset(
                        element, x_offset, y_offset
                    ).pause(hold_seconds).click(on_element=element).perform()
                    start += 1

            else:
                msg = "Element with locator {0} not found"
                print(msg.format(locator))

            if element:
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(element, x_offset, y_offset).pause(
                    hold_seconds
                ).click(on_element=element).perform()

            else:
                print(f"Element with locator {locator} not found")

    def wait_to_be_clickable(
        self,
        locator: tuple,
        check_visibility=True,
        timeout=15,
    ):
        """Wait until the element will be ready for click."""

        element = None
        try:
            element = WebDriverWait(
                self.driver, timeout, ignored_exceptions=ignored_exceptions
            ).until(EC.element_to_be_clickable(locator))

        except Exception:
            print(f"Element {locator} not clickable!")

        if check_visibility:
            self.wait_until_not_visible(locator)

        return element

    def is_visible(self, locator: tuple):
        """Check is the element visible or not."""

        try:
            if element := self.find(locator):
                return element.is_displayed()

        except Exception:
            return False

    def is_presented(self, locator: tuple):
        """Checks that the element is present on the page."""

        element = True
        try:
            element = self.find(locator)

        except Exception:
            element = False

        finally:
            return element

    def is_clickable(self, locator: tuple):
        """Check is element ready for click or not."""

        element = self.wait_to_be_clickable(locator, timeout=0.1)

        return element is not None

    def wait_until_not_visible(self, locator: tuple, timeout=15):
        """Check element is visible or not."""

        element = None
        try:
            element = WebDriverWait(
                self.driver, timeout, ignored_exceptions=ignored_exceptions
            ).until(EC.visibility_of_element_located(locator))

        except Exception:
            print("Element Element not visible!!")

        if element:
            js = (
                "return (!(arguments[0].offsetParent === null) && "
                '!(window.getComputedStyle(arguments[0]) === "none") &&'
                "arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0"
                ");"
            )
            visibility = self.driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:
                sleep(0.5)
                iteration += 1
                visibility = self.driver.execute_script(js, element)

        return element

    def text_to_present_in_element(self, locator: tuple, keys: str, timeout=15):
        """Check text in visible in element."""

        try:
            WebDriverWait(
                self.driver, timeout, ignored_exceptions=ignored_exceptions
            ).until(EC.text_to_be_present_in_element(locator, keys))

        except Exception:
            print(f"Element {locator} not visible!!")

    def send_keys(self, locator: tuple, keys: str, wait=0, click=True):
        """Send keys to the element."""

        sleep(wait)
        if element := self.find(locator):
            if click:

                self.wait_to_be_clickable(locator)
                element.click()

            element.clear()
            keys = keys.replace("\n", "")
            element.send_keys(keys)

    def upload_file(self, locator: tuple, path_to_file: str, wait=0):
        """Uploading a file on a page."""

        if element := self.find(locator):
            element.send_keys(path_to_file)
            sleep(wait)

    def get_url(self, url: str):
        """Get any url."""

        self.driver.get(url)

    def get_current_url(self):
        """Returns current browser URL."""

        return self.driver.current_url

    def scroll_up(self, offset=0):
        """Scroll the page up. Or other (By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)"""

        if offset:
            self.driver.execute_script("window.scrollTo(0, -{0});".format(offset))

        else:
            self.driver.execute_script(
                "window.scrollTo(0, -document.body.scrollHeight);"
            )

    def scroll_down(self, offset=0):
        """Scroll the page down."""

        if offset:
            self.driver.execute_script("window.scrollTo(0, {0});".format(offset))

        else:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

    def get_text(self, locator: tuple):
        """Get text of the element."""

        element = self.find(locator)
        text = ""
        try:
            text = str(element.text)

        except Exception as e:
            print("Error: {0}".format(e))

        return text

    def get_attribute(self, locator: tuple, attr_name: str):
        """Get attribute of the element."""

        if element := self.find(locator):

            return element.get_attribute(attr_name)

    def right_mouse_click(self, locator: tuple, x_offset=0, y_offset=0, hold_seconds=0):
        """Click right mouse button on the element."""

        if element := self.wait_to_be_clickable(locator):
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).pause(
                hold_seconds
            ).context_click(on_element=element).perform()

        else:
            print(f"Element {locator} not visible!!")

    def highlight_and_make_screenshot(self, locator: tuple, file_name="element.png"):
        """Highlight element and make the screen-shot of all page."""

        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        self.driver.save_screenshot(file_name)

    def scroll_to_element(self, locator: tuple):
        """Scroll page to the element."""

        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def to_select(self, locator: tuple, value: str):
        """Select drop-down list."""

        element = self.find(locator)
        select_element = Select(element)
        select_element = select_element.select_by_value(value)

        return select_element

    def get_attribute_elements(self, locator: tuple, attr_name: str):
        """Get attribute of all elements."""

        elements = self.finds(locator)

        return [element.get_attribute(attr_name) for element in elements]
