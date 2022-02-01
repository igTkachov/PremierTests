import pytest

from lib.steps import *


@pytest.fixture(scope='session', autouse=True)
def st():
    # dr = DriverConfig(webdriver.Chrome(ChromeDriverManager().install()), 5, 10)
    # yield _driver
    # _driver.quit()
    return Steps()


@allure.epic("Autotests-UI")
@allure.feature("Log in")
@allure.story("Validate Log in flow")
@allure.title("User should be able to log in with valid email and password")
def test_log_in_with_valid_email_and_password():
    '''Can't be done due to lack of permissions'''


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
@allure.title("User should be able to log in using type or enter buttons")
def test_log_in_with_right_credentials_use_keyboard(st):
    '''Can't be done due to lack of permissions'''
