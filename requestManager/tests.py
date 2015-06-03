from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(LiveServerTestCase):
    fixtures = ['request_data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        #cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_search(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/request/'))
        q = self.selenium.find_element_by_name("q")
        q.send_keys('TC7')
        q.submit()

    def test_create(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/create/'))
        q = self.selenium.find_element_by_name("title")
        q.send_keys('Data Structures')
        q = self.selenium.find_element_by_name("author")
        q.send_keys('Evangel Quiwa')
        q = self.selenium.find_element_by_name("edition")
        q.send_keys('2nd')
        q.submit()
        



