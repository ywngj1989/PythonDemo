from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# url
URL = 'http://test.app.operate.webus.vip:12321/index/login/index.html'
# 登录时的手机号
PHONE = '18358103147'
# 登录时的密码
PASSWORD = '123456'
web = webdriver.Chrome()


def login():
    web.get(URL)
    web.maximize_window()
    web.find_element_by_name("phone").send_keys(PHONE)
    # sleep(30)
    web.find_element_by_name("password").send_keys(PASSWORD)
    # sleep(30)
    web.find_element_by_link_text("登录").click()
    # sleep(30)


def addMoney():
    login()
    web.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[3]/td[5]/p/a[2]").click()
    web.find_element_by_name("amount").send_keys(100)
    web.find_element_by_name("description").send_keys("通过余额调整充值")
    web.find_element_by_class_name("submit_l submit_amount").click()
