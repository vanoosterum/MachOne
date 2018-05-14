from splinter import Browser


class Parameters():
    def __init__(self):
        self.browser = Browser('chrome')
        self.url = "http://qlv5-fe-qa.azurewebsites.net"
        self.browser.visit(self.url)
        self.browser.find_by_name('username').fill("DDAVIES")
        self.browser.find_by_name('password').fill("DDAVIES")
        self.browser.find_by_text('Login').first.click()