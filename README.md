# Lab 5: Automating UAT with Selenium

See a screenshot of it all working together in the [summary](./docs/show_its_working.md).

## Readings:

* [Selenium tutorial with Python](https://selenium-python.readthedocs.io/)

In this lab, we will be using the Selenium testing framework to develop automated user acceptance tests. Selenium is an 
open-source web-based automation tool, which can be used to automate various aspects of the User Acceptance Testing 
(UAT) effort. Selenium provides capability to instantiate a browser, simulate user interaction, and test the html 
output.

Your task is to carefully review the tutorial and develop UAT for [Lewis University website](https://www.lewisu.edu).

The UAT must test for the following:
- [x] Tile of the homepage must include “Lewis University”
- [x] Home page must include the following links
  - [x] About Us
  - [x] Academics
  - [x] Admission and Aid
  - [x] Athletics
  - [x] Student Life
  - [x] Locations
- [x] User must be able to navigate to the Faculty/Staff directory from the homepage
- [x] User must be able to search for “Omari” and get results.

## Deliverables:

- [x] [Python test cases](./tests/test_lewisu_web.py).
- [x] [Screenshots](./docs/images/LewisU_SeleniumTests.png) showing that all test cases run successfully.
