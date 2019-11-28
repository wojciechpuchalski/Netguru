from selenium.webdriver.common.keys import Keys
from utilities.setup import driver
from page_objects.locators.adobe_talent_locators import AdobeTalentLocators


class JobOffersPage(object):

    def __init__(self):
        self.driver = driver

    def buy_now(self):
        buy_now_button = self.driver.find_element(*AdobeTalentLocators.buy_now)
        buy_now_button.click()