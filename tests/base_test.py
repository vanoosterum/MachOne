import unittest
from utils import Parameters
from login_page import LoginPage
from home_page import HomePage


class BaseTest(unittest.TestCase):
    param = Parameters()
    loginpage = LoginPage(param.w, param.rootUrl)
    homepage = HomePage(param.w, param.rootUrl)

    def test_setUp(self):
        self.param.w.get(self.param.rootUrl)
