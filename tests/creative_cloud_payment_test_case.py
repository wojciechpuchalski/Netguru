import unittest
from utilities.setup import base_url
from page_objects.pages import home_page, job_offers_page, adobe_talent_page, creative_cloud_page
from utilities.setup import driver



class SecondTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = base_url

    def testScript(self):
        driver.get(self.base_url)
        home_page.HomePage.accept_cookies(self)
        home_page.HomePage.go_to_job_offers(self)
        job_offers_page.JobOffersPage.go_to_adobe_talent(self)
        adobe_talent_page.JobOffersPage.buy_now(self)
        creative_cloud_page.CreativeCloudPage.polish_version(self)