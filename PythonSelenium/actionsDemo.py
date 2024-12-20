from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
actions=ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.click(driver.find_element(By.LINK_TEXT, "Reload")).perform()