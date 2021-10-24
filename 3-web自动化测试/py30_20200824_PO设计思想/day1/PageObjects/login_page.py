"""
======================
Author: 柠檬班-小简
Time: 2020/8/24 21:00
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    # 属性 - 元素定位
    username_loc = (By.XPATH, '//input[@name="phone"]')
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    login_button_loc = (By.TAG_NAME, 'button')


    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self,user,passwd):
        self.wait.until(EC.visibility_of_element_located(self.login_button_loc))
        self.driver.find_element(*self.username_loc).send_keys(user)
        self.driver.find_element(*self.passwd_loc).send_keys(passwd)
        self.driver.find_element(*self.login_button_loc).click()
