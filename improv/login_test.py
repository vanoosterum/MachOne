from splinter import Browser
import time

browser = Browser('chrome')
url = "http://qlv5-fe-qa.azurewebsites.net"

browser.visit(url)

if browser.is_text_present('Login', wait_time=15):
    f = open("test.txt", "w")
    f.write(time.strftime("%c"))
    f.write(" Navigation Passed. \n")
    browser.find_by_name('username').fill("DDAVIES")
    browser.find_by_name('password').fill("DDAVIES")
else:
    browser.quit()
    f = open("test.txt", "w")
    f.write(time.strftime("%c"))
    f.write(" Navigation Failed. \n")
    f.close()

browser.find_by_text('Login').first.click()

if browser.is_text_present('Dashboard', wait_time=15):
    f = open("test.txt", "w")
    f.write(time.strftime("%c"))
    f.write(" Log In Passed. \n")
    f.close()
else:
    browser.quit()
    f = open("test.txt", "a")
    f.write(time.strftime("%c"))
    f.write(" Log In Failed. \n")
    f.close()