import os

from pages.base_page import BasePage, clas, css, idi, links, name, tag, xpath


class MainPage(BasePage):
    def __init__(self, driver, login_accaunt, url=""):
        if not url:
            url = os.getenv("MAIN_URL") or "https//health-diet.ru"
        super().__init__(driver)
        if login_accaunt is None or login_accaunt == True:
            login_accaunt


name_account = (css, '[title="Сергей"]')

tab_food_diary = (name, "bowl")

tab_training = (links, "Тренировки")

tab_weght_measurement = (links, "Вес и измерения")

tab_weght_measurement = (links, "Отчеты")

bell_opening = (name, "bell")

opened_message_window = (css, "#js_app_root > div.uk-height-1-1")

close_message_window = (css, 'svg[name="close"]')

dots_three_vertical = (
    css,
    'div[class="uk-float-right"]>svg[class="mzr-svg-common uk-flex-item-none"]',
)
