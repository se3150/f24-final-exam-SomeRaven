from behave import given, when, then
from selenium.webdriver.support.ui import Select
import time

@given('I open the url "{url}"')
def step_open_url(context, url):
    context.behave_driver.get(url)

@when('I enter "{value}" in the input field "{field_id}"')
def step_enter_value(context, value, field_id):
    field = context.behave_driver.find_element_by_css_selector(field_id)
    field.clear()
    field.send_keys(value)

@when('I select "{option_text}" from the dropdown "{dropdown_id}"')
def step_select_option(context, option_text, dropdown_id):
    dropdown = Select(context.behave_driver.find_element_by_css_selector(dropdown_id))
    dropdown.select_by_visible_text(option_text)

@when('I click on the button "{button_id}"')
def step_click_button(context, button_id):
    button = context.behave_driver.find_element_by_css_selector(button_id)
    button.click()


@then(u'I pause for {milliseconds}ms')
def step_impl(context, milliseconds):
    # Convert milliseconds to seconds
    delay = int(milliseconds) / 1000.0
    time.sleep(delay)

@then(u'I expect that element "{element_id}" contains the text "{expected_text}"')
def step_verify_text_in_element(context, element_id, expected_text):
    element = context.behave_driver.find_element_by_css_selector(element_id)
    if element is not None:
        element_text = element.text
        print(element_text, "==", expected_text)
        assert expected_text in element_text
    else:
        print("Element not found:", element_id)
