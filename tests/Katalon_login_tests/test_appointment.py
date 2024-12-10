import allure
import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.page_objects.home_page import HomePage
from tests.page_objects.login_page import LogInPage
from tests.page_objects.appointment_page import AppointmentPageClass
from tests.page_objects.appointment_confirmation_page import AppointmentConfirmationPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    return driver


@allure.title("Appointment Confirmation")
@allure.description("Comment added while booking appointment is correctly added or not")
@pytest.mark.positive
# def test_katalon_appointment_comment(setup):
# driver = setup
#
# homePage = HomePage(driver)
# homePage.make_appointment_click()
#
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "txt-username")))
#
# loginPage = LogInPage(driver)
#
# demo_username = loginPage.get_demo_username()
# demo_password = loginPage.get_demo_password()
#
# loginPage.login_katalon(username=demo_username, password=demo_password)
#
#
# # Check if the login button exists in the DOM
# login_button = driver.find_element(By.ID, "btn-login")
# print(f"Login Button: {login_button.is_displayed()}")  # Prints if the login button is visible
# print(f"Login Button Text: {login_button.text}")
# driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btn-login"))).click()
# WebDriverWait(driver, 20).until(EC.title_contains("appointment"))
# assert "appointment" in driver.title
#
# time.sleep(5)
def test_katalon_appointment_comment(setup):
    driver = setup

    # Navigate to the home page and initiate appointment
    homePage = HomePage(driver)
    homePage.make_appointment_click()

    # Wait for the login form to be visible (wait for username input field)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "txt-username")))

    # Create an instance of the LoginPage
    loginPage = LogInPage(driver)

    # Get the demo username and password dynamically
    demo_username = loginPage.get_demo_username()
    demo_password = loginPage.get_demo_password()

    # Perform login with the retrieved credentials
    loginPage.login_katalon(username=demo_username, password=demo_password)

    # Wait for appointment page to load
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "combo_facility")))

    # Initiating appointment page
    appointmentPage = AppointmentPageClass(driver)

    # select a facility
    appointmentPage.select_facility("Seoul CURA Healthcare Center")
    time.sleep(5)

    # Assert that selected options is correct.
    dropdown_element = driver.find_element(*AppointmentPageClass.dropdown)
    dropdown = Select(dropdown_element)
    selected_option = dropdown.first_selected_option.text
    assert selected_option == "Seoul CURA Healthcare Center", f"Expected option is 'Seoul CURA Healthcare Center', but got this {selected_option}"

    # Select a health program
    appointmentPage.health_radio_option("Medicaid")
    time.sleep(5)

    # Assert that correct radio button value is selected.
    health_radio_elements = driver.find_elements(*AppointmentPageClass.health_radio)
    selected_radio_value = None
    for radio in health_radio_elements:
        if radio.is_selected():
            selected_radio_value = radio.get_attribute("value")
            break
    assert selected_radio_value == "Medicaid", f"Expected selection is 'Medicaid', but got this {selected_radio_value}"

    # Select visit date
    appointmentPage.visit_date_select("15")
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_value((By.ID, "txt_visit_date"), "15"))

    # Comment added
    appointmentPage.comment_message("New message")
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_value((By.ID, "txt_comment"), "New message"))

    # appointment booked
    appointmentPage.book_appointment_click()

    # Confirm appointment
    appointmentConfirmationPage = AppointmentConfirmationPage(driver)

    # Assert that comment is correctly displayed.

    comment_text = appointmentConfirmationPage.comment_conf_message_txt()
    assert comment_text == "New message", f"Another message added."

    appointmentConfirmationPage.menu_toggle_click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='authenticate.php?logout']")))
    appointmentConfirmationPage.logout_button_click()
    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(5)









