from selenium.webdriver.common.by import By


class CreativeCloudPageLocators(object):
    go_to_polish_version = (By.CSS_SELECTOR, '.locale-modal_button:nth-child(3)')
    select_plans = (By.CLASS_NAME, 'plan_select_apps')
    add_to_cart = (By.CLASS_NAME, 'add_product_text')
    buy_now = (By.CLASS_NAME, 'buy_now')
    payment_page_button = (By.CSS_SELECTOR, "*[data-qe-id='action-button-email']")
    label_payment = (By.CSS_SELECTOR, "*[data-qe-id='step-indicator-label-payment']")