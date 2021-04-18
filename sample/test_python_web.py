import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        # The driver represents the web browser
        driver = self.driver

        # Start at the desired web address.
        driver.get("http://www.python.org")

        # Assert that the word "Python" is in the title.
        self.assertIn("Python", driver.title)

        # Look for an element with the name attribute "q"
        # This is the search input field.
        elem = driver.find_element_by_name("q")

        # Type in "pycon"
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        # Assert that you can't find "pycon"
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
