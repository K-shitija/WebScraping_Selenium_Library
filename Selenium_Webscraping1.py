# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:22:16 2024

@author: KSHITIJA
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

print("HI")

website= 'https://www.adamchoi.co.uk/overs/detailed'
path ='F:\Python_project_persoanl\Web_Scraping\Webscraping_Selenium\chromedriver_win32'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(website) 

time.sleep(2)
all_matches_button = driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()
time.sleep(5)

print("button clicked")

dropdown= Select(driver.find_element("id",'country'))
dropdown.select_by_visible_text('Spain')
time.sleep(5)


matches = driver.find_elements(By.TAG_NAME,'tr')
date = []
home_team = []
score = []
away_team = []
print("matchesdata")

f=1
for match in matches:
    date.append(match.find_element("xpath",'./td[1]').text)
    home_team.append(match.find_element("xpath",'./td[2]').text)
    score.append(match.find_element("xpath",'./td[3]').text)
    away_team.append(match.find_element("xpath",'./td[4]').text)
    
    print(f,':',match.text)
    f=f+1
    

df = pd.DataFrame({'date':date,'home_team':home_team, 'score':score, 'away_team':away_team})
df.to_excel('Football_data.xlsx',sheet_name='Football_Details',index=False)
driver.quit()
