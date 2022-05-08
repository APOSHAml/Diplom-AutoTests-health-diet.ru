from pathlib import Path

from pages.edit_recipe_page import LocatorsEditRecipePage as LER
from pages.edit_training_diary_page import EditTrainingDiaryPage
from pages.edit_training_diary_page import LocatorsEditTrainingDiaryPage as LETD
from pages.food_edit_page import button_go_back
from pages.training_diary_page import LocatorsTrainingDiaryPage as LTD
from pages.training_diary_page import TrainingDiaryPage

expected_list = (
    "NameTraining",
    "Повторения, раз",
    "NameMyParameters",
    "2",
    "большая грудная",
    "гребенчатая",
)


def test_edit_training(driver, login_accaunt):
    """testing the creation of a training and its use, as well as its appearance in the schedule"""

    edit_training_page = EditTrainingDiaryPage(driver, login_accaunt)

    edit_training_page.send_keys(LETD.name_training, "NameTraining")
    edit_training_page.to_select(LETD.select_part_of_muscle, "5")
    edit_training_page.click(
        LETD.add_parameters, LETD.exercise_parameters, LETD.create_my_parameters
    )

    edit_training_page.send_keys(LETD.name_my_parameter, "NameMyParameters")
    edit_training_page.to_select(LETD.select_type_of_my_parameter, "3")
    edit_training_page.click(
        LETD.button_save_my_parameter,
        LETD.button_close_my_parameters,
        LETD.add_core_muscles,
        LETD.large_chest,
        LETD.close_button,
        LETD.add_extra_muscles,
        LETD.comb_muscle,
        LETD.close_button,
        LETD.description_exercise,
    )

    edit_training_page.scroll_to_element(LTD.scrolling)
    edit_training_page.wait_until_not_visible(LETD.click_add_foto_exercise)
    edit_training_page.click(LETD.click_add_foto_exercise)
    edit_training_page.wait_until_not_visible(LETD.add_foto_exercise)
    edit_training_page.upload_file(
        LETD.add_foto_exercise, (str(Path.cwd()) + str(Path("/beef.png")))
    )
    edit_training_page.wait_until_not_visible(LETD.img_foto_load, timeout=200)
    edit_training_page.click(LETD.save_button_foto)
    edit_training_page.send_keys(LETD.number_of_approaches, "2")
    edit_training_page.click(LER.save_button, button_go_back)

    training_diary_page = TrainingDiaryPage(driver, login_accaunt=False)
    training_diary_page.wait_until_not_visible(LTD.other_category_post, timeout=30)
    training_diary_page.click(LTD.other_category_post, LTD.my_name_training_category)
    training_diary_page.click(LTD.description_record_my_training)
    training_diary_page.wait_until_not_visible(LTD.img_foto_load_description)

    assert (training_diary_page.is_visible(LTD.img_foto_load_description)) and (
        expected_list
        == (
            training_diary_page.get_text(LTD.title_name_training),
            training_diary_page.get_text(LTD.repetitions_times_column),
            training_diary_page.get_text(LTD.name_parameters_column),
            training_diary_page.get_text(LTD.column_count_approaches),
            training_diary_page.get_text(LTD.large_chest_decsripion),
            training_diary_page.get_text(LTD.comb_muscle_decription),
        )
    )


def test_my_filtr_exercises(driver, login_accaunt):
    """testing the filter of the exercise program"""

    training_diary_page = TrainingDiaryPage(driver, login_accaunt)
    training_diary_page.wait_until_not_visible(LTD.other_category_post, timeout=30)
    training_diary_page.click(LTD.tab_programms, LTD.button_choose_program)
    training_diary_page.to_select(LTD.select_gender, "2")
    training_diary_page.to_select(LTD.select_place, "1")
    training_diary_page.to_select(LTD.select_target, "2")
    training_diary_page.to_select(LTD.select_difficulty_level, "1")

    assert " Дома для мужчин" == training_diary_page.get_text(LTD.home_for_men)


def test_delete_record_training(driver, login_accaunt):
    """testing deleting a training record"""

    training_diary_page = TrainingDiaryPage(driver, login_accaunt)
    training_diary_page.wait_until_not_visible(LTD.still_button)
    training_diary_page.click(LTD.still_button, LTD.icon_trash)
    assert "Дневник тренировок пуст" == training_diary_page.get_text(
        LTD.not_is_name_my_training
    )


def test_delete_my_training(driver, login_accaunt):
    """testing deleting my training"""

    training_diary_page = TrainingDiaryPage(driver, login_accaunt)

    training_diary_page.wait_until_not_visible(LTD.other_category_post, timeout=30)
    training_diary_page.click(LTD.other_category_post)
    training_diary_page.wait_until_not_visible(LTD.my_name_training_category)
    training_diary_page.click(LTD.my_name_training_category)
    training_diary_page.wait_until_not_visible(LTD.still_button)
    training_diary_page.click(LTD.still_button, LTD.editing_parameters_training)
    training_diary_page.scroll_down()
    training_diary_page.click(LTD.delete_my_training, LTD.button_yes_delete)
    training_diary_page.wait_until_not_visible(LTD.other_category_post, timeout=30)

    assert all(
        i.text != "NameTraining (мое)"
        for i in training_diary_page.finds(LTD.my_other_category)
    )
