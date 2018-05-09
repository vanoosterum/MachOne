import page_objects


class LoginPage(page_objects.PageObject):
    username_field = page_objects.PageElement(id_="username")
    password_field = page_objects.PageElement(id_="password")
    username_and_password_fields = page_objects.MultiPageElement(xpath='//input[@type"text"]')

    # def check_page(self):  #    """

    #   :rtype: object  #   """  # type: () -> object  #   return "QL" in self.w.title


def login(self, homepage, username, password):
    self.username_field.send_keys(username)
    self.password_field.send_keys(password)
    self.password_field.submit()
    return homepage.check_page()


def multi_page_elements_test(self, text):
    self.username_password_fields = text
    return text in self.username_field.get_attribute("value") and text in self.password_field.get_attribute("value")