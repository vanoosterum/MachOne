from selenium import webdriver


class Parameters():
    def __init__(self):
        self.w = webdriver.Chrome('C:\Drivers\chromedriver')  # To start Chrome
        self.rootUrl = "http://qlv5-fe-qa.azurewebsites.net/"  # To navigate to the Aareon Application
        # self.w.implicitly_wait(10)