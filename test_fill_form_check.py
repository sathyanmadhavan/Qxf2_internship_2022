"""
This Script is used to test if the values entering properly
"""
#Importing time module
import time
#Importing webdriver from selenium
from selenium import webdriver
#Initilaze driver instance
driver=webdriver.Chrome()
#.get method helps you to redirecrt to the URL
driver.get("https://edumarshal.com/")
#find_element method searches and locate the web element
name=driver.find_element("xpath","//input[@name='input_1.3']").send_keys("Sathyan")
name=driver.find_element("xpath","//input[@name='input_1.6']").send_keys("Madhavan")
message=driver.find_element("xpath","//input[@type='email']").send_keys("xxx@gmail.com")
#send_keys will send the value
phone=driver.find_element("xpath","//input[@type='tel']").send_keys("1234567890")
name=driver.find_element("xpath","//input[@name='input_5']").send_keys("Asan institute")
city=driver.find_element("xpath","//input[@name='input_8']").send_keys("chennai")
number=driver.find_element("xpath","//input[@name='input_7']").send_keys("10")
#.click method will emulates a mouse click option
check=driver.find_element("xpath","//label[@for='choice_1_6_1']").click()
submit=driver.find_element("xpath","//input[@type='submit']").click()
#Sleep method will wait for the page to load
time.sleep(3)
driver.close()
