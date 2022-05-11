from pages.base_page import (URI, BasePage, clas, css, id_, link_, name, tag,
                             xpath)
from pages.food_diary_page import LocatorsFoodDiaryPage as LFD
from pages.main_page import tab_food_diary


class FoodEditPage(BasePage):
    """To disable login_account, the attribute must have the False flag"""

    def __init__(self, driver, login_accaunt=False, url=""):

        super().__init__(driver)
        if login_accaunt and url:
            self.open_sign_in(url)
            self.click(tab_food_diary)
            self.wait_until_not_visible(LFD.my_foods)
            self.click(LFD.button_create_food)
        if not login_accaunt and url:
            self.get_url(url)
        if login_accaunt and not url:
            url = f"{URI}/account/login"
            self.open_sign_in(url)
            self.click(tab_food_diary)
            self.wait_until_not_visible(LFD.my_foods)
            self.click(LFD.button_create_food)


input_name_food = (css, 'input[class="js-food-edit-name"]')
select_food_manufacturer = (css, 'input[value="2"]')
input_name_manufacturer = (css, 'input[placeholder="Введите название производителя"]')
input_description_manufacturer = (css, 'textarea[placeholder="Напишите описание"]')
select_category_unit_measurement = (clas, "t-food-edit-select-unit ")
portion_weight_food = (
    css,
    'input[class="InputNumber t-food-edit-weightOfBaseUnit uk-text-left"]',
)
food_chemical_composition = (
    css,
    "div.uk-form-row.uk-margin-bottom > div > div > div:nth-child(2) > label > input[type=radio]",
)
calories_chemical_composition_food = (
    css,
    'input[class="InputNumber t-food-edit-11 uk-text-left"]',
)
squirrels_composition_food = (
    css,
    'input[class="InputNumber t-food-edit-13 uk-text-left"]',
)
barcode_food = (css, 'input[placeholder="Штрихкод"]')
save_button_food = (
    css,
    'button[class="uk-button uk-button-primary t-food-footer-save"]',
)
button_go_back = (css, 'svg[name="chevron-left"]')
