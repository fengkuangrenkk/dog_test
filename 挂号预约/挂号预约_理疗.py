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
import random

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
name = ['张', '李', '王', '赵', '天', '肖', '张', '李', '王', '赵', '天', '肖'] * 100
number = random.randint(1, 200)

# 预约10个患者,10个明天患者
for i in range(1, 20):
    time.sleep(3)

    # 点击全部理疗师
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[3]/div[1]/div[3]/button').click()
    # 输入患者姓名
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div['
                                  '1]/form/div[1]/div[1]/div/div[1]/input').send_keys(name[number].__str__())
    time.sleep(3)
    # 选定患者
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div['
                                  '1]/form/div[1]/div[1]/div/div[2]/div/div[2]').click()
    # 大于6时勾选同时完成签到,大于15时取消签到
    if 6 < i < 15:
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@aria-label="新增预约"]/div[2]/div[2]/div[2]/label/span[1]/span').click()
    # 点击时间进入时间控件
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/'
                                  'form/div[2]/div[2]/div/div[1]/input').click()
    time.sleep(3)
    local_time = time.localtime(time.time())  # 获取当前时间的时间元组
    week_index = local_time.tm_wday  # 获取时间元组内的tm_wday值
    # 获取当前时间，可配置修改
    week_list = [1, 2, 3, 4, 5, 6, 7]
    # 大于10时预约明天时间
    if i > 10:
        week_list = [2, 3, 4, 5, 6, 7, 8]
    week_time = week_list[week_index]
    # 判断理疗师是否可点击-预约号源
    for j in range(1, 30):
        spa = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div' + [j].__str__() +
                                  '/div' + [week_time + 1].__str__())
        if spa.is_enabled():
            spa.click()
            break
    time.sleep(3)
    # 判断时间是否可点击 选择预约时间
    for c in range(1, 10):
        driver.find_element(By.XPATH, '//li[@class=""]' + [c].__str__()).click()
        try:
            driver.find_element(By.XPATH, '//li[@class=""]').click()
            break
        except:
            driver.find_element(By.XPATH, '/html/body//span/button[2]//span[text()="取 消"]').click()
    time.sleep(3)
    # 确认选择时间
    driver.find_element(By.XPATH, '/html/body//span/button[1]/span[text()="确定"]').click()
    time.sleep(3)
    # 完成预约
    driver.find_element(By.XPATH, '//span[text()="完成预约"]').click()

# 理疗预约随机搜索姓-搜索后清空搜索姓名
driver.find_element(By.XPATH, '//input[@placeholder="姓名、手机"]').send_keys(name[number].__str__())
time.sleep(5)
driver.find_element(By.XPATH, '//input[@placeholder="姓名、手机"]').send_keys(Keys.BACK_SPACE)
time.sleep(3)
# 点击全部
for i in range(1, 5):
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div['
                                  '1]/div/div/div[1]/div' + [i].__str__()).click()
    # 签到作废
    if i == 2:
        driver.find_element(By.XPATH, '//span[text()="已签"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@aria-label="新增预约"]//span[text()="作废"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@aria-label="作废"]/div/div[3]/button[2]/span').click()
    # 待签退号-待签签到
    elif i == 3:
        driver.find_element(By.XPATH, '//*[@class="table_body"][2]/div/div[3]/table/tbody/tr[1]/td[1]').click()
        time.sleep(3)
        # 退号
        # driver.find_element(By.XPATH, '//span[text()="退号"]').click()
        # driver.find_element(By.XPATH, '//*[@aria-label="退号"]/div/div[3]/button[2]/span').click()
        driver.find_element(By.XPATH, '//*[@aria-label="新增预约"]//span[text()="签到"]').click()
        driver.find_element(By.XPATH, '//*[@aria-label="签到"]/div/div[3]/button[2]/span').click()       
# 点击-明天-后天-更多
driver.find_element(By.ID, 'tab-tomorrow').click()
time.sleep(3)
driver.find_element(By.ID, 'tab-afterTomorrow').click()
time.sleep(3)
driver.find_element(By.ID, 'tab-more').click()

# 测试时间控件,遍历当月时间
current_time = int(time.strftime('%m', time.localtime(time.time())))    # 获取当前天数时间

for i in range(1, current_time):
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]//input[@type="text"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//td'+[i].__str__()+'[@class="available"]/div/span').click()

# 遍历过去月天数
for i in range(1, 3):
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]//input[@type="text"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@class="el-date-picker__header"]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//td'+[i].__str__()+'[@class="available"]/div/span').click()
# 选择年份2021年-月份一月份-天数为1
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]//input[@type="text"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//span[text()="2022 年"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//a[text()="2021"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//a[text()="一月"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//tr[@class="el-date-table__row"]/td/div//span[text()=1]').click()
# 退出浏览器
driver.quit()
