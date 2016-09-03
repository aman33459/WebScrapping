import webbrowser
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time;
driver = webdriver.Chrome()
driver.get("https://gabrielecirulli.github.io/2048/");
time.sleep(2)
button = driver.find_element_by_tag_name('body')

while True:
	time.sleep(1)
        pp = driver.find_elements_by_tag_name('p')
        for i in pp:
                if(i.text=="Game over!"):
                        time.sleep(5)
                        driver.close()
                        exit()
	button.send_keys(Keys.UP);
	time.sleep(1)
	button.send_keys(Keys.RIGHT);
	time.sleep(1)
	button.send_keys(Keys.UP);
	time.sleep(1)
	button.send_keys(Keys.LEFT);
	time.sleep(1)
	button.send_keys(Keys.DOWN);
	time.sleep(1)
	
'''
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

'''
