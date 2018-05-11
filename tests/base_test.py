import unittest
from utils import Parameters
from login_page import LoginPage
from home_page import HomePage


class BaseTest(unittest.TestCase):
    param = Parameters()
    loginpage = LoginPage(param.w, param.url)
    homepage = HomePage(param.w, param.url)

    def setUp(self):
        self.param.w.visit(self.param.url)
        assert self.loginpage.check_page()

    @classmethod
    def tearDownClass(cls):
        cls.param.w.quit()