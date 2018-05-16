import unittest
from utilss import Parameters

import time


class TestLogIn(unittest.TestCase):
    param = Parameters

    def setUp(self):
        self.param.browser.visit(self.param.url)
        self.param.browser.wait_time = 10
        self.param.browser.driver.maximize_window()
        self.param.browser.find_by_name('username').fill(self.param.username)
        self.param.browser.find_by_name('password').fill(self.param.password)
        self.param.browser.find_by_text('Login').first.click()
        self.param.browser.wait_time = 30
        self.param.browser.find_link_by_partial_text(self.param.client).first.click()
        self.param.browser.wait_time = 30
        if self.param.browser.is_text_present('Client', wait_time=20):
            f = open("claddress.txt", "w")
            f.write("***View Client Dashboard*** \n")
            f.write(time.strftime("%c"))
            f.write(" PASS \n")
            f.close()
            self.param.browser.wait_time = 20
            self.param.browser.find_by_xpath(self.param.editclient).first.click()
            if self.param.browser.is_text_present('Personal Information', wait_time=25):
                f = open("claddress.txt", "a")
                f.write("***Open Client Edit Screen*** \n")
                f.write(time.strftime("%c"))
                f.write(" PASS \n")
                f.close()
            else:
                f = open("claddress.txt", "a")
                f.write("***Open Client Edit Screen*** \n")
                f.write(time.strftime("%c"))
                f.write(" FAIL - Tests Aborted \n")
                f.close()
        else:
            self.param.browser.quit()
            f = open("claddress.txt", "w")
            f.write("***View Client Dashboard*** \n")
            f.write(time.strftime("%c"))
            f.write(" FAIL - Tests Aborted \n")
            f.close()

    def test_ClientAddressEdit(self):
        self.param.browser.wait_time = 20
        self.param.browser.find_by_xpath(self.param.coradd).first.click()
        if self.param.browser.is_text_present('Search Addresses'):
            f = open("claddress.txt", "a")
            f.write("***Search Addresses Modal Displayed*** \n")
            f.write(time.strftime("%c"))
            f.write(" PASS \n")
            f.close()
        else:
            f = open("claddress.txt", "a")
            f.write("***Search Addresses Modal Displayed*** \n")
            f.write(time.strftime("%c"))
            f.write(" FAIL - Tests aborted \n")
            f.close()
        self.param.browser.find_by_xpath(self.param.addsearch).fill(self.param.addscrit)
        self.param.browser.wait_time = 40
        if self.param.browser.is_text_present(self.param.addverify):
            f = open("claddress.txt", "a")
            f.write("***Address found*** \n")
            f.write(time.strftime("%c"))
            f.write(" PASS \n")
            f.close()
        else:
            self.param.browser.quit()
            f = open("claddress.txt", "a")
            f.write("***Address found*** \n")
            f.write(time.strftime("%c"))
            f.write(" FAIL - Tests aborted \n")
            f.close()
        self.param.browser.find_by_xpath(self.param.addselect).first.click()
        self.param.browser.wait_time = 40
        self.param.browser.find_by_xpath(self.param.clientsave).first.click()
        self.param.browser.is_text_present('client', wait_time=15)
        self.param.browser.wait_time = 20
        if self.param.browser.is_text_present(self.param.addverify):
            f = open("claddress.txt", "a")
            f.write("***Address Selected*** \n")
            f.write(time.strftime("%c"))
            f.write(" PASS \n")
            f.close()
        else:
            self.param.browser.quit()
            f = open("claddress.txt", "a")
            f.write("***Address Selected*** \n")
            f.write(time.strftime("%c"))
            f.write(" FAIL - Tests aborted \n")
            f.close()