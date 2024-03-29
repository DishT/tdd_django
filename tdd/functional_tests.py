from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
import time
chrome_options = Options()


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='./chromedriver',
                                        options=chrome_options)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')
        # self.browser.implicitly_wait(3)
        time.sleep(3)
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy peacock feathers" into a text box (Edith's hobby # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists # "1: Buy peacock feathers" as an item in a
        # to-do list table inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))

        self.fail('Finish the test!')
        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]


if __name__ == '__main__':
    unittest.main(warnings='ignore')
