from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
browserSortedVeggies=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#put the browser sorted veggie list in an array (browser will sort the veggies while cliking the header)
browserSortedWebelements=driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in browserSortedWebelements:
    browserSortedVeggies.append(ele.text)
print(browserSortedVeggies)
originalBrowserSortedVeggies=browserSortedVeggies.copy()

#manually sort the array
browserSortedVeggies.sort()
#check if manualy sorted array and browser sorted array are equal
assert originalBrowserSortedVeggies ==browserSortedVeggies