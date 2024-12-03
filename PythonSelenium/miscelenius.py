
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore_certificate_errors")

# chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
driver.get_screenshot_as_file("screeen.png")