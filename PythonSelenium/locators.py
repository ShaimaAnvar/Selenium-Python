
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,  "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# xpath- //tagname[@attribute='submit']
# css selector- tagname[attribute='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("aaaa")

#select
dropdwn = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdwn.select_by_index(0)
#dropdwn.select_by_value()
dropdwn.select_by_visible_text("Female")


driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME, "alert-success").text

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("bbb")
assert "Success" in message
print(message)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


