import base_test


class TestCases(base_test.BaseTest):
    def test_01_test_login_page_login(self):
        assert self.loginpage.login(self.homepage, "DDAVIES", "DDAVIES")
