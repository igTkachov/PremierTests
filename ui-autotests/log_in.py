import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from lib.steps import *


@pytest.fixture(scope='function', autouse=True)
def st(run_browser):
    if run_browser == 'firefox':
        f_options = FirefoxOptions()
        f_options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=f_options)
    else:
        ch_options = ChromeOptions()
        ch_options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=ch_options)
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 5)
    driver.implicitly_wait(10)
    return Steps(driver)


def pytest_generate_tests(metafunc):
    browsers = metafunc.config.getoption("browser")
    if "run_browser" in metafunc.fixturenames:
        metafunc.parametrize("run_browser", browsers)


@pytest.mark.usefixtures("st")
@pytest.fixture(scope='function', autouse=True)
def driver(st):
    yield
    st.driver.close()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should not be able to log in with valid username and incorrect password")
def test_not_log_in_with_valid_username_and_incorrect_password(st):
    st.open_log_in_page()
    st.provide_email('itkachov@test.com')
    st.provide_password('not_valid_pass')
    st.login_click()
    st.check_login_error_message()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should not be able to log in with unregistered username and valid password")
def test_not_log_in_with_unregistered_username_and_valid_password(st):
    st.open_log_in_page()
    st.provide_email('valid_email@test.com')
    st.provide_password('test12345')
    st.login_click()
    st.check_login_error_message()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should not be able to log in with password of another registrated users")
def test_not_log_in_with_password_of_another_registrated_users(st):
    st.open_log_in_page()
    st.provide_email('itkachov@test.com')
    st.provide_password('other_password')
    st.login_click()
    st.check_login_error_message()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should not be able to log in with empty email and empty password")
def test_not_log_in_with_empty_email_and_empty_password(st):
    st.open_log_in_page()
    st.login_click()
    st.check_email_error_message()
    st.check_password_error_message()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should not be able to log in with empty email and valid password")
def test_not_log_in_with_empty_email_and_valid_password(st):
    st.open_log_in_page()
    st.provide_password('test12345')
    st.login_click()
    st.check_email_error_message()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should not be able to log in with valid email and empty password")
def test_not_log_in_with_valid_email_and_empty_password(st):
    st.open_log_in_page()
    st.provide_email('itkachov@test.com')
    st.login_click()
    st.check_password_error_message()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should not be able to log in with type valid email as password and valid password as email")
def test_not_log_in_with_revers_credentials(st):
    st.open_log_in_page()
    st.provide_email('valid_pass')
    st.provide_password('itkachov@test.com')
    st.login_click()
    st.check_login_error_message()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should be able to log in with valid email and password (no happy path data)")
def test_log_in_with_valid_email_and_password():
    '''Can't be done due to lack of permissions'''


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should be able to log in using type or enter buttons (no happy path data)")
def test_log_in_with_right_credentials_use_keyboard(st):
    '''Can't be done due to lack of permissions'''
