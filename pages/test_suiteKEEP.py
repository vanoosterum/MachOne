import unittest
from utilss import Parameters
import time


class TestLogIn(unittest.TestCase):
    param = Parameters

    def setUp(self):
        self.param.browser.visit(self.param.url)
        self.param.browser.find_by_name('username').fill(self.param.username)
        self.param.browser.find_by_name('password').fill(self.param.password)
        self.param.browser.find_by_text('Login').first.click()

    def test_FeedBack(self):
        nameinput = 'Helma van Oosterum'
        emailinput = 'helma.vanoosterum@aareon.co.uk'

        self.param.browser.is_text_present('Dashboard', wait_time=15)
        self.param.wait_time = 30
        self.param.browser.find_by_text('Feedback').first.click()

        if self.param.browser.is_text_present('opinion', wait_time=10):
            self.param.browser.find_by_id('nameInput').fill(nameinput)
            self.param.browser.find_by_id('emailInput').fill(emailinput)
            f = open("fback.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Feedback Form PASSED. \n")
            f.close()
        else:
            f = open("fback.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Feedback Form FAILED. \n")
            f.close()