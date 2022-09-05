import time

import heartrate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 显示等待
# 键盘事件
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = 'http://192.168.8.50:31833/login'
# 将路径实例化为一个Service对象
s = Service(r"F:\Chrome驱动\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=s)
# 最大化窗口
driver.maximize_window()
driver.get(url)
# 设置隐式等待为 10s
driver.implicitly_wait(10)
# 打印代码响应时间
# heartrate.trace(browser=True)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/input').send_keys(
    15118120531)  # 登录
paasword = 'yxd123456'
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/input').send_keys(paasword)

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/button/span').click()  # 点击登录
time.sleep(3)

# 清空排班
# driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[1]/button[2]/span').click()
# driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/span/button[1]/span').click()
# time.sleep(3)
local_time = time.localtime(time.time())  # 获取当前时间的时间元组
week_index = local_time.tm_wday  # 获取时间元组内的tm_wday值
# 获取当前时间，可配置修改
week_list = [2, 3, 4, 5, 6, 7, 8]
# 预约明天号源
# week_list = [3, 4, 5, 6, 7, 8, 9]
week_time = week_list[week_index]

# 跳转到医生排班指定元素
Scheduling = driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div[1]/div' + [week_time].__str__())
driver.execute_script("arguments[0].scrollIntoView();", Scheduling)

for i in range(1, 11):
    time.sleep(3)
    # 鼠标悬停到指定排班人员
    staff = driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                                '/div' + [week_time].__str__())
    if i == 10:
        staff_axd = driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i + 3].__str__() +
                                        '/div' + [week_time].__str__())
        ActionChains(driver).move_to_element(staff_axd).perform()
        time.sleep(3)
    ActionChains(driver).move_to_element(staff).perform()
    # 点击排班
    driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div/div/button[1]/span').click()
    time.sleep(3)
    # 勾选排班
    driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7'
                                                         ']/td[1]/div/label/span[1]/span').click()
    time.sleep(3)
    # 输入号源量
    driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/td[3]/div'
                                                         '/div/input').send_keys(100)
    time.sleep(3)
    # 选择诊室-确定选选择
    driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [
                            week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/td[4]/div/div/div/input').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/td[4]'
                                                         '/div/div/div[2]/div[1]/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div[2]/div[2]/button[1]').click()
    # 设置医生排班人员休息-删除
    if i == 9:
        ActionChains(driver).move_to_element(staff).perform()
        driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() +
                            '/div' + [week_time].__str__() + '/div[2]/div/button[3]/span').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@aria-label="休息"]//span[text()="确 定"]').click()
        time.sleep(3)
    elif i == 10:
        ActionChains(driver).move_to_element(staff).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="pane-first"]/div/div[2]/div[2]/div' + [i].__str__() + '/div' + [
            week_time].__str__() +
                            '/div[2]/div/button[2]/span').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@aria-label="删除排班"]//span[text()="确 定"]').click()
        time.sleep(3)

# 选择理疗预约
classes = driver.find_element(By.XPATH, '//*[@id="tab-second"]')
driver.execute_script("arguments[0].scrollIntoView();", classes)
driver.find_element(By.XPATH, '//*[@id="tab-second"]').click()
time.sleep(3)
# 跳转定位到第一个人员元素
classes_a = driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div[1]/div' + [week_time].__str__())
driver.execute_script("arguments[0].scrollIntoView();", classes_a)

# 清空本周排班
# driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[1]/button[2]/span').click()
# time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/span/button[1]').click()
# time.sleep(3)

for i in range(1, 11):
    time.sleep(3)
    # 鼠标悬停到指定排班人员
    staff_call = driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() +
                                     '/div' + [week_time].__str__())
    if i == 10:
        staff_calla = driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i + 3].__str__() +
                                          '/div' + [week_time].__str__())
        ActionChains(driver).move_to_element(staff_calla).perform()
        time.sleep(3)
    ActionChains(driver).move_to_element(staff_call).perform()
    # 点击排班
    driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div/div/button[1]/span').click()
    time.sleep(3)
    # 勾选排班
    driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() + '/div' +
                        [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/td[1]/div/lab'
                                                'el/span[1]/span').click()
    time.sleep(3)
    # 输入班次时长
    driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() + '/div'
                        + [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/td[3]/d'
                                                  'iv/div[1]/input').send_keys(30)
    time.sleep(3)
    # 可同时预约人数
    driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/'
                                                         'td[3]/div/div[2]/div/input').click()
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[4]//span[text()="4人"]/parent::*').click()
        print('预约人数失败', i)
    except:
        driver.find_element(By.XPATH, '//*[@x-placement="bottom-start"]//span[text()="4人"]/parent::*').click()
        print('预约人数成功', i)
    time.sleep(3)
    # 选择诊室-确定选选择
    driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() +
                        '/div' + [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/td['
                                                         '4]/div/div/div/input').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() + '/div' +
                        [week_time].__str__() + '/div[2]/div[1]/div[3]/table/tbody/tr[7]/td[4]/div/div'
                                                '/div[2]/div[1]/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() + '/div' +
                        [week_time].__str__() + '/div[2]/div[2]/button[1]/span').click()
    # 设置理疗排班人员休息-删除
    if i == 9:
        ActionChains(driver).move_to_element(staff_call).perform()
        driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() +
                            '/div' + [week_time].__str__() + '/div[2]/div/button[3]/span').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@aria-label="休息"]//span[text()="确 定"]').click()
    elif i == 10:
        ActionChains(driver).move_to_element(staff_call).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div[2]/div[2]/div' + [i].__str__() + '/div' +
                            [week_time].__str__() + '/div[2]/div/button[2]/span').click()
        # time.sleep(3)
        # a = driver.find_element(By.XPATH, '//*[@aria-label="删除排班"]//span[text()="确 定"]')
        # ActionChains(driver).click(a).perform()
