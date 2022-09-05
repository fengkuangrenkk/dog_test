from idlelib import browser
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from xml import etree
# 显示等待
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

driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div[2]/div/ul/li[3]/div/span').click()  # 点击挂号预约

# 门诊挂号
for i in range(1, 9999):
    time.sleep(10)
    # 点击全部医生
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button').click()
    # 输入姓名
    driver.find_element(By.XPATH,
                        '//*[@class="name el-input el-input--suffix"]/input').send_keys('中药--1 号')
    time.sleep(13)
    # 选择输入框人员
    driver.find_element(By.XPATH, '//*[@class="list_item"]').click()
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[2]/div['
                        '2]/label/span[1]/span').click()
    time.sleep(13)
    # 点击选择时间
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/di'
                                  'v[1]/form/div[2]/div[4]/div/div[1]/div/input').click()
    time.sleep(15)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li/span').click()
    time.sleep(15)
    # 完成挂号
    driver.find_element(By.XPATH, '//span[text()="完成挂号"]').click()


