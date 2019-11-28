from selenium.webdriver.common.keys import Keys
from utilities.setup import driver
from page_objects.locators.job_offers_locators import JobOffersLocators



class JobOffersPage(object):

    def __init__(self):
        self.driver = driver

    def search_for_job(self):
        search_input = self.driver.find_element(*JobOffersLocators.search_input)
        search_input.send_keys("UI/UX")
        search_input.send_keys(Keys.ENTER)

    def verify_returned_offers(self):
        offer_description = self.driver.find_element(*JobOffersLocators.offer_description).text
        assert ("UI" in offer_description)
