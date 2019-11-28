from utilities.setup import driver
from page_objects.locators.home_page_locators import HomePageLocators


class HomePage(object):

    def __init__(self):
        self.driver = driver

    def go_to_job_offers(self):
        job_offers = self.driver.find_element(*HomePageLocators.job_offers_link)
        job_offers.click()


