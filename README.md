Introduction
------------

This repository contains site tests https://health-diet.ru using a page object template
using Selenium and Python with (Pytest + Selenium + Allure)




How To Run Tests
----------------

1) Install all requirements:

    ```
    pip install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```
    pytest -v -s  {path_to_tests}
    ```
    With Allure
    ```
    pytest -v -s --alluredir=%allure_result_folder% ./tests
    allure serve %allure_result_folder%
    ```

