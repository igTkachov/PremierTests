from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Browser(object):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.wait = WebDriverWait(driver, 5)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(self):
        self.driver.close()
