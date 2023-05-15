from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


ser_obj = Service('C:\browser drivers\chromedriver_win32')
driver = webdriver.Chrome(service = ser_obj)
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
driver.find_element(By.LINK_TEXT, 'Register').click()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Log').click()
driver.find_element(By.ID, 'Email').send_keys('shaikdadapeer362@gmail.com')
driver.find_element(By.NAME, 'Password').send_keys('chinnu7736')
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'forgot-password').click()
time.sleep(3)
links = driver.find_element(By.TAG_NAME, 'a')
print('links', len(links))
