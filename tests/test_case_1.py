import unittest
from page_objects.pages import home_page, job_offers_page
from utilities.setup import driver


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = 'https://behance.net'

    def testScript(self):
        driver.get(self.base_url)
        home_page.HomePage.go_to_job_offers(self)
        job_offers_page.JobOffersPage.search_for_job(self)
        job_offers_page.JobOffersPage.verify_returned_offers(self)

    def tearDown(self):
        driver.quit()