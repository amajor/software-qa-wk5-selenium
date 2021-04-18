import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestLewisUniversityWebsite(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    # Tile of the homepage must include “Lewis University”
    def test_homepage_tile(self):
        driver = self.driver
        driver.get("https://www.lewisu.edu")
        self.assertIn("Lewis University", driver.title)

    # Home page must include the following links:
    # About Us, Academics, Admission and Aid, Athletics, Student Life, Locations
    @parameterized.expand([
        ("About Us link", "About Us"),
        ("Academics link", "Academics"),
        ("Admission & Aid link (only 'Admission')", "Admission"),
        ("Admission & Aid link (only 'Aid')", "Aid"),
        ("Athletics link", "Athletics"),
        ("Student Life link", "Student Life"),
        ("Locations link", "Locations")
    ])
    def test_homepage_links(self, name, link_text):
        driver = self.driver
        driver.get("https://www.lewisu.edu")

        # Confirm that link is clickable (will raise exception if it is not!)
        driver.find_element_by_partial_link_text(link_text).click()

        # Page source includes the text for the link.
        assert link_text in driver.page_source

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


if __name__ == "__main__":
    unittest.main()
