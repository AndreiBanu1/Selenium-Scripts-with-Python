Feature: Google Search
  Scenario Outline: Search functionality exists
    Given User have opened the browser
    When User have opened Google webpage and verify the title
    When User entered Text as "‹Data›" to search
    Examples:
      | Data   |
      | <Hello world> |