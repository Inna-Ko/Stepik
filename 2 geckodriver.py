# Иницализация в одну строчку, через SeleniumManager

from selenium import webdriver

driver = webdriver.Firefox()


# Инициализация через WebDriverManager
#
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
#
# service = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service)

