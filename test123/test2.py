from selenium import webdriver

driver = webdriver.Chrome()
driver.get("C:\\Users\\pkrustc\\PycharmProjects\\test123\\radiobuttons.html")

#radioButton = driver.find_element_by_css_selector("input:nth-of-type(2)")
#radioButton.click()

radioButtons = driver.find_elements_by_css_selector("input")
for B in radioButtons:
    if B.is_selected():
        print(i.get_attribute("value"))

driver.quit()