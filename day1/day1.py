from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj = Service('C:\browser drivers\chromedriver_win32')
driver = webdriver.Chrome(service=ser_obj)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(5)
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
act_title = driver.title
print("title", act_title)
driver.close()