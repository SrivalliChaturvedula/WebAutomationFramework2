"""
Appointment page class
Responsibility:
Get username and send keys - email
get password and send keys - password
Click submit button and navigate to dashboard
Invalid credentials - error message
Forgot password
"""
from selenium.common import NoSuchElementException
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


class AppointmentPageClass:
    def __init__(self, driver):
        self.driver = driver

    # page locators

    dropdown = (By.ID, "combo_facility")
    health_radio = (By.XPATH, "//label[@class='radio-inline']/input[@type='radio']")
    visit_date = (By.XPATH, "//span[@class='glyphicon glyphicon-calendar']")
    date_select = (By.XPATH, "//td[@class='day' and text()='15']")
    comment_box = (By.XPATH, "//textarea[@placeholder='Comment']")
    book_appointment = (By.ID, "btn-book-appointment")

    # page actions
    def select_facility(self, facility_value):
        # Locate the dropdown element
        dropdown_element = self.driver.find_element(*AppointmentPageClass.dropdown)

        # Create a Select object with the dropdown web element
        select = Select(dropdown_element)

        # Select the option by value
        try:
            select.select_by_value(facility_value)
        except NoSuchElementException:
            print(f"Value '{facility_value}' not found in the dropdown.")

    def health_radio_option(self, radio_value):
        health_radio_elements = self.driver.find_elements(*AppointmentPageClass.health_radio)

        for radio in health_radio_elements:
            if radio.get_attribute("value") == radio_value:
                radio.click()
                break

    def visit_date_select(self, day):
        visit_date_element = self.driver.find_element(*AppointmentPageClass.visit_date)
        visit_date_element.click()

        date_option = (By.XPATH, f"//td[@class='day' and text()='{day}']")
        date_select_element = self.driver.find_element(*date_option)
        if not date_select_element.is_displayed():
            print("Date picker is not displayed. Retrying...")
        date_select_element.click()
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Comment']").click()

    def comment_message(self, message):
        comment_element = self.driver.find_element(*AppointmentPageClass.comment_box)
        comment_element.send_keys(message)

    def book_appointment_click(self):
        book_appointment_element = self.driver.find_element(*AppointmentPageClass.book_appointment)
        book_appointment_element.click()







