import random
import time

from generator.generator import generator_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generator_person())

        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        present_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(present_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, present_address

    def check_field_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        present_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, present_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.HOME_SWITCHERS_BUTTONS).click()

        self.element_is_visible(self.locators.DESKTOP_SWITCHERS_BUTTONS).click()

        self.element_is_visible(self.locators.DOCUMENTS_SWITCHERS_BUTTONS).click()
        self.element_is_visible(self.locators.WORK_SPACE_SWITCHERS_BUTTONS).click()
        self.element_is_visible(self.locators.OFFICE_SWITCHERS_BUTTONS).click()

        self.element_is_visible(self.locators.DOWNLOADS_SWITCHERS_BUTTONS).click()


    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ALL_CHECKBOXES)

        for _ in range(len(item_list)):
            item = random.choice(item_list)
            self.go_to_element(item)
            item.click()













