from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = By.CSS_SELECTOR, "button[id='submit']"

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    HOME_SWITCHERS_BUTTONS = (By.CSS_SELECTOR,'span[class ="rc-tree-switcher rc-tree-switcher_close"]')

    DESKTOP_SWITCHERS_BUTTONS = (By.XPATH,"//span[text()='Desktop']/ancestor::div[contains(@class, 'rc-tree-treenode')][1]/span[contains(@class, 'rc-tree-switcher')]")
    DOCUMENTS_SWITCHERS_BUTTONS = (By.XPATH,"//span[text()='Documents']/ancestor::div[contains(@class, 'rc-tree-treenode')][1]/span[contains(@class, 'rc-tree-switcher')]")
    WORK_SPACE_SWITCHERS_BUTTONS = (By.XPATH,"//span[text()='WorkSpace']/ancestor::div[contains(@class, 'rc-tree-treenode')][1]/span[contains(@class, 'rc-tree-switcher')]")
    OFFICE_SWITCHERS_BUTTONS = (By.XPATH,"//span[text()='Office']/ancestor::div[contains(@class, 'rc-tree-treenode')][1]/span[contains(@class, 'rc-tree-switcher')]")
    DOWNLOADS_SWITCHERS_BUTTONS = (By.XPATH,"//span[text()='Downloads']/ancestor::div[contains(@class, 'rc-tree-treenode')][1]/span[contains(@class, 'rc-tree-switcher')]")

    CHECKBOX_HOME = (By.CSS_SELECTOR, 'span[aria-label="Select Home"]')
    ITEM_LIST = (By.CSS_SELECTOR,'span[class ="rc-tree-title"]')

    ALL_CHECKBOXES = (By.CSS_SELECTOR, 'span[class="rc-tree-checkbox"]')

    CHECKED_ALL_CHECKBOX = (By.CSS_SELECTOR, 'span[class="rc-tree-checkbox rc-tree-checkbox-checked"]')
    TITLE_CHECKED_ALL_CHECKBOX = (By.XPATH, "ancestor::div[contains(@class, 'rc-tree-treenode')]//span[@class='rc-tree-title']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'input[id="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'input[id="impressiveRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

class WebTablePageLocators:

    ADD_BUTTON_BUTTON =(By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')

    FIRST_NAME_INPUT= (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[id="submit"]')






