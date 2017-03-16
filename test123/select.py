from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("C:\\Users\\pkrustc\\PycharmProjects\\test123\\Select.html")
select = Select(driver.find_element_by_id("select1"))
select.select_by_visible_text("Mariika")

#driver.quit()
