from splinter import Browser

browser = Browser('chrome')
# Visit URL
url = "http://qlv5-fe-qa.azurewebsites.net"
browser.visit(url)
browser.find_by_name('username').fill("DDAVIES")
browser.find_by_name('password').fill("DDAVIES")
browser.find_by_text('Login').first.click()
if browser.is_text_present('Dashboard', wait_time=15):
    print "Login Passed"
else:
    print "Log In Failed"
