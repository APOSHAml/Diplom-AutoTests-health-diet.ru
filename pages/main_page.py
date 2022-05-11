from pages.base_page import (URI, BasePage, clas, css, id_, link_, name, tag,
                             xpath)


class MainPage(BasePage):
    def __init__(self, driver, login_accaunt=False, url=""):

        super().__init__(driver)
        if login_accaunt and url:
            self.open_sign_in(url)
        if not login_accaunt and url:
            self.get_url(url)
        if login_accaunt and not url:
            url = f"{URI}/account/login"
            self.open_sign_in(url)


name_account = (css, '[title="Сергей"]')

tab_food_diary = (name, "bowl")

tab_training = (link_, "Тренировки")

tab_weght_measurement = (link_, "Вес и измерения")

tab_weght_measurement = (link_, "Отчеты")

bell_opening = (name, "bell")

opened_message_window = (css, "#js_app_root > div.uk-height-1-1")

close_message_window = (css, 'svg[name="close"]')

dots_three_vertical = (
    css,
    'div[class="uk-float-right"]>svg[class="mzr-svg-common uk-flex-item-none"]',
)
