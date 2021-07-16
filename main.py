import os
from selenium import webdriver
from time import sleep

assert os.environ.get('USER_LOGIN') != None, "USER_LOGIN must be set"
assert os.environ.get('USER_PASSWORD') != None, "USER_PASSWORD must be set"

chromedriver = os.environ["webdriver_path"]
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://esia.gosuslugi.ru/profile/user/personal")
sleep(3)

username = os.environ['USER_LOGIN']
driver.find_element_by_id("login").send_keys(username)

password = os.environ['USER_PASSWORD']
driver.find_element_by_id("password").send_keys(password)

driver.find_element_by_id("loginByPwdButton").click()
sleep(3)

passport_data = driver.find_element_by_xpath("//*[contains(text(), 'Паспорт гражданина РФ')]")
res_file = open("result.txt", "w+")
res_file.write(passport_data.text.strip())
res_file.close()
print("Succsess")
