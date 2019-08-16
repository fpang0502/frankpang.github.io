import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import csv
from os import listdir
from os.path import isfile, join
from selenium.webdriver.support.ui import Select

loginPage = 'https://www.midwestpublishing.com/login.asp'
url2 = 'https://www.midwestpublishing.com/product222/Directoryload.asp?UserName=W8565%20ANDREW%20SANTALUCIA'

driver = webdriver.Chrome(executable_path=r"/Users/fpang/Desktop/code/oceanit-2019/chromedriver")
driver.get(loginPage)

username = driver.find_element_by_id("UserName")
username.clear()
username.send_keys("W8565 ANDREW SANTALUCIA")

password = driver.find_element_by_name("Password")
password.clear()
password.send_keys("DragX2019")

driver.find_element_by_tag_name('button').click()

# wait to make sure there are two windows open
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)

# switch windows
driver.switch_to.window(driver.window_handles[1])

# print(driver.window_handles)

iFrames = driver.find_elements_by_tag_name("frame")
driver.switch_to.frame(iFrames[0])

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"gb")))

startIndustrySearchHere = driver.find_elements_by_xpath("//*[contains(text(), 'Start Industry Search Here')]")

startIndustrySearchHere[0].click()

pipeline = driver.find_elements_by_xpath("//*[contains(text(), 'Pipeline')]")

driver.execute_script("arguments[0].click();", pipeline[0])

pipelineOwners = driver.find_elements_by_xpath("//*[contains(text(), 'Pipeline Owners & Operators')]")

driver.execute_script("arguments[0].click();", pipelineOwners[0])


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"PLOpersSearchBox")))

pipelineBox = driver.find_element_by_id("PLOpersSearchBox")
listing = driver.find_element_by_xpath("//form[@id='PLOpersSearchBox']/div[1]/div[2]/div[6]/div[15]/input[1]")
# print(listing.get_attribute("outerHTML"))
driver.execute_script("arguments[0].click();", listing)

# ----------------
select = Select(driver.find_element_by_id('gotopage1'))
select.select_by_index(264)
# ----------------
# header = ['Location', 'Company_Name', 'Phone_Number', 'Website', 'Email']
# with open('midwestPublishing.csv', 'w') as csvFile:
	# writer = csv.writer(csvFile)
	# writer.writerow(header)
for i in range(1):

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"results")))

	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']")))

	resultsBox = driver.find_element_by_id("results")

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME,"hr")))

	pluses = driver.find_elements_by_css_selector("[style^=color]")

	for i, p in enumerate(pluses):
		company_sign_id = p.get_attribute("id");
		if "Company_sign" in company_sign_id:
			# company_information = []
			# location = "None"
			# company_name = "None"
			# phone_number = "None"
			# website = "None"
			# email = "None"
			driver.execute_script("arguments[0].click();", p)
			id_num = company_sign_id.replace("Company_sign", "")
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"Company_List"+id_num)))
			company_name_element = driver.find_element_by_xpath("//div[@id='DetailAll"+id_num+"']/div[1]")
			company_name = company_name_element.get_attribute("innerText")
			company_name = company_name.strip()
			# indices = company_name.split("\n")
			# print("COMPANY NAME FOUND: " + indices[0])
			# company_detail_element = driver.find_element_by_id("Company_Detail"+id_num)
			# company_detail = company_detail_element.get_attribute("innerText")
			# for line in company_detail.split("\n"):
			# 	line = line.strip()
			# 	if "," in line:
			# 		indices = line.split("\n")
			# 		location =  indices[0]
			# 		# print("LOCATION FOUND: " + location)
			# 	elif ("Phone: " in line) or ("Fax: " in line) or ("Cell: " in line): 
			# 		phone_number = line
			# 		# print("PHONE NUMBER FOUND: " + phone_number)
			# 	elif ("Website: " in line) or ("General email:" in line):
			# 		mylist = line.split()
			# 		indices = [i for i, s in enumerate(mylist) if 'www' in s]
			# 		if len(indices):
			# 			website = mylist[indices[0]]
			# 			# print("WEBSITE FOUND: " + website)
			# 		indices = [i for i, s in enumerate(mylist) if '@' in s]
			# 		if len(indices):
			# 			email = mylist[indices[0]]
			# 			# print("EMAIL FOUND: " + email)
			# 		break
			# company_information.append(location)
			# company_information.append(company_name)
			# company_information.append(phone_number)
			# company_information.append(website)
			# company_information.append(email)

			# writer.writerow(company_information)

			contacts = driver.find_elements_by_xpath("//*[starts-with(@id, 'O" + id_num + "') and contains(@id, 'N')]/preceding-sibling::a")		
			for c in contacts:
				onclick = c.get_attribute("onclick")
				driver.execute_script("arguments[0].click();", c)
				mylist = onclick.split("\'")
				contact_id = mylist[1].replace("O","")
				WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"contactimglarge"+contact_id)))
				company_image_element = driver.find_element_by_id("contactimglarge"+contact_id)
				company_image_element.screenshot("./Screenshots/"+company_name+"_"+contact_id+".png")
				
			driver.execute_script("arguments[0].click();", p)

	nextBtn = driver.find_elements_by_xpath("//*[contains(text(), 'Next >')]")
	driver.execute_script("arguments[0].click();", nextBtn[1])
	print("\n\nNEW PAGE\n\n")

# csvFile.close()



