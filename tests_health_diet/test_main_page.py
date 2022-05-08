from pages.main_page import (
    MainPage,
    bell_opening,
    close_message_window,
    dots_three_vertical,
    name_account,
    opened_message_window,
)


def test_name_accaunt(driver, login_accaunt):
    """testing the account name"""

    main_page = MainPage(driver, login_accaunt)
    name_accaunt = main_page.get_text(name_account)
    assert "Сергей" == name_accaunt, f"Name accaunt is {name_accaunt}"


def test_bell_opening(driver, login_accaunt):
    """testing notifications"""

    main_page = MainPage(driver, login_accaunt)
    main_page.click(bell_opening)
    main_page.wait_until_not_visible(opened_message_window)
    assert main_page.is_visible(opened_message_window)
    main_page.click(close_message_window)
    assert not main_page.is_presented(opened_message_window)


def test_dots_three_vertical(driver, login_accaunt):
    """testing three points are vertical"""

    main_page = MainPage(driver, login_accaunt)
    assert main_page.is_clickable(dots_three_vertical)
