from page_objects import PageObject, PageElement


class LoginPage(PageObject):

    def check_page(self):
        return "QL V5 Authentication" in self.w.title