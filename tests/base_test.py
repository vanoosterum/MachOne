import unittest

import utils
from login_page import LoginPage
from home_page import HomePage


class BaseTest (unittest.TestCase):
    param = utils.Parameters()
    loginpage = LoginPage(param.w, param.rootUrl)
    homepage = HomePage(param.w, param.rootUrl)

    def setUp(self):
        self.param.w.get(self.param.rootUrl)
        #       assert self.loginpage.check_page()
