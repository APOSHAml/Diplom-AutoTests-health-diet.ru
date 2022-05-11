from pages.base_page import (URI, BasePage, clas, css, id_, link_, name, tag,
                             xpath)
from pages.main_page import tab_training
from pages.training_diary_page import LocatorsTrainingDiaryPage as LTD


class EditTrainingDiaryPage(BasePage):
    """To disable login_account, the attribute must have the False flag"""

    def __init__(self, driver, login_accaunt=False, url=""):

        super().__init__(driver)
        if login_accaunt and url:
            self.open_sign_in(url)
            self.click(tab_training)
            self.wait_to_be_clickable(LTD.other_category_post)
            self.click(LTD.button_create_training)
        if not login_accaunt and url:
            self.get_url(url)
        if login_accaunt and not url:
            url = f"{URI}/account/login"
            self.open_sign_in(url)
            self.click(tab_training)
            self.wait_to_be_clickable(LTD.other_category_post)
            self.click(LTD.button_create_training)


class LocatorsEditTrainingDiaryPage:

    name_training = (css, 'input[placeholder="Введите название упражнения"]')
    select_part_of_muscle = (css, 'select[data-test="tSelectGroup"]')
    add_parameters = (
        css,
        'button[class="uk-button uk-button-link uk-button-success "]',
    )
    exercise_parameters = (css, 'input[value="2"]')
    create_my_parameters = (css, 'button[class="uk-button uk-button-outline "]')
    name_my_parameter = (css, 'input[placeholder="Введите название параметра"]')
    select_type_of_my_parameter = (
        css,
        'div[class="uk-form-row "]>div[class="uk-form-controls "]>select',
    )
    button_save_my_parameter = (
        css,
        'div[class="mzr-button-group uk-flex uk-flex-wrap uk-flex-middle  uk-flex-right mzr-button-group-right"]>button[class="uk-button uk-button-primary "]',
    )
    button_close_my_parameters = (
        css,
        "div.uk-margin-top.mzr-button-group-wrapper > div > button:nth-child(2)",
    )
    add_core_muscles = (name, "circlePlus")
    large_chest = (css, 'input[value="30"]')
    close_button = (css, 'svg[name="close"]')
    add_extra_muscles = (
        css,
        'svg[class="mzr-svg-common mzr-pointer uk-flex-item-none t-muscle-second uk-margin-right "]',
    )
    comb_muscle = (css, 'input[value="8"]')

    description_exercise = (css, 'div[class=" uk-text-muted"]')
    click_add_foto_exercise = (css, 'i[class="uk-icon-camera uk-icon-small"]')
    add_foto_exercise = (css, 'input[type="file"]')
    number_of_approaches = (css, 'input[class="InputNumber"]')
    img_foto_load = (css, 'div[class="uk-thumbnail uk-thumbnail-small"] > img')
    save_button_foto = (
        css,
        'button[class="uk-button uk-button-primary uk-margin-right  t-button-save"]',
    )
