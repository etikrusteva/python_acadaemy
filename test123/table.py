from selenium import webdriver

driver = webdriver.Chrome()
driver.get("C:\\Users\\pkrustcPycharmProjects\\test123\\table.html")
outertable = driver.find_element_by_tag_name("table")
innertable = outertable.find_element_by_tag_name("table")
row = innertable.find_element_by_tag_name("td")[1]
#print(row.text)
