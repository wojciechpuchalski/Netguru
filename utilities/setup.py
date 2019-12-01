from selenium import webdriver

base_url = 'https://behance.net'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=options)