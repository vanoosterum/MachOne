import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Drivers\chromedriver') # To start Chrome
driver.get('http://qlv5-fe-qa.azurewebsites.net/') # To navigate to the Aareon Application

time.sleep(20) # To allow user to see the progress. Can be commented out for behind the scene tests