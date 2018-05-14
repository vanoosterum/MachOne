from page_objects import PageObject


class HomePage(PageObject):
    def check_page(self):
        self.w.is_text_present('Dashboard', wait_time=15)