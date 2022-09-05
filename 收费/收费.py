import random
from idlelib import browser
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from xml import etree
# 显示等待
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
# 键盘事件
from selenium.webdriver.common.keys import Keys
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
import self

url = 'http://192.168.8.50:31833/login'
# 将路径实例化为一个Service对象
s = Service(r"F:\Chrome驱动\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=s)
# 最大化窗口
driver.maximize_window()
driver.get(url)
# 设置隐式等待为 10s
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/input').send_keys(
    15118120531)  # 登录
paasword = 'yxd123456'
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/input').send_keys(paasword)

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/button/span').click()  # 点击登录

# 点击收费
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div[2]/div/ul/li[5]').click()


# a = random.randint(1, 7)


def x():
    time.sleep(10)
    # 点击第一个患者
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div[1]/div[1]/div[2]/div[2]/div[1]/'
                                  'div/div[1]/span').click()
    time.sleep(10)
    # 点击收费（微信收钱）
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/div[1]/div[1]/div[2]/button[1]').click()
    time.sleep(10)
    a = random.randint(1, 7)
    print(a, 'a')
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/ul/li' + [a].__str__() + '/div/div').click()
    time.sleep(10)
    # 勾选同时发药
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div/div[1]/div/label/span[1]/span').click()
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div/div[2]/button[1]/span').click()


for i in range(1, 1000):
    if __name__ == '__main__':
        x()
    if i % 5 == 0:
        driver.refresh()
        print(i)
