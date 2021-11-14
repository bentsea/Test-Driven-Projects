from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #They get frustrated and exit quit out of the entire browser angry.
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #David heard about a cool new online recipe site. They go to check out its  homepage.
        self.browser.get('http://localhost:8000')


        #They notice the page title and header mention it's a cooking project.
        self.assertIn("Cooking Project",self.browser.title)
        self.fail("Finish the test!")



if __name__ == '__main__':
    unittest.main(warnings="ignore")
