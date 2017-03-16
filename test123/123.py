from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://google.bg")

searchbox = driver.find_element_by_id("lst-ib").send_keys("pyhton")
searchbox.submit()
images = driver.find_element_by_class_name("q qs").click()
images = driver.find_element_by_name("vZKJO2_oBP1evM:")

driver.quit()

