import time

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("http://google.bg")

assert "Google" in driver.title
#left expected result , right actual result

searchbox = driver.find_element_by_id("lst-ib")
searchbox.send_keys("pyhton")
searchbox.send_keys(Keys.ENTER)

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".qs")))

images = driver.find_element_by_css_selector(".qs").click()
image = driver.find_element_by_css_selector("#isr_mc img:first-child")
v = image.get_attribute("class")
#pravim atribut za da go dokajem s assert
assert "rg_ic rg_i" in image.get_attribute("class")

#assert pravi proverka na na6iq image dali e tam

#    driver.quit()

