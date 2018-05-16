from splinter import Browser


class Parameters:
    # Login details
    url = "http://qlv5-fe-qa.azurewebsites.net"
    browser = Browser('chrome')
    username = 'DDAVIES'
    password = 'DDAVIES'
    # Select a recent contact by Surname
    client = 'Davies'
    nameinput = 'Helma van Oosterum'
    emailinput = 'helma.vanoosterum@aareon.co.uk'
    # select the edit icon
    editclient = '/html/body/ql-app-root/main/div/ql-workspace/div/div/div/ql-client-dashboard/div/div[1]/' \
                 'ql-client-info/div/div/div/div[1]/div/a/i'
    # select the Title dropdown
    editclstitle = '/html/body/ql-app-root/main/div/ql-workspace/div/div/div/ql-client-quick-edit/div/div[2]/' \
                   'form/div[2]/div[1]/div'
    # Select a new title by option number
    editcltitle = '//*[@id="title"]/option[3]'
    # Edit client details
    editclfname = 'Honest Abe'
    editclsname = 'Lincoln'
    # View More data fields
    clsname = 'THOMJ'
    clinitial = 'T J'
    clwarns = 'Very unpleasant person'
    cltelno = '01656862693'
    clalttel = '02920310952'
    clemail = 'helma.vanoosterum@aareon.com'
    # save button after client edit
    clientsave = '/html/body/ql-app-root/main/div/ql-workspace/div/div/div/ql-client-quick-edit/div/div[2]/' \
                 'form/div[2]/div[11]/button[1]'
    # cancel button after client edit
    clientcancel = '//*[@id="cancel"]'
    # verify client edits have saved. This line compares the header text with the Surname
    dbheader = '/html/body/ql-app-root/main/div/ql-workspace/div/div/div/ql-client-dashboard/div/div[1]/' \
               'ql-client-info/div/div/div/div[1]/h4'
