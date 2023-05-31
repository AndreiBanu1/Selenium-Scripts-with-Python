Feature: CucumberJava
  Scenario Outline: Login functionality exists
  Given User have opened the browser
  When User have opened EasyTesting website
  When User entered username as "‹username>" and password as "<password>"
  Then Login button should exist
  Examples:
    | username                      | password  |
    | Andrei_Cristian93@gmail.com   | Andrei132 |
    | Adrian_Alexandru555@gmail.com | Adrian112 |