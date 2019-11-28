from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.setup import driver
from page_objects.locators.creative_page_locators import CreativeCloudLocators


class CreativeCloudPage(object):

    def __init__(self):
        self.driver = driver

    def polish_version(self):
        go_to_polish_version_link = self.driver.find_element(*CreativeCloudLocators.go_to_polish_version)
        go_to_polish_version_link.click()
