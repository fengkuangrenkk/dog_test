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
for i in range(1, 20):
    time.sleep(15)
    # 点击全部医生
    driver.find_element(By.XPATH, '//*[@class="data_list"]/div[1]/div[4]//span[text()="挂号"]').click()
    # 输入姓名
    driver.find_element(By.XPATH,
                        '//*[@class="name el-input el-input--suffix"]/input').send_keys('张天下')
    time.sleep(3)
    # 选择输入框人员
    driver.find_element(By.XPATH, '//*[@class="list_item"]').click()
    if 5 < i:
        # 勾选签到
        driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div['
                                      '2]/div[2]/label/span[1]/span').click()
        time.sleep(3)
    # 点击选择时间
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/di'
                                  'v[1]/form/div[2]/div[4]/div/div[1]/div/input').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li/span').click()
    # 完成挂号
    driver.find_element(By.XPATH, '//span[text()="完成挂号"]').click()
# 门诊预约,
for i in range(1, 20):
    time.sleep(5)
    # 点击全部医生
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button').click()
    # 输入姓名
    driver.find_element(By.XPATH,
                        '//*[@class="name el-input el-input--suffix"]/input').send_keys('张天下')
    time.sleep(3)
    # 选择输入框人员
    driver.find_element(By.XPATH, '//*[@class="list_item"]').click()
    time.sleep(3)
    # 点击预约时间
    driver.find_element(By.XPATH, '//*[@class="el-radio__input"]/span').click()
    driver.find_element(By.XPATH, '//input[@placeholder="选择预约时间"]').click()
    local_time = time.localtime(time.time())  # 获取当前时间的时间元组
    week_index = local_time.tm_wday  # 获取时间元组内的tm_wday值
    # 获取当前时间，可配置修改
    week_list = [1, 2, 3, 4, 5, 6, 7]
    if i > 5:
        week_list = [2, 3, 4, 5, 6, 7, 8]
    week_time = week_list[week_index]
    # 判断医生是否可点击-预约号源
    for j in range(1, 9):
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div' + [j].__str__() +
                            '/div' + [week_time + 1].__str__()).click()
        try:
            driver.find_element(By.XPATH, '//li[@class=""]').click()
            break
        except:
            driver.find_element(By.XPATH, '/html/body//span/button[2]//span[text()="取 消"]').click()
    time.sleep(3)
    # # 选定预约时间
    # driver.find_element(By.XPATH, '//li[@class=""]').click()
    # time.sleep(3)
    driver.find_element(By.XPATH, '/html/body//span/button[1]/span[text()="确定"]').click()
    # 完成挂号
    driver.find_element(By.XPATH, '//span[text()="完成挂号"]').click()

time.sleep(5)
# 点击已签列表
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[1]'
                              '/div[1]/div/div[1]/div/div/div/div[2]').click()
# 点击患者
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div'
                              '[4]/div[2]/table/tbody/tr[1]').click()
# 点击作废
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/d'
                              'iv/div[2]/div[2]/div[1]/button').click()
# 确认作废
driver.find_element(By.XPATH, '//*[@aria-label="作废"]/div/div[3]/button/span').click()
# 搜索人员
driver.find_element(By.XPATH, '//*[@placeholder="姓名、手机"]').send_keys('张')
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="app"]//div[2]/div[2]/div[1]/div/input').send_keys(Keys.BACK_SPACE)
# 点击全部-已签-待签-已诊-待诊-已退
for i in range(1, 7):
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@class="table"]/div/div/div/div/div/div/div/div/div' + [i].__str__()).click()
# 待签退号
driver.find_element(By.XPATH, '//*[@class="table"]/div/div/div/div/div/div/div/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3'
                              ']/table/tbody/tr[1]/td[5]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[4'
                              ']/div[1]/div/div[2]/div[2]/div[1]/button').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span').click()
time.sleep(3)
# 点击签到
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]'
                              '/div[3]/table/tbody/tr[1]/td[5]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[2]/div[2]/div[2]/div/div[4]/div['
                              '1]/div/div[2]/div[2]/div[2]/button[1]').click()
time.sleep(3)
# 确定签到
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span').click()
time.sleep(3)

# 点击-明天-后天-更多
driver.find_element(By.ID, 'tab-tomorrow').click()
time.sleep(3)
driver.find_element(By.ID, 'tab-afterTomorrow').click()
time.sleep(3)
driver.find_element(By.ID, 'tab-more').click()

# 测试时间控件,遍历当月时间
current_time = int(time.strftime('%m', time.localtime(time.time())))  # 获取当前天数时间

for i in range(1, current_time):
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]//input[@type="text"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//td' + [i].__str__() + '[@class="available"]/div/span').click()

# 遍历过去月天数
for i in range(1, 3):
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]//input[@type="text"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@class="el-date-picker__header"]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//td' + [i].__str__() + '[@class="available"]/div/span').click()
# 选择年份2021年-月份一月份-天数为1
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]//input[@type="text"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//span[text()="2022 年"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//a[text()="2021"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//a[text()="一月"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//span[text()=1]').click()
# 退出浏览器
driver.quit()
