Feature: Loggin in with valid credentials

Scenario Outline: User search information in Google

    Given I open "https://www.google.pl/" webside
    When I type <phrase>
    And I click on search
    Then I should see <result>

Examples:
    | phrase          | result                    |
    | "I love Python" | "Why I Love Python"       |
    | "Python"        | "Welcome to Python.org"   |
    | "Żaneta Ranosz" | "Kapela Jedlicki"         |
#
#    Scenario: User search information in Google
#
#    Given I open "https://www.google.pl/" webside
#    When I type "I love Python"
#    And I click on search
#    Then I should see "Why I Love Python"
