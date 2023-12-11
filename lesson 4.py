from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://translate.google.ru/')
PAGE_TITLE1 = driver.title
print(PAGE_TITLE1)
driver.get('https://ya.ru/')
PAGE_TITLE2 = driver.title
print(PAGE_TITLE2)
driver.back()
assert PAGE_TITLE1 == driver.title, "Неверный заголовок страницы"
driver.refresh()
PAGE_URL1 = driver.current_url
driver.forward()
assert PAGE_URL1 != driver.current_url, "Адрес не изменился"

