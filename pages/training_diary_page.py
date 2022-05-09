from pages.base_page import URI, BasePage, clas, css, id_, link_, name, tag, xpath
from pages.main_page import tab_training


class TrainingDiaryPage(BasePage):
    """To disable login_account, the attribute must have the False flag"""

    def __init__(self, driver, login_accaunt=True, url=""):

        if not url:
            url = f"{URI}/account/login"
        super().__init__(driver)
        if login_accaunt:
            self.open_sign_in(url)
            self.click(tab_training)
        if url and not login_accaunt:
            self.get_url(url)


class LocatorsTrainingDiaryPage:

    button_create_training = (name, "create-exercise")

    other_category_post = (
        css,
        "#js-exersice-search-stop-scroll > div > div > div:nth-child(6) > div",
    )
    my_other_category = (
        css,
        'div[class="uk-flex uk-flex-middle mzr-tree-node  mod-padding-element"]',
    )

    my_name_training_category = (
        css,
        'div[class="uk-flex-item-1 mzr-pointer uk-margin-small-right"]',
    )

    scrolling = (
        css,
        'div[class="mzr-block-header-light uk-flex uk-flex-space-between uk-flex-middle "]',
    )
    title_name_training = (css, 'div[class="mzr-block-header-light "]')
    repetitions_times_column = (css, "tr.el-row-parameter> td.el-first-column > div")
    name_parameters_column = (
        xpath,
        '//*[@id="js_app_root"]/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/table/tbody/tr[3]/td[1]/div',
    )

    column_count_approaches = (css, "tr.el-row-exercise > td:nth-child(3) > div")
    description_record_my_training = (
        css,
        "div.mzr-block-menu.mzr-no-print > div:nth-child(2) > span",
    )
    img_foto_load_description = (
        css,
        'div[class="uk-thumbnail uk-position-relative"] > img',
    )
    large_chest_decsripion = (css, 'span[class="mod-has-muscle-image"]')
    comb_muscle_decription = (css, "li:nth-child(2) > span.mod-has-muscle-image")

    still_button = (name, "dots-three-horizontal")
    icon_trash = (clas, "uk-icon-trash")
    not_is_name_my_training = (
        css,
        'div[class=" uk-text-center mzr-font--body16sb uk-margin-xlarge-bottom "]',
    )

    editing_parameters_training = (
        css,
        'div[data-t="editExercise"] > div[class="mzr-actions-button-text"]',
    )
    delete_my_training = (
        css,
        'button[class="uk-button uk-button-outline uk-button-transparent "]',
    )
    button_yes_delete = (
        css,
        'button[class="uk-button uk-button-primary js-modal-confirm"]',
    )

    tab_programms = (name, "checklist")
    button_choose_program = (name, "filter2")
    select_gender = (css, 'div[class="uk-form-controls "] > select')
    select_place = (css, "div:nth-child(2) > div > select")
    select_target = (css, "div:nth-child(3) > div > select")
    select_difficulty_level = (css, "div:nth-child(4) > div > select")
    home_for_men = (
        css,
        'div[class="uk-flex uk-flex-middle mzr-tree-node   mzr-tree-node-open  mod-group uk-flex-item-1 "] > div',
    )
