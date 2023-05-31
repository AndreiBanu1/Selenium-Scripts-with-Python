Feature: CucumberPython

  Scenario: Login functionality exists
    Given User have opened the browser
    When User have opened EasyTesting website
    When User entered username as "Alchemytraining123@gmail.com"
    Then Login button should exist
