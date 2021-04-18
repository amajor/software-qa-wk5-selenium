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

    # Home page must include the following links:
    # About Us, Academics, Admission and Aid, Athletics, Student Life, Locations
    def test_homepage_links(self):
        driver = self.driver
        driver.get("https://www.lewisu.edu")

        # Includes "About Us"
        assert "About Us" in driver.page_source

        # Includes "Academics"
        assert "Academics" in driver.page_source

        # Includes "Admission & Aid"
        assert "Admission &amp; Aid" in driver.page_source

        # Includes "Athletics"
        assert "Athletics" in driver.page_source

        # Includes "Student Life"
        assert "Student Life" in driver.page_source

        # Includes "Locations"
        assert "Locations" in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
