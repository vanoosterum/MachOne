from page_objects import PageObject, PageElement


class LoginPage(PageObject):


    def check_page(self):
        return "Authentication" in self.w.title