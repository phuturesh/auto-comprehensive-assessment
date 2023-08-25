page_num = 4 # 你需要评价的同学的页数

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
print("imported normally")

driver = webdriver.Chrome()
# 如果网址有变, 请自行修改
driver.get("http://172.31.126.2/prod-api/casLogin?source=1")

username = driver.find_element(by=By.ID, value="un")
password = driver.find_element(by=By.ID, value="pd")

username.clear()
password.clear()
# 下面两行引号内输入你的用户名 (username) 和密码 (password)
username.send_keys("")
password.send_keys("")
# 你有20秒完成: 输入验证码, 登录, 点击左侧"班级互评"按钮, 如果不够, 请修改sleep后面的数字(秒)
print("waiting for logging in")
time.sleep(20)
driver.implicitly_wait(2)

grades = ["20", "45", "10", "10", "10"]

# 一轮只能处理一个页面的同学
def fill_in_one_page(page):
    for i in range(0, 10):
        nextpage_button = driver.find_element(by=By.CLASS_NAME, value="btn-next")
        for p in range(1, page):
            nextpage_button.click()

        time.sleep(1)
        print(f"dealing with the {i}th student")
        links = driver.find_elements(by=By.CLASS_NAME, value="action")
        links[i].click()
        
        blanks = driver.find_elements(by=By.CLASS_NAME, value="el-input__inner")
        count = 0
        for blank in blanks:
            if count < 5:
                blank.clear()
                blank.send_keys(grades[count])
                count += 1
            else:
                break
        button = driver.find_element(by=By.CLASS_NAME, value="el-button--primary")

        button.click()
        driver.back()

for pn in range(1, page_num+1):
    fill_in_one_page(pn)

print("finish")
