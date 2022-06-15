from pytest_bdd import feature, scenario, given, when, then, parsers
from pages.main_page import MainPage, name_account
import allure
from pages.base_page import URI


@allure.feature("main_page")
@allure.story("login name")
@scenario("feature/main_page.feature", "The login name corresponds to the user name")
def test_login_name():
    pass


@given("I log in under my account on the main page")
def open_main_page_and_login_accaunt(driver):
    MainPage(driver, login_accaunt=True, url=URI)


@when("I see login name")
def get_text_user_name(driver):
    main_page = MainPage(driver)
    global name_accaunt
    name_accaunt = main_page.get_text(name_account)


@then(parsers.parse("This login name is my {username}"))
def shoud_username_is_login_name(username):
   
    assert username == name_accaunt, f"Name accaunt is {name_accaunt}"