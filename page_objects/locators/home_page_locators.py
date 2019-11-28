from selenium.webdriver.common.by import By


class HomePageLocators(object):
    accept_cookies = (By.ID, '_evidon-accept-button')
    job_offers_link = (By.PARTIAL_LINK_TEXT, 'Oferty pracy')