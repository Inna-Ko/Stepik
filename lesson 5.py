from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
ICON = driver.find_element(By.CLASS_NAME, "wikipedia-icon")
print("ICON = ", ICON)
INPUT = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
print("INPUT = ", INPUT)
SEARCH = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
print("SEARCH = ", SEARCH)
