import unittest
from utilities.setup import driver


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = 'https://beatport.com'

    def testScript(self):
        driver.get(self.base_url)

    def tearDown(self):
        driver.quit()