import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get('https://trendoceans.com')
print('Title: %s' % driver.title)
time.sleep(10)
driver.quit()
