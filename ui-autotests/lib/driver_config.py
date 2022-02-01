from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class DriverConfig:

    def __init__(self, driver: webdriver, driver_wait: int, implicitly_wait: int):
        self.driver = driver
        self.driver_wait = driver_wait
        self.implicitly_wait = implicitly_wait

        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(driver, driver_wait)
        self.driver.implicitly_wait(implicitly_wait)
