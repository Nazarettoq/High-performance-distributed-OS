import time
from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.google.com');
print('Go to browser!')
time.sleep(10)
driver.quit()