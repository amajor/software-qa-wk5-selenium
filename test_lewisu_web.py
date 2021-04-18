import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # Tile of the homepage must include “Lewis University”
    def test_homepage_tile(self):
        driver = self.driver
        driver.get("https://www.lewisu.edu")
        self.assertIn("Lewis University", driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
