Feature: CucumberPython

  Scenario: Login functionality exists
    Given User have provided the credentials
    Then Verify the password
    Then Verify the username
