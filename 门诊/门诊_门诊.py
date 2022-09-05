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

url = 'http://192.168.8.88:8080/login'
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

# 点击门诊
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div[2]/div/ul/li[4]/div/span').click()
time.sleep(5)


class Service:
    # 输入患者信息-填入理疗治疗项目
    def Service_case(self):
        for i in range(1, 6):
            # 点击第一个患者
            driver.find_element(By.XPATH, '//li[@class=""][1]').click()
            # 点击选择医生
            driver.find_element(By.XPATH,
                                '//*[@class="main_content"]/div[1]/div[2]/div[2]//input[@type="text"]').click()
            time.sleep(3)
            driver.find_element(By.XPATH,
                                '/html/body/div/div[1]/div[1]/ul/li[@class="el-select-dropdown__item"]').click()
            if i < 5:
                case = '咳嗽，干咳，咳痰，夜咳，自汗，盗汗，少汗，多汗'
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="chief_complaint_dia"]//span[text()="关闭"]').click()
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[2]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[3]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="past_history_box"]//span[text()="关闭"]').click()
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[4]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="menu"]/div/i').click()
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[5]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="middle_box"]//span[text()="关闭"]').click()
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[6]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="wrap"]//span[text()="关闭"]').click()
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[7]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="wrap"]/div/div[2]/i').click()
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[8]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH, '//*[@class="module_content_wrapper"]/div[9]/div/div/textarea').send_keys(
                    case)
                driver.find_element(By.XPATH,
                                    '//*[@class="module_content_wrapper"]/div[10]/div/div/textarea').send_keys(case)
            else:
                # 调用病例
                driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]').click()

            # 点击治疗项目
            driver.find_element(By.XPATH,
                                '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/div['
                                '2]/div[2]').click()
            # 选择治疗项目
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[3]/div/div['
                                          '1]/div[3]/div[2]/div[1]/label/span[1]/span').click()
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/'
                                          'div[3]/div/div[1]/div[3]/div[2]/div[3]/label/span[1]/span').click()
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/di'
                                          'v[3]/div/div[1]/div[3]/div[2]/div[4]/label/span[1]/span').click()
            # 点击确定
            driver.find_element(By.XPATH, '//span[text()="确定"]').click()
            # 点击理疗项目
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[3]/div/d'
                                          'iv[1]/div[2]/div[3]').click()
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[3]/div/div['
                                          '1]/div[ '
                                          '3]/div[2]/div[1]/label/span[1]/span').click()
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[3]/div/div['
                                          '1]/div '
                                          '[3]/div[3]/button/span').click()  # 点击确定
            # 完成接诊-确定完成接诊
            driver.find_element(By.XPATH, '//span[text()="完成接诊"]').click()
            driver.find_element(By.XPATH, '//*[@aria-label="是否确认完成接诊？"]//button/span').click()
            time.sleep(5)

    # 复制病例
    def Copy_case(name):
        driver.find_element(By.XPATH, '//input[@placeholder="姓名、手机、诊断、编号"]').send_keys(name)
        time.sleep(10)
        # 点击第一个患者
        driver.find_element(By.XPATH, '//li[@class=""][1]').click()
        # 点击选择医生
        driver.find_element(By.XPATH, '//*[@class="main_content"]/div[1]/div[2]/div[2]//input[@type="text"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/ul/li[@class="el-select-dropdown__item"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@class="list_item"]').click()
        time.sleep(7)
        driver.find_element(By.XPATH, '//span[text()="复制全部"]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@aria-label="提示"]/div/div[3]/button[2]/span').click()
        # 完成接诊-确定完成接诊
        driver.find_element(By.XPATH, '//span[text()="完成接诊"]').click()
        driver.find_element(By.XPATH, '//*[@aria-label="是否确认完成接诊？"]//button/span').click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)

    # 开具中药处方
    def Service_Herbal(self):
        # 点击第一个患者
        driver.find_element(By.XPATH, '//li[@class=""][1]').click()
        # 跳转到中药处方
        Materials = driver.find_element(By.XPATH, '//div[text()="中药处方"]')
        driver.execute_script("arguments[0].scrollIntoView();", Materials)
        time.sleep(3)
        # 点击中药处方
        driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div'
                                      '[2]/div[1]').click()
        time.sleep(5)
        # 开具中药-选定中药
        driver.find_element(By.XPATH, '//input[@placeholder="请选择药品"]').send_keys('中药')
        time.sleep(5)

        text = driver.execute_script("return Array.from(document.querySelectorAll('div.menu_item>div:nth-child("
                                     "1)')).find(e => e.innerText.trim() == '中药饮片---草根').click()")
        print(text)

        # xxx = driver.find_element(By.XPATH, '//*[@class="menu_item menu_item7680"]')
        # ActionChains(driver).move_to_element(xxx).perform()
        #
        # ActionChains(driver).click(xxx).perform()
        # xxx = driver.find_element(By.__class__, '//div[text()="中药饮片---草根"]/parent::*')
        # driver.execute_script("arguments[0].click();", xxx)


for i in range(2500):
    if __name__ == '__main__':
        Service.Service_case(self)
        #Service.Copy_case("中药--1 号")


# if __name__ == '__main__':
#     Service.Service_Herbal(self)

'''
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div[1]/d'
                              'iv[2]/div[2]').click()
# 跳转到中药处方
Materials = driver.find_element(By.XPATH, '//div[text()="中药处方"]')
driver.execute_script("arguments[0].scrollIntoView();", Materials)
time.sleep(3)
# 点击中药处方
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div'
                              '[2]/div[1]').click()
time.sleep(5)

# 开具中药-选定中药
driver.find_element(By.XPATH, '//input[@placeholder="请选择药品"]').send_keys('中药')
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]'
                              '/div[4]/div/div[2]/div/div[3]/div/div[2]').click()

time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[2]/di'
                              'v[4]/div/div[2]/div/div[3]/div/div[2]/div[1]').click()
time.sleep(3)
# 数量 煎法
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/d'
                              'iv[4]/div/div[2]/div/ul/li[1]/div[2]/div[1]/div/input').send_keys(10)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/di'
                              'v/ul/li[1]/div[2]/div[2]/div[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/di'
                              'v[2]/div/ul/li[1]/div[2]/div[2]/div[2]/div/div[1]/ul/li[1]').click()
# 输入剂数 选择用法-剂量-频率-服用量
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/'
                              'div[2]/div[1]/div[1]/div/div').send_keys(10)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/d'
                              'iv[2]/div/div[2]/div[1]/div[2]/div/div[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div'
                              '/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/ul/li[1]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]'
                              '/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/'
                              'div[2]/div[1]/div[3]/div/div[2]/div/div[1]/ul/li[1]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div'
                              '[2]/div/div[2]/div[1]/div[4]/div/div[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/div['
                              '2]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/ul/li[1]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/di'
                              'v[4]/div/div[2]/div/div[2]/div[1]/div[5]/div/div[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/div/d'
                              'iv[2]/div/div[2]/div[1]/div[5]/div/div[2]/div/div[1]/ul/li[1]').click()
driver.find_element(By.XPATH, '').click()

# 点击就诊历史
driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div/div/div[1]/p[1]').click()
time.sleep(10)  # 延迟10秒

# 点击复制全部
# driver.find_element(By.XPATH,
#        "/html/body/div[1]/div/section/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[34]/div/div[2]/button[1]/span").click()
# time.sleep(10)  # 延迟10秒
# driver.find_element(By.XPATH,'//*[@id="pane-second"]/div/div/div/div[6]/div/div[2]/button[1]/span').click()
# time.sleep(10)  # 延迟10秒
'''
# 完成接诊
# driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/div[2]/div[1]/div[3]/button[1]').click()
