page_num = 4 # 你需要评价的同学的页数
stu_id = "302xxxxxxx" # 输入你的学号，后续不需要输验证码

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
print("imported normally")

driver = webdriver.Chrome()
# driver = webdriver.ChromiumEdge()

# 如果网址有变, 请自行修改
driver.get("http://172.31.126.2/login?redirect=/user/profile")
driver.maximize_window()

username=driver.find_element(by="xpath",value="/html/body/div/div/form/div[1]/div/div/input")
password = driver.find_element(by="xpath",value="/html/body/div/div/form/div[2]/div/div[1]/input")
driver.implicitly_wait(2)

username.clear()
password.clear()
username.send_keys(stu_id)
password.send_keys(stu_id)

login_button = driver.find_element(by=By.CLASS_NAME, value="el-button--large")
login_button.click()
cross_vali_button = driver.find_elements(by=By.CLASS_NAME, value="submenu-title-noDropdown")[1]
cross_vali_button.click()

# 打分列表, 依次为德智体美劳
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
        for count, blank in enumerate(blanks[:5]):
            blank.clear()
            blank.send_keys(grades[count])
        button = driver.find_element(by=By.CLASS_NAME, value="el-button--primary")

        button.click()
        driver.back()

for pn in range(1, page_num+1):
    fill_in_one_page(pn)

print("finish")
