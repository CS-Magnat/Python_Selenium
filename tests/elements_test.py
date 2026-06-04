import time

from pages.elements_page import TextBoxPage


class TestElement:

    def test(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()
        text_box_page.fill_all_fields()
        print(text_box_page.check_field_form())
        time.sleep(5)
