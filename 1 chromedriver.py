# Иницализация в одну строчку, через SeleniumManager

from selenium import webdriver

driver = webdriver.Chrome()


# Инициализация через WebDriverManager
#
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


# Инициализация через WebDriverManager + версия Chrome
#
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
# driver = webdriver.Chrome(service=service)