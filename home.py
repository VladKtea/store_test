import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_xpath("//div[@class='woocommerce']/ul/li[1]/a").click()
driver.execute_script("window.scrollBy(0, 400);")
driver.find_element_by_xpath("//div[@class='woocommerce-tabs wc-tabs-wrapper']/ul/li[2]/a").click()
driver.find_element_by_css_selector(".star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Iona Durham")
driver.find_element_by_id("email").send_keys("barymasemu@mailinator.com")
driver.find_element_by_id("submit").click()
time.sleep(2)
driver.quit()