from splinter import Browser
import unittest


class TestLogin(unittest.TestCase):
    def test_Log(self):
        username = 'DDAVIES'
        password = 'DDAVIES'

        browser = Browser('chrome')
        url = "http://qlv5-fe-qa.azurewebsites.net"

        browser.visit(url)

        if browser.is_text_present('Login', wait_time=15):
            browser.find_by_id('username').fill(username)
            browser.find_by_id('password').fill(password)
            browser.find_by_text('Login').first.click()