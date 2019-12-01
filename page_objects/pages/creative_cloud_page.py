from utilities.setup import driver
from page_objects.locators.creative_cloud_page_locators import CreativeCloudPageLocators
from selenium.webdriver.common.keys import Keys


class CreativeCloudPage(object):

    def __init__(self):
        self.driver = driver

    def select_plan(self):
        driver.switch_to.window(driver.window_handles[1])
        close = self.driver.find_element(*CreativeCloudPageLocators.go_to_polish_version)
        close.click()
        select_plans = self.driver.find_element(*CreativeCloudPageLocators.select_plans)
        select_plans.click()

    def add_plan_to_cart(self):
        add_to_cart = self.driver.find_element(*CreativeCloudPageLocators.add_to_cart)
        add_to_cart.click()

    def buy_selected_plan(self):
        buy = self.driver.find_element(*CreativeCloudPageLocators.buy_now)
        buy.click()

    def check_page(self):
        page_text = self.driver.find_element(*CreativeCloudPageLocators.payment_page_button).text
        label_payment = self.driver.find_element(*CreativeCloudPageLocators.label_payment).text
        assert ("Przejdź do płatności" in page_text)
        assert ("Płatność" in label_payment)