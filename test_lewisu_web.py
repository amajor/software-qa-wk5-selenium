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

    # User must be able to search for “Omari” and get results.
    def test_faculty_directory_search(self):
        driver = self.driver
        driver.get("https://www.lewisu.edu/facstaffdirectory/FacStaffDir2.htm")

        # Look for the search input field
        elem = driver.find_element_by_name("last")

        # Type in "Omari" and submit
        elem.send_keys("Omari")
        elem.send_keys(Keys.RETURN)

        # Assert that you get back a record for Dr. Omari.
        assert "No records" not in driver.page_source
        assert "Omari, Dr. Safwan" in driver.page_source
        assert "Associate Professor" in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
