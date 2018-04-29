from selenium import webdriver
class Parameters():
    def__init__(self):
    self.w = webdriver.Chrome('C:\Drivers\chromedriver') # To start Chrome
    self.rootUrl = "http://qlv5-fe-qa.azurewebsites.net/" # To navigate to the Aareon Application
    self.w.implicitly_wait (20) # To allow user to see the progress. Can be commented out for behind the scene tests