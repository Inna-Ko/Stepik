import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://hyperskill.org/tracks")

LOGO = driver.find_element(By.XPATH, "(//div/*[contains(@class, 'h-icon')])[1]")
print("LOGO = ", LOGO)

EXPLORE = driver.find_element(By.XPATH, "//a[contains(text(),'Explore')]")
print("EXPLORE = ", EXPLORE)

H1_1 = driver.find_element(By.XPATH, "//h1[contains(text(),'What is your learning goal?')]")
print("H1_1 = ", H1_1)

time.sleep(3)
ALL_TRACKS_TAB = driver.find_element(By.XPATH, "//a[contains(@click-event-context,'all_tracks')]")
print("ALL_TRACKS_TAB = ", ALL_TRACKS_TAB)
