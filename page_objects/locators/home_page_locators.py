from selenium.webdriver.common.by import By


class HomePageLocators(object):
    job_offers_link = (By.PARTIAL_LINK_TEXT, 'Oferty pracy')