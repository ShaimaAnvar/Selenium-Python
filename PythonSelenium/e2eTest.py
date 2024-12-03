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
driver.get("https://rahulshettyacademy.com/angularpractice/")

               # my code
# driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.find_element(By.XPATH, "(//button[text()='Add '])[1]").click()
# driver.find_element(By.CLASS_NAME, "btn-primary").click()
# driver.find_element(By.CLASS_NAME, "btn-success").click()
# driver.find_element(By.ID, "country").send_keys("India")
# wait=WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India"))).click()
# # driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
# driver.find_element(By.CLASS_NAME, "btn-success").click()
# assert driver.find_element(By.CLASS_NAME, "alert").is_displayed()


              # instructor's solution
# //a[contains(@href,'shop')]    or   a[href*='shop'] -------> regular expression with partial class
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productName=product.find_element(By.XPATH, "div/h4").text
    if productName == 'Blackberry':
        product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class*= 'btn-primary']").click()
driver.find_element(By.CLASS_NAME, "btn-success").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India"))).click()
driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successText= driver.find_element(By.CLASS_NAME, "alert").text
assert 'Thank you'in successText
driver.close()