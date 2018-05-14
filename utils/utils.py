from splinter import Browser


browser = Browser('chrome')
url = "http://qlv5-fe-qa.azurewebsites.net"
browser.visit(url)
browser.find_by_name('username').fill("DDAVIES")
browser.find_by_name('password').fill("DDAVIES")