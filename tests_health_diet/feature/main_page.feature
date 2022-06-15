Feature: User is on a main page


    Scenario: The login name corresponds to the user name
    Given I log in under my account on the main page
    When I see login name 
    Then This login name is my <username>

    Examples:
        | username |
        |  Сергей  |
    