import allure

from pages.base_page import URI
from pages.main_page import (MainPage, bell_opening, close_message_window,
                             dots_three_vertical, name_account,
                             opened_message_window)


def test_name_accaunt(driver):
    """testing the account name"""

    main_page = MainPage(driver, url=URI)
    name_accaunt = main_page.get_text(name_account)
    with allure.step("После входа в аккаунт, проверяем имя пользователя"):
        assert "Сергей" == name_accaunt, f"Name accaunt is {name_accaunt}"


def test_bell_opening(driver):
    """testing notifications"""

    main_page = MainPage(driver)
    with allure.step(
        "Кликаем по колокольчику для вызова окна сообщений и проверяем что оно отображается"
    ):
        main_page.click(bell_opening)
        main_page.wait_until_not_visible(opened_message_window)
        assert main_page.is_visible(opened_message_window)
    with allure.step(
        "Кликаем по по кнопке закрытия окна сообщений и проверяем что оно не отображается"
    ):
        main_page.click(close_message_window)
        assert not main_page.is_presented(opened_message_window)


def test_dots_three_vertical(driver):
    """testing three points are vertical"""

    with allure.step("Проверяем, что кнопка 'три точки' кликабельна"):
        main_page = MainPage(driver)
        assert main_page.is_clickable(dots_three_vertical)
