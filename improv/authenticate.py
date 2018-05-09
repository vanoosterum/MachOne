from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import unittest
class myLoginclass(unittest.TestCase):
    @classmethod
    def test_TC_1_login_page(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.gmail.com')
        self.driver.find_element_by_xpath(".//*[@id='name-group']/input").send_keys("HELLO")
        self.driver.find_element_by_xpath(".//*[@id='password-group']/input").send_keys("WORLD")
        self.driver.find_element_by_id("loginButton").click()

if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)