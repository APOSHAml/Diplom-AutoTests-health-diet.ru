from pathlib import Path

import allure
import pytest

from pages.base_page import URI, path_to_root_project
from pages.edit_recipe_page import EditRecipePage
from pages.edit_recipe_page import LocatorsEditRecipePage as LER
from pages.food_diary_page import FoodDiaryPage
from pages.food_diary_page import LocatorsFoodDiaryPage as LFD

empty_favourites_text = "Здесь появятся продукты и блюда, которые вы отметите как “Избранное”. Это позволит вам заполнять дневник на 30% быстрее!"
warning_add_favourites = 'Добавление продуктов и дневников из раздела "Избранное" доступно только в полной версии. Подробнее в разделе "Подписка"'
expected_list = [
    "Roast beef",
    "129 ккал",
    'Говядина, верхняя часть кострца, стейк, мясо с жиром убранным до уровня 0", сырая',
    "200",
    "Food",
    "Step One, Step Two",
    "Порция - 2г",
]


@pytest.mark.dependency(name="name_recipe_second_cours")
def test_name_recipe_second_cours(driver):
    """testing the creation of a recipe and its use in food, as well as its appearance in the schedule"""

    recipe_edit_page = EditRecipePage(driver, login_accaunt=True, url=URI)

    with allure.step("Кликаем на верхнюю кнопку создать рецепт и заполняем данные"):
        recipe_edit_page.click(LER.tab_description)
        recipe_edit_page.send_keys(LER.input_description, "food")
        recipe_edit_page.upload_file(
            LER.attach_foto_food, (str(path_to_root_project) + str(Path("/beef.png")))
        )
        recipe_edit_page.wait_until_not_visible(LER.button_load_foto)
        recipe_edit_page.click(LER.button_load_foto)
        recipe_edit_page.wait_until_not_visible(LER.displayed_foto_food)
        recipe_edit_page.send_keys(LER.stages_preparation, "Step One, Step Two")
        recipe_edit_page.upload_file(
            LER.attach_foto_steps, (str(path_to_root_project) + str(Path("/beef.png")))
        )
        recipe_edit_page.click(LER.foto_turn, count=4)
        recipe_edit_page.click(LER.button_load_foto)
        recipe_edit_page.send_keys(LER.input_hours, "2")
        recipe_edit_page.text_to_present_in_element(
            LER.description_select_ingredient, "не выбрано"
        )
        recipe_edit_page.click(
            LER.description_select_ingredient,
            LER.meat_ingredient_input,
            LER.input_beef_name,
            LER.description_select_ingredient,
            LER.cooking_method,
            LER.choose_smoked,
            LER.roll_up,
            LER.choose_eating,
            LER.select_breakfest,
            LER.roll_up,
            LER.description_purpose,
            LER.description_on_holiday,
            LER.description_on_23,
            LER.roll_up,
            LER.hot_and_cold,
            LER.select_hot,
            LER.roll_up,
            LER.cuisines_world,
            LER.show_more,
            LER.polish_cuisine,
            LER.roll_up,
        )
        recipe_edit_page.scroll_up()
        recipe_edit_page.click(LER.tab_structure)

        recipe_edit_page.send_keys(LER.input_name_recipe, "Roast beef")
        recipe_edit_page.click(
            LER.input_select_category,
            LER.select_category,
            LER.roll_up,
            LER.food_search_beef_ingredient,
            LER.food_search_raw_beef,
        )
        recipe_edit_page.send_keys(LER.count_beef, "200")
        recipe_edit_page.click(LER.add_ingredient)
        recipe_edit_page.send_keys(LER.input_number, "2")
        recipe_edit_page.send_keys(LER.input_number, "100")
        recipe_edit_page.scroll_up()

        recipe_edit_page.click(
            LER.save_button, LER.button_to_eats, LER.button_add_close
        )

    with allure.step("Кликаем на запись в дневнике и проверяем введенные даные"):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.wait_until_not_visible(LFD.title_food, timeout=30)
        food_diary_page.click(LFD.title_food, LFD.chemical_composition_sign)
        food_diary_page.wait_until_not_visible(LFD.foto_ingredient_chemical_composition)
        food_diary_page.wait_until_not_visible(LFD.foto_steps_chemical_composition)

        actual_list = [
            food_diary_page.get_text(LFD.title_food),
            food_diary_page.get_text(LFD.calories_chemical_composition_recipe),
            food_diary_page.get_text(LFD.text_ingredient_chemical_composition),
            food_diary_page.get_attribute(LFD.input_weight_ingredient, "value"),
            food_diary_page.get_text(LFD.name_food_chemical_composition),
            food_diary_page.get_text(LFD.steps_preparations_chemical_composition),
            food_diary_page.get_text(LFD.portion_weight_composition),
        ]

        assert expected_list == actual_list


@pytest.mark.dependency(depends=["name_recipe_second_cours"])
def test_description_my_recipe(driver):
    """testing my recipe description"""

    with allure.step(
        "Кликаем в правой базе свой рецепт и сверяем вес, калории и порцию"
    ):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.click(
            LFD.my_recipes, LFD.my_recipes_select_category, LFD.my_roast_beef
        )
        food_diary_page.send_keys(LER.count_beef, "200")
        food_diary_page.text_to_present_in_element(LFD.calories, "258")
        assert (expected_list[0], "258", expected_list[2], expected_list[6]) == (
            food_diary_page.get_text(LFD.my_recipe_name_food),
            food_diary_page.get_text(LFD.calories),
            food_diary_page.get_text(LFD.text_ingredient_chemical_composition),
            food_diary_page.get_text(LFD.portion_weight_composition_my_recipe),
        )


@pytest.mark.dependency(depends=["name_recipe_second_cours"])
def test_add_favourites(driver):
    """testing adding my recipe to favorites"""

    with allure.step(
        "Нажимаем добаdить в избранное наш рецепт, и проверяем его наличие во вкладке 'Мое' "
    ):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.click(
            LFD.my_recipes,
            LFD.my_recipes_select_category,
            LFD.my_roast_beef,
            LFD.button_add_favourites,
            LFD.my_favourites,
            LFD.tab_favourites,
        )
        assert "Roast beef" == food_diary_page.get_text(LFD.text_favourites)


@pytest.mark.xfail(reason="Delete favourites doesn't work in base version")
def test_delete_favourites(driver):
    """testing delete my recipe to favorites"""

    with allure.step(
        "Нажимаем удалить из избранного наш рецепт, и проверяем его отсутсвие во вкладке 'Мое' "
    ):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.click(
            LFD.my_recipes,
            LFD.my_recipes_select_category,
            LFD.my_roast_beef,
            LFD.button_delete_favourites,
            LFD.my_favourites,
            LFD.tab_favourites,
        )

        assert empty_favourites_text == food_diary_page.get_text(LFD.empty_favourites)


def test_delete_favourites_in_base_version_site(driver):
    """testing delete diary from favorites in base version site"""

    with allure.step(
        "Нажимаем во вкладке 'Мое' в избранном на наш дневник питания, и проверяем невозможность его удаления "
    ):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.click(
            LFD.my_favourites,
            LFD.tab_favourites,
            LFD.my_diary_favourites,
        )

        assert warning_add_favourites == food_diary_page.get_text(
            LFD.subscription_offer
        )


@pytest.mark.dependency(depends=["name_recipe_second_cours"])
def test_schedule_add_favourites(driver):
    """testing schedule adding my recipe to favorites"""

    with allure.step("Добавление в график избранного рецепт "):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.click(
            LFD.schedule_add_favourites, LFD.select_dinner, LER.save_button
        )
        food_diary_page.scroll_to_element(LFD.button_close)
        food_diary_page.click(LFD.button_close)
        food_diary_page.click(LFD.my_favourites)

        assert "Дневник за" in food_diary_page.get_text(LFD.text_favourites)


@pytest.mark.dependency(depends=["name_recipe_second_cours"])
def test_search_ingredients_and_recipes(driver):
    """testing search ingredients and recipes"""
    with allure.step(
        "Вводим в поле поиска название рецепта и проверяем его в результатах проверки "
    ):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.wait_until_not_visible(LFD.search_ingredients_and_pecipes)
        food_diary_page.send_keys(LFD.search_ingredients_and_pecipes, "Roast beef")

        assert "Roast beefВторые блюда" == food_diary_page.get_text(
            LFD.result_search_ingredients
        )


def test_invalid_search_ingredients_and_pecipes(driver):
    """testing non-path_to_root_projectult search ingredients and recipes"""

    with allure.step(
        "Вводим в поле поиска несуществуещее название рецепта и проверяем пустой результат поиска "
    ):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.wait_until_not_visible(LFD.search_ingredients_and_pecipes)
        food_diary_page.send_keys(LFD.search_ingredients_and_pecipes, "ololololo")

        assert "По вашему запросу ничего не найдено." == food_diary_page.get_text(
            LFD.empty_result_search
        )


@pytest.mark.dependency(depends=["name_recipe_second_cours"])
def test_delete_record_recipe(driver):
    """testing delete record my recipes"""

    with allure.step("Удаление записи рецепта"):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.text_to_present_in_element(LFD.title_food, "Roast beef")
        food_diary_page.click(LFD.title_food)
        food_diary_page.click(LFD.delete_record_my_food)

        assert "Дневник питания пуст" == food_diary_page.get_text(
            LFD.not_is_name_my_food
        )


@pytest.mark.dependency(depends=["name_recipe_second_cours"])
def test_delete_my_recipe(driver):
    """testing delete my recipe"""

    with allure.step("Удаление нашего рецепта"):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=True)
        food_diary_page.click(
            LFD.my_recipes,
            LFD.my_recipes_select_category,
            LFD.my_roast_beef,
            LFD.delete_selected,
            LFD.button_notice_delete,
        )
        food_diary_page.wait_until_not_visible(LFD.my_recipes)

        assert not food_diary_page.is_visible(LFD.my_recipes_select_category)
