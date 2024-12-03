from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME, "blinkingText").click()
windowsOpened=driver.window_handles
driver.switch_to.window(windowsOpened[1])
paraContent = driver.find_element(By.XPATH, "//p[2]").text
# print(paraContent)
email=paraContent[18:47]
# print(email)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1234")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

wait = WebDriverWait(driver, 10)
message = driver.find_element(By.XPATH, "//form/div[1]")
wait.until(expected_conditions.visibility_of(message))

print(message.text)


