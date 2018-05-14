import unittest
from splinter import Browser
import time


class TestFeedBack(unittest.TestCase):
    def test_Feedb(self):
        browser = Browser('chrome')
        url = "http://qlv5-fe-qa.azurewebsites.net"
        browser.visit(url)
        browser.find_by_name('username').fill("DDAVIES")
        browser.find_by_name('password').fill("DDAVIES")
        browser.find_by_text('Login').first.click()

        nameinput = 'Helma van Oosterum'
        emailinput = 'helma.vanoosterum@aareon.co.uk'

        browser.is_text_present('Dashboard', wait_time=15)
        browser.wait_time = 30
        browser.find_by_text('Feedback').first.click()

        if browser.is_text_present('opinion', wait_time=10):
            browser.find_by_id('nameInput').fill(nameinput)
            browser.find_by_id('emailInput').fill(emailinput)
            f = open("fback.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Feedback Form PASSED. \n")
            f.close()
        else:
            f = open("fback.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Feedback Form FAILED. \n")
            f.close()
