import unittest
from splinter import Browser
import time
from utilss import Parameters


class TestFeedBack(unittest.TestCase):
    param = Parameters

    def test_Feedb(self):
        browser = Browser('chrome')
        url = "http://qlv5-fe-qa.azurewebsites.net"
        browser.visit(url)
        browser.find_by_name('username').fill(self.param.username)
        browser.find_by_name('password').fill(self.param.password)
        browser.find_by_text('Login').first.click()

        browser.is_text_present('Dashboard', wait_time=15)
        browser.wait_time = 30
        browser.find_by_text('Feedback').first.click()

        if browser.is_text_present('opinion', wait_time=10):
            browser.find_by_id('nameInput').fill(self.param.nameinput)
            browser.find_by_id('emailInput').fill(self.param.emailinput)
            f = open("fback.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Feedback Form PASSED. \n")
            f.close()
        else:
            f = open("fback.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Feedback Form FAILED. \n")
            f.close()
