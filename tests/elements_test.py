import time

from pages.elements_page import TextBoxPage, CheckBoxPage


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
        time.sleep(5)


