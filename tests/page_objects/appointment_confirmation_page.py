# Page class
# Page locators
# Page Actions
# Webdriver initializations
# Custom functions
# No assertions (in page object class)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class AppointmentConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    comment_confirmation = (By.XPATH, "//p[@id='comment']")
    menu_toggle = (By.ID, "menu-toggle")
    logout_button = (By.XPATH, "//a[@href='authenticate.php?logout']")

    def comment_conf_message(self):
        return self.driver.find_element(*AppointmentConfirmationPage.comment_confirmation)

    def comment_conf_message_txt(self):
        return self.comment_conf_message().text

    def menu_toggle_click(self):
        menu_toggle_element = self.driver.find_element(*AppointmentConfirmationPage.menu_toggle)
        menu_toggle_element.click()

    def logout_button_click(self):
        logout_element = self.driver.find_element(*AppointmentConfirmationPage.logout_button)
        logout_element.click()
