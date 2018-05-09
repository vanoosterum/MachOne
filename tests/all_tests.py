import base_test


class TestCases(base_test.BaseTest):

    def test_login(self):
        assert self.loginpage.login(self.homepage, "DDAVIES", "DDAVIES")
        assert self.homepage.logout(self.loginpage)
