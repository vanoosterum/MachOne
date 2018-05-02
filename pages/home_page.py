from page_objects import PageObject, PageElement


class HomePage(PageObject):
    def check_page(self):
        return "QLWebApp" in self.w.title