import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElement:

    def test(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        full_name, email, current_address, present_address = text_box_page.fill_all_fields()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()

        assert full_name == output_full_name, "the full name does not match"
        assert email == output_email, "the email does not match"
        assert current_address == output_current_address, "the current address does not match"
        assert present_address == output_permanent_address, "the present address does not match"

class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, "the checked checkboxes do not match the output result"
        time.sleep(5)

class TestRadioButton:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
        radio_button_page.open()
        radio_button_page.click_selected_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        # radio_button_page.click_selected_radio_button("no")
        radio_button_page.element_is_not_clickable(radio_button_page.locators.NO_RADIOBUTTON)
        output_no = radio_button_page.get_output_result()
        radio_button_page.click_selected_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        assert output_yes == "Yes", "'YES' have not been selected"
        assert output_no == "No", "'NO' have not been selected"
        assert output_impressive == "Impressive", "'Impressive' have not been selected"


