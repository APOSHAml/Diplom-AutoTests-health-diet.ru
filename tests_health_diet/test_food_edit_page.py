import allure
import pytest

from pages.base_page import URI
from pages.food_diary_page import FoodDiaryPage
from pages.food_diary_page import LocatorsFoodDiaryPage as LFD
from pages.food_edit_page import (FoodEditPage, barcode_food, button_go_back,
                                  calories_chemical_composition_food,
                                  food_chemical_composition,
                                  input_description_manufacturer,
                                  input_name_food, input_name_manufacturer,
                                  portion_weight_food, save_button_food,
                                  select_category_unit_measurement,
                                  select_food_manufacturer,
                                  squirrels_composition_food)


@pytest.mark.dependency(name="name_edit_discription_food")
def test_name_edit_discription_food(driver):
    """testing the creation of a food and its use, as well as its appearance in the schedule"""

    with allure.step("Кликаем на кнопку создание своего продукта и заполняем данные"):
        food_edit_page = FoodEditPage(driver, url=URI)
        food_edit_page.wait_until_not_visible(input_name_food)
        food_edit_page.send_keys(input_name_food, "NameProduct")
        food_edit_page.click(select_food_manufacturer)
        food_edit_page.send_keys(input_name_manufacturer, "NameManufacturer")
        food_edit_page.send_keys(
            input_description_manufacturer, "DescriptionManufacturer"
        )
        food_edit_page.to_select(select_category_unit_measurement, "2")
        food_edit_page.send_keys(portion_weight_food, "50")
        food_edit_page.click(food_chemical_composition)
        food_edit_page.send_keys(calories_chemical_composition_food, "1000")
        food_edit_page.send_keys(portion_weight_food, "50")
        food_edit_page.send_keys(squirrels_composition_food, "17")
        food_edit_page.send_keys(barcode_food, "1234567")
        food_edit_page.click(save_button_food, button_go_back, LFD.my_foods)
    with allure.step(
        "Кликаем на свой созданый продукт в базе и проверяем название продукта"
    ):
        food_diary_page = FoodDiaryPage(driver, login_accaunt=False)
        food_diary_page.wait_to_be_clickable(LFD.name_my_manufacturer_select_category)
        food_diary_page.click(
            LFD.name_my_manufacturer_select_category, LFD.name_my_product
        )

        assert ("NameManufacturer", "NameProduct") == (
            food_diary_page.get_text(LFD.name_my_manufacturer_open),
            food_diary_page.get_text(LFD.name_my_product),
        )


@pytest.mark.dependency(depends=["name_edit_discription_food"])
def test_description_my_food(driver):
    """testing the description my food"""

    with allure.step("Кликаем в базе на наш продукт и проверяем его описание "):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.click(
            LFD.my_foods, LFD.name_my_manufacturer_select_category, LFD.name_my_product
        )
        food_diary_page.text_to_present_in_element(LFD.calories, "500")
        food_diary_page.click(LFD.button_add_record)
        assert ("NameProduct", "500", "DescriptionManufacturer", "порция (50г)") == (
            food_diary_page.get_text(LFD.my_recipe_name_food),
            food_diary_page.get_text(LFD.calories),
            food_diary_page.get_text(LFD.description_my_food),
            food_diary_page.get_text(LFD.portion_weight_composition_my_recipe),
        )


@pytest.mark.dependency(depends=["name_edit_discription_food"])
def test_delete_record_food(driver):
    """testing delete my record_food"""

    with allure.step("Удаление записи нашего продукта из дневника "):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.text_to_present_in_element(LFD.title_food, "NameProduct")
        food_diary_page.wait_to_be_clickable(LFD.title_food)
        food_diary_page.click(LFD.title_food, LFD.delete_record_my_food)
        assert "Дневник питания пуст" == food_diary_page.get_text(
            LFD.not_is_name_my_food
        )


@pytest.mark.dependency(depends=["name_edit_discription_food"])
def test_delete_my_food(driver):
    """testing delete my food"""

    with allure.step("Проверяем удаление нашего продукта"):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.click(
            LFD.my_foods,
            LFD.name_my_manufacturer_select_category,
            LFD.name_my_product,
            LFD.delete_selected,
            LFD.button_notice_delete,
        )
        food_diary_page.wait_until_not_visible(LFD.my_foods)
        food_diary_page.click(LFD.my_foods)

        assert not food_diary_page.is_visible(LFD.name_my_manufacturer_select_category)
