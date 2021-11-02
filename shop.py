import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("mipi@mailinator.com")
time.sleep(1)
driver.find_element_by_id("password").send_keys("4C7G2jvagQRBHdB")
time.sleep(1)
driver.find_element_by_xpath("//input[@name='login']").click()
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 200);")
driver.find_element_by_xpath("//div[@id='content']/ul/li[3]/a").click()
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.XPATH, "//h1[@class='product_title entry-title']"), "HTML5 Forms"))
time.sleep(1)
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 200);")
driver.find_element_by_link_text("HTML").click()
items_count = driver.find_elements_by_css_selector(".products.masonry-done li")
print(len(items_count))
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 200);")
scheduled = driver.find_element_by_css_selector(".orderby")
scheduled_checked = scheduled.get_attribute("value")
if scheduled_checked == "menu_order":
    print("выбран: Default sorting")
else:
    print("что то не так")
element = driver.find_element_by_css_selector(".orderby")
select = Select(element)
select.select_by_value("price-desc")
scheduled = driver.find_element_by_css_selector(".orderby")
scheduled_checked = scheduled.get_attribute("value")
if scheduled_checked == "price-desc":
    print("выбран: от большего к меньшему")
else:
    print("что то не так")
time.sleep(2)
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 200);")
driver.find_element_by_xpath("//div[@id='content']/ul/li[1]/a").click()
element = driver.find_element_by_css_selector(".price >del").text
assert "₹600.00" in element
element = driver.find_element_by_css_selector(".price >ins").text
assert "₹450.00" in element
time.sleep(1)
driver.find_element_by_css_selector(".images >a").click()
WebDriverWait(driver, 20).until(
   EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
driver.find_element_by_css_selector(".pp_close").click()
time.sleep(2)
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_link_text("Sign out").click()
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_xpath("//a[@data-product_id='181']").click()
time.sleep(3)
elent = driver.find_element_by_xpath("//span[@class='amount']").text
assert "280.00" in elent
elem = driver.find_element_by_xpath("//span[@class='cartcontents']").text
assert "1 Item" in elem
driver.find_element_by_xpath("//ul[@id='main-nav']/li[6]/a").click()
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.XPATH, "//tr[@class='cart-subtotal']/td/span"), "280.00"))
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.XPATH, "//tr[@class='order-total']/td/strong/span"), "294.00"))
driver.find_element_by_xpath("//tbody/tr[1]/td[1]/a").click()
time.sleep(2)
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element_by_xpath("//a[@data-product_id='182']").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_xpath("//a[@data-product_id='180']").click()
time.sleep(2)
driver.find_element_by_xpath("//ul[@id='main-nav']/li[6]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//tbody/tr[1]/td[1]/a").click()
driver.find_element_by_link_text("Undo?").click()
count = driver.find_element_by_xpath("//tbody/tr[1]/td[5]/div/input")
count.clear()
count.send_keys("3")
time.sleep(2)
driver.find_element_by_xpath("//tbody/tr[3]/td[1]/input[@class='button']").click()
element = driver.find_element_by_xpath("//tbody/tr[1]/td[5]/div/input").get_attribute("value")
assert element == "3"
time.sleep(3)
driver.find_element_by_xpath("//tbody/tr[3]/td[1]/div/input[@class='button']").click()
time.sleep(2)
element = driver.find_element_by_css_selector(".woocommerce-error >li").text
assert "Please enter a coupon code" in element
time.sleep(2)
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_xpath("//a[@data-product_id='182']").click()
time.sleep(2)
driver.find_element_by_xpath("//ul[@id='main-nav']/li[6]/a").click()
WebDriverWait(driver, 20).until(
   EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a")))
driver.find_element_by_css_selector(".wc-proceed-to-checkout > a").click()
WebDriverWait(driver, 30).until(
   EC.text_to_be_present_in_element((By.XPATH, "//div[@class='woocommerce-billing-fields']/h3"), "Billing Details"))
driver.find_element_by_id("billing_first_name").send_keys("Dahlia")
driver.find_element_by_id("billing_last_name").send_keys("Foley")
driver.find_element_by_id("billing_email").send_keys("diqehovyja@mailinator.com")
driver.find_element_by_id("billing_phone").send_keys("+1 (481) 226-7057")
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_xpath("//div/a/span/b").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("united ki")
driver.find_element_by_css_selector(".select2-result-label").click()
driver.find_element_by_id("billing_address_1").send_keys("22 Second Parkway")
driver.find_element_by_id("billing_address_2").send_keys("Dolore dolore volupt")
driver.find_element_by_id("billing_city").send_keys("delectus")
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_id("billing_state").send_keys("Temporibus")
driver.find_element_by_id("billing_postcode").send_keys("GU16 7HF")
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
WebDriverWait(driver, 20).until(
   EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
WebDriverWait(driver, 20).until(
   EC.text_to_be_present_in_element((By.XPATH, "//table/tfoot/tr[3]/td"), "Check Payments"))
driver.quit()