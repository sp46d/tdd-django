from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest


class NewVisitorTest(unittest.TestCase):
    DRIVER_PATH = "/Users/sanghyuk/.local/bin/chromedriver"
    BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.binary_location = self.BRAVE_PATH
        service = Service(executable_path=self.DRIVER_PATH)

        self.browser = webdriver.Chrome(options=option, service=service)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)

        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main()
