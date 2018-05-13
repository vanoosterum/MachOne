from splinter import Browser
import time
import unittest


class TestLogin(unittest.TestCase):
    def test_Log(self):
        username = 'DDAVIES'
        password = 'DDAVIES'

        browser = Browser('chrome')
        url = "http://qlv5-fe-qa.azurewebsites.net"

        browser.visit(url)

        if browser.is_text_present('Login', wait_time=15):
            f = open("test.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Navigation Passed. \n")
            browser.find_by_id('username').fill(username)
            browser.find_by_id('password').fill(password)
            browser.find_by_text('Login').first.click()

            if browser.is_text_present('Dashboard', wait_time=10):
                f = open("logn.txt", "w")
                f.write(time.strftime("%c"))
                f.write(" Log In Passed. \n")
                f.close()
            else:
                f = open("logn.txt", "w")
                f.write(time.strftime("%c"))
                f.write(" Log In Failed. \n")
                f.close()
        else:
            browser.quit()
            f = open("test.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Navigation Failed. \n")
            f.close()