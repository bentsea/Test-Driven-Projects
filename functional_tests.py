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

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def enter_new_ingredient(self,ingredient_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(ingredient_text)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

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
        self.enter_new_ingredient('1Lb chopped human liver')

        #There is still a text box inviting the user to add another item. They enter 'Minced finger tips'
        self.enter_new_ingredient('3oz Minced finger tips')


        #The page updates, and now shows both items on her list.
        self.check_for_row_in_list_table('1: 1Lb chopped human liver')
        self.check_for_row_in_list_table('2: 3oz Minced finger tips')
        self.fail("Finish the test!")

        #The page updates again, and now both ingredients appear on the list.
        [...]



if __name__ == '__main__':
    unittest.main(warnings="ignore")
