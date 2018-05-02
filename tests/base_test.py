import unittest

from home_page import HomePage
from login_page import LoginPage
from utils import Parameters


class BaseTest(unittest.TestCase):
    param = Parameters()
    loginpage = LoginPage(param.w, param.rootUrl)
    homepage = HomePage(param.w, param.rootUrl)

    def setUp(self):
        self.param.w.get(self.param.rootUrl)
