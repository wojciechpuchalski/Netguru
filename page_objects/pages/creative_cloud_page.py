from utilities.setup import driver
from page_objects.locators.creative_cloud_page_locators import CreativeCloudPageLocators


class CreativeCloudPage(object):

    def __init__(self):
        self.driver = driver

    def select_plan(self):
        close = self.driver.find_element(*CreativeCloudPageLocators.go_to_polish_version)
        self.driver.execute_script("arguments[0].click();", close)
        select_plans = self.driver.find_element(*CreativeCloudPageLocators.select_plans)
        select_plans.click()

