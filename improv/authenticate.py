from splinter import Browser

browser = Browser('chrome')
# Visit URL
url = "http://qlv5-fe-qa.azurewebsites.net"
browser.visit(url)
browser.find_by_name('username').fill("DDAVIES")
browser.find_by_name('password').fill("DDAVIES")
browser.find_by_text('Login').first.click()
if browser.is_text_present('Dashboard', wait_time=15):
    browser.find_by_text('DD').first.click()
    if browser.is_text_present('Session', wait_time=10):
        browser.find_by_text('Log Out').first.click()
        f = open("test.txt", "w")  # opens file with name of "test.txt"
        f.write("Log In Passed")
    else:
        f = open("test.txt", "w")  # opens file with name of "test.txt"
        f.write("Log Out Failed")
else:
    f = open("test.txt", "w")  # opens file with name of "test.txt"
    f.write("Log In Failed")
    f.close()