import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("reg_email").send_keys("mipi@mailinator.com")
time.sleep(1)
driver.find_element_by_id("reg_password").send_keys("4C7G2jvagQRBHdB")
time.sleep(2)
driver.find_element_by_xpath("//input[@name='register']").click()
time.sleep(1)
driver.find_element_by_id("username").send_keys("mipi@mailinator.com")
time.sleep(1)
driver.find_element_by_id("password").send_keys("4C7G2jvagQRBHdB")
time.sleep(1)
driver.find_element_by_xpath("//input[@name='login']").click()
some_element= WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-content > p > a"), "Sign out"))
time.sleep(2)
driver.quit()