import time
from selenium import webdriver
driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://easycollege.in/dgvcoe/college/stuindex.aspx")
name=driver.find_element("xpath","//input[@type='text']")
name.send_keys("1913101058139")
name=driver.find_element("xpath","//input[@type='password']")
name.send_keys("sat2525")
button=driver.find_element("xpath","//input[@type='submit']")
button.click()
time.sleep(3)
driver.close()