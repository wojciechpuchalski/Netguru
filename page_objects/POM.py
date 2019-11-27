from utilities.setup import driver
from selenium.webdriver.common.keys import Keys


class HomePage(object):

    def __init__(self):
        self.driver = driver

    def go_to_job_offers(self):
        job_offers = self.driver.find_element_by_partial_link_text("Oferty pracy").click()


class JobOffersPage(object):

    def __init__(self):
        self.driver = driver

    def search_for_job(self):
        search_input = self.driver.find_element_by_class_name("Search-userInput-3YZ")
        search_input.send_keys("UI/UX")
        search_input.send_keys(Keys.ENTER)

    def verify_returned_offers(self):
        offer_description = self.driver.find_element_by_class_name("JobCard-jobCard-yoE")
        offer_description.text()
