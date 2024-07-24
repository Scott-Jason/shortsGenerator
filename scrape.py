
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chromedriver_path = "/Users/jscott/repos/chromedriver"
service = Service(chromedriver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.reddit.com/r/AmItheAsshole/")


print(driver.title)
#keep it open for 5 sec
time.sleep(5)

