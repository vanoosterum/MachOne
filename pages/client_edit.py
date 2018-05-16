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

    def test_ClientEdit(self):
        self.param.browser.is_text_present('Dashboard', wait_time=10)
        self.param.browser.wait_time = 30
        self.param.browser.find_link_by_partial_text(self.param.client).first.click()
        self.param.browser.wait_time = 30
        if self.param.browser.is_text_present('Client', wait_time=40):
            f = open("dashb.txt", "w")
            f.write("***View Client Dashboard*** \n")
            f.write(time.strftime("%c"))
            f.write(" PASS \n")
            f.close()
            self.param.browser.wait_time = 20
            self.param.browser.find_by_xpath(self.param.editclient).first.click()
            if self.param.browser.is_text_present('Personal Information', wait_time=25):
                f = open("dashb.txt", "a")
                f.write("***Open Client Edit Screen*** \n")
                f.write(time.strftime("%c"))
                f.write(" PASS \n")
                f.close()
            else:
                self.param.browser.quit()
                f = open("dashb.txt", "a")
                f.write(time.strftime("%c"))
                f.write(" Edit Client Not Displayed. \n")
                f.close()
            self.param.browser.find_by_xpath(self.param.editclstitle).first.click()
            self.param.browser.find_by_xpath(self.param.editcltitle).first.click()
            self.param.browser.find_by_name('forename').fill(self.param.editclfname)
            self.param.browser.find_by_name('surname').fill(self.param.editclsname)
            self.param.browser.wait_time = 10
            self.param.browser.find_by_xpath('//*[@id="ngb-panel-1-header"]/a/div').first.click()
            if self.param.browser.is_text_present('Short Name', wait_time=10):
                self.param.browser.find_by_name('shortname').fill(self.param.clsname)
                f = open("dashb.txt", "a")
                f.write("***View More Client Data*** \n")
                f.write(time.strftime("%c"))
                f.write(" PASS \n")
                f.close()
            else:
                f = open("dashb.txt", "a")
                f.write("***View More Client Data*** \n")
                f.write(time.strftime("&c"))
                f.write(" FAIL \n")
                f.close()
            self.param.browser.find_by_name('telephoneNumber').fill(self.param.cltelno)
            self.param.browser.find_by_name('email').fill(self.param.clemail)
            self.param.browser.find_by_xpath(self.param.clientsave).first.click()
            self.param.browser.is_text_present('client', wait_time=15)
            self.param.browser.wait_time = 20
            if self.param.browser.is_text_present(self.param.editclsname):
                f = open("dashb.txt", "a")
                f.write("***Save Client Changes*** \n")
                f.write(time.strftime("&c"))
                f.write(" PASS \n")
                f.close()
            else:
                f = open("dashb.txt", "a")
                f.write("***Save Client Changes*** \n")
                f.write(time.strftime("&c"))
                f.write(" FAIL \n")
                f.close()
        else:
            self.param.browser.quit()
            f = open("dash.txt", "w")
            f.write(time.strftime("%c"))
            f.write(" Client Dashboard Not Displayed. \n")
            f.close()
