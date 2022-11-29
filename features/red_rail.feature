Feature: RedRail Train module
  Scenario: Verify user is able to enter station and click on upi payment
    Given Open the browser and enter valid url
    When Click on redrail
    And Enter from station
    And Enter to station
    And Click on date-picker and enter the date
    And Click on search button
    And Select desired train class
    When Click on go ahead button
    And Click on irctc username and Enter irctc username and verify the username
    And Click on add new passenger button and enter passenger details
    And Enter email id
    And Enter phone no
    When Click on proceed button
    And Click on upi and enter upi id and verify it
    And Close the browser
    Then Redrail module is functionally stable

