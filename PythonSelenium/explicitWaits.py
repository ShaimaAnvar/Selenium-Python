import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
expectedList= ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList=[]
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results= driver.find_elements(By.XPATH, "//div[@class='products']/div")
count=len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert actualList == expectedList
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
prices= driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
totAmount= int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert sum == totAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)
discAmount= float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert discAmount < totAmount
