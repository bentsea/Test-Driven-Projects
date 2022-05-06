from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Cooking Project",header_text)

        #They are immediately prompted to create a recipe.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a recipe ingredient'
        )

        #They type in 1lb chopped human liver into a text box (their hobby is cannibalism)
        inputbox.send_keys('1Lb chopped human liver')

        #When they hit enter, the page updates , and now the page lists "1. 1Lb chopped human liver" as an ingredient in a recipe.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. 1Lb chopped human liver' for row in rows)
        )

        #There is still a text box inviting the user to add another item. They enter 'Minced finger tips'
        self.fail("Finish the test!")

        #The page updates again, and now both ingredients appear on the list.
        [...]



if __name__ == '__main__':
    unittest.main(warnings="ignore")
