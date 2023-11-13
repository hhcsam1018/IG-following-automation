from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException

def auto_follow_comments(username, password, post_url):
    # 设置 WebDriver 驱动程序路径
    driver_path = 'T:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver'  # 替换为你的 WebDriver 驱动程序路径

    # 创建 WebDriver 对象
    driver = webdriver.Chrome()  # 替换为你的 WebDriver 驱动程序

    # 打开 Instagram 登录页面
    driver.get('https://www.instagram.com/accounts/login/')
    
    # 等待登录页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    
    # 输入用户名和密码并登录
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    
    # 等待登录完成并跳转到帖子页面
    time.sleep(5)
    # WebDriverWait(driver, 10).until(EC.url_contains('https://www.instagram.com/'))
    
    # 打开指定的帖子页面
    driver.get(post_url)
    time.sleep(5)
    # WebDriverWait(driver, 10,5)
    
    # 获取帖子的所有留言帐号
    comments = driver.find_elements(By.XPATH, '//span[contains(@class, "_ap3a") and contains(@class, "_aaco") and contains(@class, "_aacw") and contains(@class, "_aacx") and contains(@class, "_aad7") and contains(@class, "_aade")]')
    print('comments : ',comments)
    
    # 追踪留言帐号
    for comment in comments:
        try:
            profile_username = comment.text
            print('profile_username : ',profile_username)
            # 判断是否已经追踪过该帐号
            # if not is_following(driver, profile_username):
            # #     # 追踪帐号
            follow_user(driver, profile_username)
            print(f'已追踪帐号：{profile_username}')
        except StaleElementReferenceException:
            print("StaleElementReferenceException. Retrying...")
    # 关闭浏览器
    driver.quit()

# # 判断是否已经追踪该帐号
# def is_following(driver, username):
#     driver.get(f'https://www.instagram.com/{username}/')
#     time.sleep(5)
#     follow_button = driver.find_element(By.XPATH, "//*[@id="mount_0_0_y8"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button/div")
    
#     return follow_button.is_displayed()

# 追踪帐号
def follow_user(driver, username):
    driver.get(f'https://www.instagram.com/{username}/')
    time.sleep(5)
    follow_button = driver.find_element(By.XPATH, "//div[@class='_ap3a _aaco _aacw _aad6 _aade']")
    follow_button.click()
    

# 调用函数，传入你的 Instagram 用户名、密码和帖子的 URL
auto_follow_comments("帳號", "密碼", 'https://www.instagram.com/p/CqiHIBoPfLU/comments/')
