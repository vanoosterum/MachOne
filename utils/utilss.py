from splinter import Browser


class Parameters:
    url = "http://qlv5-fe-qa.azurewebsites.net"
    browser = Browser('chrome')
    username = 'DDAVIES'
    password = 'DDAVIES'
    client = 'Johnson'
    nameinput = 'Helma van Oosterum'
    emailinput = 'helma.vanoosterum@aareon.co.uk'
    editclient = '/html/body/ql-app-root/main/div/ql-workspace/div/div/div/ql-client-dashboard/div/div[1]/' \
                 'ql-client-info/div/div/div/div[1]/div/a/i'