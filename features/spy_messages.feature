Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select "Encode" from the dropdown "#decoder-setting"
    And I select "1" from the dropdown "#shift-amount"
    And I enter "I like dogs" in the input field "#letters" 
    And I click on the button "#submit"
    Then I pause for 2000ms
    Then I expect that element "#decoded_message" contains the text "J mjlf epht"


Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select "Decode" from the dropdown "#decoder-setting"
    And I select "1" from the dropdown "#shift-amount"
    And I enter "J mjlf epht" in the input field "#letters" 
    And I click on the button "#submit"
    Then I pause for 2000ms
    Then I expect that element "#decoded_message" contains the text "I like dogs"



