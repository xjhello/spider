from selenium import webdriver

driver_path = r'D:\project\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('hello')