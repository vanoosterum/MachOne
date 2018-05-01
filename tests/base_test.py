import unittest
from utils import Parameters
from login_page import LoginPage


class BaseTest(unittest.TestCase):
    param = Parameters()
    loginpage = LoginPage(param.w, param.rootUrl)

    def test_setUp(self):
        self.param.w.get(self.param.rootUrl)
        assert self.loginpage.check_page()
