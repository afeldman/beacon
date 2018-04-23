Feature: Start Beacon with daimler id
  It starts the test using the daimler company ID 0x017c
  
  Scenario: Start with 017c
    Given I have a key of "01" and "7c"
    When I build Beacon
    Then I receive 0
