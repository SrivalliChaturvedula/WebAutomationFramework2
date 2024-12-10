"""
homepage
click on the make appointment button available in this page.
This page should navigate to login page.
"""
# Page class
# Page locators
# Page Actions
# Webdriver initializations
# Custom functions
# No assertions (in page object class)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators

    make_appointment = (By.ID, "btn-make-appointment")

    def get_make_appointment(self):
        return self.driver.find_element(*HomePage.make_appointment)

    def make_appointment_click(self):
        return self.get_make_appointment().click()
