import webbrowser
import requests
import bs4
from selenium import webdriver
import time;
driver = webdriver.Chrome()
driver.get("http://www.codeforces.com");
time.sleep(2)
button = driver.find_element_by_link_text("Enter");
button.click();
handles=driver.window_handles
#print handles
for i in handles:
	driver.switch_to.window(i)
#driver.switch_to.window(driver.current_url)
form=driver.find_element_by_id("handle");
form.send_keys("*****");#change accordingly
time.sleep(5)
ff=driver.find_element_by_id("password");
ff.send_keys("*****");#change accordingly
time.sleep(5)
ff.submit();
time.sleep(5)
driver.close()

