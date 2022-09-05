from idlelib import browser
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

# 点击理疗预约
driver.find_element(By.XPATH, '//*[@id="tab-2"]').click()
time.sleep(5)
# 点击全部理疗师
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[3]/div[1]/div[3]/button').click()
# 点击时间进入时间控件
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/'
                              'form/div[2]/div[2]/div/div[1]/input').click()
time.sleep(3)
local_time = time.localtime(time.time())  # 获取当前时间的时间元组
week_index = local_time.tm_wday  # 获取时间元组内的tm_wday值
# 获取当前时间，可配置修改
week_list = [1, 2, 3, 4, 5, 6, 7]
week_time = week_list[week_index]
# 点击预约号源
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div' + [week_time + 1].__str__()).click()
# 选择预约时间
a = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/ul')
b = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/ul')
print(a)

for i in a:
#    print(i.text)
    c = i.text
print(c)
c = list[c]
print(c)




'''
for i in range()
subscribe_therapy = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/ul/li[14]')


# 确认选择时间
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/span/button[1]').click()

time.sleep(3)
# 完成预约
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/'
                              'div[2]/div[2]/div[2]/button[1]').click()

# 理疗预约搜索王半仙
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[1]/div/input').send_keys('王半仙')
time.sleep(5)
xb_subscribe = driver.find_elements(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/di'
                                              'v[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/span')
for i in xb_subscribe:
    if i.text == '王半仙':
        print(i.text, '打印成功')
    else:
        print('叫开发写bug')
        '''
# 获取排班号源
