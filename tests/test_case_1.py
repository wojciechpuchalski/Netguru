import unittest
from page_objects.POM import HomePage, JobOffersPage
from utilities.setup import driver


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = 'https://behance.net'

    def testScript(self):
        driver.get(self.base_url)
        HomePage.go_to_job_offers(self)
        JobOffersPage.search_for_job(self)
        JobOffersPage.verify_returned_offers(self)

    def tearDown(self):
        driver.quit()