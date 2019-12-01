from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CreativeCloudPageLocators(object):
    go_to_polish_version = (By.CSS_SELECTOR, '.locale-modal_button:nth-child(3)')
    select_plans = (By.CLASS_NAME, 'plan_select_apps')