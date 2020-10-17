@partners
  Feature: The feature is example to create scenarios using Partners api

    @test
    Scenario: Create partner
      Given I wanna create partner
      And   The id is random
      And   The trading name is Adega Osasco
      And   The owner name is Dunha
      And   The document is random
      And   The address is 20.01 and 20.02
      And   The coverage area is '20.01, 20.01, 45.01, 40.01, 20.01'
      When  I send request to create partners
      Then  The result response code should be 200
      And   The result body must be:
            | id          | 123            |
            | tradingName | Adega Osasco   |

      @test2
      Scenario Outline: Create multiples partners
        Given I wanna create partner
        And   The id is <id>
        And   The trading name is <tradingName>
        And   The owner name is <ownerName>
        And   The document is <document>
        And   The address is <log> and <lat>
        And   The coverage area is <coverageArea>
        When  I send request to create partners
        Then  The result response code should be <code>
        Examples:
          | id     | tradingName | ownerName| document | log   | lat   | coverageArea                        | code |
          | random | tn1         | on1      | random   | 20.01 | 20.02 | '20.01, 20.01, 45.01, 40.01, 20.01' | 200  |
          | random | tn2         | on2      | random   | 20.01 | 20.02 | '20.01, 20.01, 45.01, 40.01, 20.01' | 200  |






