from selenium.webdriver.common.by import By


class JobOffersLocators(object):
    search_input = (By.CLASS_NAME, 'Search-userInput-3YZ')
    offer_description = (By.CLASS_NAME, 'JobCard-description-396')
    publish_job_offers = (By.CLASS_NAME, 'CrossSellCard-button-1u4')