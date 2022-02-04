from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure


class LoginPageElements:

    LOGIN = 'button[data-test=\'button-submit\']'
    USER = 'username'
    PASS = 'password'
    INCORRECT_ERROR_MESSAGE = 'div[data-test=\'component-Errors\']'
    FILL_IN_ERROR_MESSAGE = '.List__Root-sc-icriza-0 div[class^=\'Text__Root\']'
    EXP_ERROR_MESSAGE = 'Please fill in this field'


class Steps:

    def __init__(self, driver: webdriver):
        self.driver = driver

    @allure.step('Open log in page')
    def open_log_in_page(self):
        self.driver.get('https://sandbox-dashboard.primer.io/login')
        # wait till page loaded and log in button will be displayed
        self.driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, LoginPageElements.LOGIN)))
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot for open_log_in_page", attachment_type=AttachmentType.PNG)

    @allure.step('Provide email')
    def provide_email(self, email):
        email_field = self.driver.wait.until(EC.presence_of_element_located(
            (By.ID, LoginPageElements.USER)))
        email_field.send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot for provide_email", attachment_type=AttachmentType.PNG)

    @allure.step('Provide password')
    def provide_password(self, password):
        pass_field = self.driver.wait.until(EC.presence_of_element_located(
            (By.ID, LoginPageElements.PASS)))
        pass_field.send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot for provide_password", attachment_type=AttachmentType.PNG)

    @allure.step('Click log in')
    def login_click(self):
        login_button = self.driver.find_element_by_css_selector(LoginPageElements.LOGIN)
        login_button.click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot for login_click", attachment_type=AttachmentType.PNG)

    @allure.step('Check log in error message')
    def check_login_error_message(self):
        exp_err_message = 'Incorrect username or password'
        act_err_message = self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, LoginPageElements.INCORRECT_ERROR_MESSAGE))).text
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot for check_login_error_message", attachment_type=AttachmentType.PNG)
        assert exp_err_message == act_err_message, 'Log in error message is not equal'

    @allure.step('Check email error message')
    def check_email_error_message(self):

        act_err_message = self.driver.wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, LoginPageElements.FILL_IN_ERROR_MESSAGE)))[0].text
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot for check_email_error_message", attachment_type=AttachmentType.PNG)
        assert LoginPageElements.EXP_ERROR_MESSAGE == act_err_message, 'Fill in error message is not equal'

    @allure.step('Check password error message')
    def check_password_error_message(self):
        act_err_message = self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, LoginPageElements.FILL_IN_ERROR_MESSAGE))).text
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot for check_password_error_message", attachment_type=AttachmentType.PNG)
        assert LoginPageElements.EXP_ERROR_MESSAGE == act_err_message, 'Fill in error message is not equal'
