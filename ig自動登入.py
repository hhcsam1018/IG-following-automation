from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'https://www.instagram.com/'  
post_url='https://www.instagram.com/p/CqiHIBoPfLU/comments/'

# ------ 前往該網址 ------
browser.get(url) 

# ------ 填入帳號與密碼 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))

# ------ 網頁元素定位 ------
browser.find_element(By.NAME, 'test.test8596').send_keys("")
browser.find_element(By.NAME, 'sam1996').send_keys("")
browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()

browser.get(post_url)
# ------ 登入 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
'//*[@id="loginForm"]/div/div[3]/button/div')))
# ------ 網頁元素定位 ------
login_click = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
# ------ 點擊登入鍵 -----
login_click.click()

