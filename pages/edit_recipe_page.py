from pages.base_page import BasePage, clas, css, idi, name, tag, xpath
from pages.food_diary_page import LocatorsFoodDiaryPage as LFD
from pages.main_page import tab_food_diary


class EditRecipePage(BasePage):
    """To disable login_account, the attribute must have the False flag"""

    def __init__(self, driver, login_accaunt, url=""):
        if not url:
            url = "https://health-diet.ru/diary/recipeEdit/new"

        super().__init__(driver)
        self.driver = driver
        if login_accaunt is None or login_accaunt == True:
            login_accaunt
            self.click(tab_food_diary)
            self.wait_to_be_clickable(LFD.my_recipes)
            self.click(LFD.button_create_recipe)


class LocatorsEditRecipePage:

    input_name_recipe = (idi, "form-recipe-name")
    input_select_category = (
        css,
        'div[class="uk-form-controls uk-position-relative"]>input[type="text"]',
    )
    select_category = (css, 'input[value="35"]')
    roll_up = (css, 'div[class=" mzr-pointer mzr-font--body13reg"]')
    second_courses = (css, '[value="Вторые блюда"]')
    input_name_cours = (css, '[value="Roast beef"]')

    description = (
        css,
        'div[class=" mzr-pointer uk-flex-item-none mzr-font--body14sb mzr-pointer uk-flex-item-none uk-margin-right "]',
    )
    input_description = (css, 'textarea[class="Textarea"]')
    attach_foto_food = (css, 'input[type="file"]')
    button_load_foto = (
        css,
        'div[class="mzr-button-group uk-flex uk-flex-wrap uk-flex-middle  uk-flex-center mzr-button-group-center"]>button[class="uk-button uk-button-primary "]',
    )
    displayed_foto_food = (
        css,
        "#js_app_root > div.mzr-grid-2-column > div.mzr-grid-content > div > div.mzr-main-block > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > img",
    )
    stages_preparation = (css, 'textarea[placeholder="Напишите инструкцию"]')
    attach_foto_steps = (
        css,
        'div[class="uk-form-row "]>div[class="uk-flex uk-flex-middle uk-flex-wrap"]>div[class="uk-flex uk-flex-middle uk-flex-center uk-flex-column mzr-gray-3-1-1"]>input[type="file"]',
    )
    foto_turn = (
        css,
        'div[class="mzr-button-group uk-flex uk-flex-wrap uk-flex-middle  uk-flex-center mzr-button-group-center"]>button[class="uk-button uk-button-outline uk-button-success uk-button-small "]',
    )
    input_hours = (css, 'input[class="InputNumber uk-text-left uk-text-left"]')
    description_select_ingredient = (css, 'input[placeholder="не выбрано"]')
    meat_ingredient_input = (css, 'input[value="120"]')
    input_beef_name = (css, 'input[value="137"]')
    cooking_method = (
        xpath,
        '//*[@id="js_app_root"]/div[3]/div[1]/div/div[1]/div[4]/div/div/div[4]/div/input',
    )

    choose_smoked = (css, 'input[value="82"]')
    choose_eating = (
        xpath,
        '//*[@id="js_app_root"]/div[3]/div[1]/div/div[1]/div[4]/div/div/div[5]/div/input',
    )
    select_breakfest = (css, 'input[value="95"]')
    description_purpose = (
        xpath,
        '//*[@id="js_app_root"]/div[3]/div[1]/div/div[1]/div[4]/div/div/div[6]/div/input',
    )
    description_on_holiday = (css, 'input[value="109"]')
    description_on_23 = (css, 'input[value="112"]')
    hot_and_cold = (
        xpath,
        '//*[@id="js_app_root"]/div[3]/div[1]/div/div[1]/div[4]/div/div/div[7]/div/input',
    )
    select_hot = (css, 'input[value="48"]')
    cuisines_world = (
        xpath,
        '//*[@id="js_app_root"]/div[3]/div[1]/div/div[1]/div[4]/div/div/div[8]/div/input',
    )
    show_more = (css, 'button[class="uk-button uk-button-outline uk-margin-top  "]')
    polish_cuisine = (css, 'input[value="237"]')
    tab_structure = (
        css,
        'div[class=" mzr-pointer uk-flex-item-none mzr-font--body14sb mzr-pointer uk-flex-item-none uk-margin-right "]',
    )

    food_search_beef_ingredient = (
        css,
        "#js-food-search-stop-scroll > div > div:nth-child(6)",
    )
    food_search_raw_beef = (
        css,
        "#js-food-search-stop-scroll > div > div:nth-child(30)",
    )

    count_beef = (css, '[inputmode="decimal"]')

    add_ingredient = (
        css,
        'button[class="uk-button uk-button-primary uk-width-1-1 uk-margin-top  t-button-add"]',
    )
    add_200_weigt = (css, 'div[style="color: var(--color--shade-black);"]')

    input_number = (css, 'input[inputmode="decimal"]')
    weight_serving = (css, 'div[class="uk-form-controls "]>input[step="any"]')
    save_button = (css, 'button[class="uk-button uk-button-primary "]')
    button_to_eats = (
        css,
        'button[class="uk-button uk-button-outline uk-margin-right  "]',
    )
    button_add_close = (
        css,
        'button[class="uk-button uk-button-primary t-button-add uk-flex-item-auto"]',
    )
