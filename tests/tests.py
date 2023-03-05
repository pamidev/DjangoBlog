import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='https://pamidev.eu.pythonanywhere.com/admin')


def element_is_clickable():
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("pamidev")
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("pamidev")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="user-tools"]/a[1]').click()
    driver.find_element_by_xpath('/html/body/nav/div/a/span').click()


element_is_clickable()


def respons_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)


respons_check(900, "test900.png")
respons_check(1200, "test1200.png")
respons_check(1800, "test1800.png")
respons_check(600, "test600.png")
