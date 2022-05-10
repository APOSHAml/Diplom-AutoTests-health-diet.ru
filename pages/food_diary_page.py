from pages.base_page import URI, BasePage, clas, css, id_, name, tag, xpath
from pages.main_page import tab_food_diary


class FoodDiaryPage(BasePage):
    """To disable sign in login_account, the attribute must have the False flag"""

    def __init__(self, driver, login_accaunt=True, url=""):

        if not url:
            url = f"{URI}/account/login"
        super().__init__(driver)
        if login_accaunt:
            self.open_sign_in(url)
            self.click(tab_food_diary)
        if url and not login_accaunt:
            self.get_url(url)


class LocatorsFoodDiaryPage:

    button_create_recipe = (name, "createRecipe")
    button_create_food = (css, 'div[title="Создать новый продукт"]')

    title_food = (css, 'span[class="t-name"]')

    chemical_composition_sign = (css, 'div[data-t="foodInfo"]')
    calories_chemical_composition_recipe = (
        css,
        "div:nth-child(3) > div:nth-child(2) > div.mzr-macronutrients-item-header > span",
    )
    foto_ingredient_chemical_composition = (css, "div:nth-child(7) > a > img")
    text_ingredient_chemical_composition = (css, 'td[class="el-name"]')
    input_weight_ingredient = (css, 'input[value="200"]')
    name_food_chemical_composition = (css, "div:nth-child(7) > p")
    steps_preparations_chemical_composition = (
        css,
        'div[class="uk-text-break uk-margin-bottom"]',
    )
    foto_steps_chemical_composition = (css, "div.uk-text-center > a > img")
    portion_weight_composition = (css, "div:nth-child(8) > ul > li")

    my_recipes = (css, "#js-food-search-stop-scroll > div > div:nth-child(2)")
    my_recipes_select_category = (
        css,
        'div[class="mzr-tree-node mod-group mod-padding-element"]',
    )
    my_roast_beef = (css, 'div[class="mzr-tree-node mod-padding-element2"]')
    calories = (css, 'div[class=" uk-text-bold-semi"]')
    my_recipe_name_food = (
        css,
        'div[class="mzr-block-header-light t-food-name mzr-font--body16sb"]',
    )
    portion_weight_composition_my_recipe = (css, "div:nth-child(5) > div > ul > li")

    button_add_favourites = (
        css,
        'div[class="uk-flex-item-none uk-flex uk-flex-column uk-flex-center uk-flex-middle mzr-gray-3-1-1"] > svg[name="star"]',
    )
    my_favourites = (
        css,
        "#js-food-search-header-2 > div.uk-flex.uk-flex-space-around > div:nth-child(2) > div > div",
    )
    tab_favourites = (
        css,
        "#js-food-search-header-content > div.uk-flex.uk-flex-space-around > div:nth-child(2) > div > div",
    )
    button_delete_favourites = (name, "starIn")
    text_favourites = (css, 'div[class="mzr-tree-node mod-padding-element"]')
    empty_favourites = (css, 'div[class=" uk-text-center mzr-font--body13reg"]')
    my_diary_favourites = (css, 'div[class="mzr-tree-node mod-padding-element"]')
    subscription_offer = (css, 'div[class="mzr-main-block"] > div > div > div > div[class]')
    schedule_add_favourites = (
        css,
        "div.mzr-block-menu.mzr-no-print > div:nth-child(3) > span",
    )
    select_dinner = (css, 'input[value="3"]')
    button_close = (css, 'svg[class="mzr-svg-common t-modal-close uk-flex-item-none"]')

    delete_selected = (name, "remove")
    button_notice_delete = (
        css,
        'button[class="uk-button uk-button-primary js-modal-confirm"]',
    )
    delete_record_my_food = (
        css,
        'div[data-t="remove"]>div[class="mzr-actions-button-text"]',
    )
    not_is_name_my_food = (
        css,
        'div[class="uk-flex uk-flex-column uk-flex-middle t-isEmpty"]',
    )

    search_ingredients_and_pecipes = (css, 'input[class="t-search-food"]')
    result_search_ingredients = (css, 'div[class="mzr-tree-node "]')
    empty_result_search = (css, 'div[class=" uk-text-center mzr-font--body13reg"]')

    my_foods = (css, 'div[class="mzr-tree-node mod-group "]')
    name_my_manufacturer_select_category = (
        css,
        'div[class="mzr-tree-node mod-group mod-padding-element"]',
    )
    name_my_product = (css, 'div[class="mzr-tree-node mod-padding-element2"]')
    name_my_manufacturer_open = (
        css,
        'div[class="mzr-tree-node mod-group mod-padding-element mzr-tree-node-open "]',
    )
    description_my_food = (tag, "p")

    button_add_record = (
        css,
        'button[class="uk-button uk-button-outline uk-margin-xsmall-right  uk-flex-item-auto"]',
    )
