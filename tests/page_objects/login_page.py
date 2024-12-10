"""
Login page class
Responsibility:
Get username and send keys - email
get password and send keys - password
Click submit button and navigate to dashboard
Invalid credentials - error message
Forgot password
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


class LogInPage:
    def __init__(self, driver):
        self.driver = driver

    # page locators
    demo_username = (By.XPATH, "//input[@value='John Doe']")
    demo_password = (By.XPATH, "//input[@value='ThisIsNotAPassword']")
    user_name = (By.XPATH, "//input[@id='txt-username']")
    password = (By.XPATH, "//input[@id='txt-password']")
    login = (By.XPATH, "//button[@id='btn-login']")


    # page actions

    def get_username(self):
        return self.driver.find_element(*LogInPage.user_name)

    def get_password(self):
        return self.driver.find_element(*LogInPage.password)

    def get_login(self):
        return self.driver.find_element(*LogInPage.login)

    def get_demo_username(self):
        return self.driver.find_element(*LogInPage.demo_username).get_attribute('value')

    def get_demo_password(self):
        return self.driver.find_element(*LogInPage.demo_password).get_attribute('value')

    # page main action

    def login_katalon(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login().click()

    def login_click(self):
        login_click = self.driver.find_element(*LogInPage.login)
        login_click.click()
