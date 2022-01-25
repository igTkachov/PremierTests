from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture
# def test_valid_username_incorrect_password():
#     open_log_in_page()
#     provide_email('itkachov@test.com')
#     provide_password('xxxxxxx')
#     login_click()
#     check_login_error_message()


def init_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 5)
    driver.implicitly_wait(10)
    return driver


def open_log_in_page():
    driver.get('https://sandbox-dashboard.primer.io/login')
    # wait till page loaded and log in button will be displayed
    driver.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'button[data-test=\'button-submit\']')))
    driver.get_screenshot_as_file('screenshots/test_valid_username_incorrect_password/open_log_in_page_step.png')


def provide_email(email):
    email_field = driver.wait.until(EC.presence_of_element_located(
        (By.ID, 'username')))
    email_field.send_keys(email)
    driver.get_screenshot_as_file('screenshots/test_valid_username_incorrect_password/provide_email_step.png')


def provide_password(password):
    pass_field = driver.wait.until(EC.presence_of_element_located(
        (By.ID, 'password')))
    pass_field.send_keys(password)
    driver.get_screenshot_as_file('screenshots/test_valid_username_incorrect_password/provide_password_step.png')


def login_click():
    login_button = driver.find_element_by_css_selector('button[data-test=\'button-submit\']')
    login_button.click()
    driver.get_screenshot_as_file('screenshots/test_valid_username_incorrect_password/login_click_step.png')


def check_login_error_message():
    exp_err_message = 'Incorrect username or password'
    act_err_message = driver.wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[data-test=\'component-Errors\']'))).text
    print('Expected error message: %s', exp_err_message)
    print('Actual error message: %s', act_err_message)
    driver.get_screenshot_as_file('screenshots/test_valid_username_incorrect_password/check_login_error_message_step.png')
    assert exp_err_message == act_err_message, 'Log in error message is not equal'


if __name__ == "__main__":
    driver = init_driver()
    open_log_in_page()
    provide_email('itkachov@test.com')
    provide_password('xxxxxxx')
    login_click()
    check_login_error_message()
    driver.quit()
