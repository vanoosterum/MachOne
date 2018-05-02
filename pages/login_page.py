from page_objects import PageObject, PageElement


class LoginPage(PageObject):

    def check_page(self):
        return "Authentication" in self.w.title


username_field = PageElement(id_="username")
password_field = PageElement(id_="password")


def login(self, homepage, username, password):
    self.username_field.send_keys(username)
    self.password_field.send_keys(password)
    self.password_field.submit()
    return homepage.check_page()
