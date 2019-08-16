import csv
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/fpang/Desktop/code/oceanit-2019/ITP303-Final-Project-9285bf31fdda.json"
from os import listdir
from os.path import isfile, join
from google.cloud import vision
import google.auth
import google.auth.transport.requests

def detect_text(path):
	with open(path, 'rb') as image_file:
		content = image_file.read()
		image = vision.types.Image(content=content)

		for i in range(5):
			try:
				client = vision.ImageAnnotatorClient()	
				response = client.text_detection(image=image)
				texts = response.text_annotations
				print(path)
				info_list = texts[0].description.split("\n")
				image_file.close()
				return info_list
			except Exception as ex:
				print(ex)
				print("Retrying {} time with google vision api...".format(i))
				image_file.close()

def writeRowCSV(company_name, mylist, writer):
	newList = []
	name = "None"
	title = "None"
	phone = "None"
	cell = "None"
	email = "None"
	print(mylist)
	for i in mylist:
		details = i.split(": ")
		if "Name" in details[0]:
			try:
				name = details[1]
			except IndexError as ie:	
				name = "None"
		elif "Title" in details[0]:
			try:
				title = details[1]
			except IndexError as ie:
				title = "None"
		elif "Phone" in details[0]:
			try:
				phone = details[1]
			except IndexError as ie:
				phone = "None"
		elif "Cell" in details[0]:
			try:
				cell = details[1]
			except:
				cell = "None"
		elif ("Email" in details[0]) and len(details)==2:
			try:
				email = details[1]
			except IndexError as ie:
				email = "None"
		elif "@" in details[0]:
			try:
				email = details[0]
			except IndexError as ie:	
				email = "None"
	newList.append(company_name)
	newList.append(title)
	newList.append(name)
	newList.append(email)
	newList.append(phone)
	newList.append(cell)
	print(newList)
	print()
	writer.writerow(newList)

def writeFail(company_name, writer):
	newList = []
	name = "FAIL"
	title = "FAIL"
	phone = "FAIL"
	cell = "FAIL"
	email = "FAIL"
	print(mylist)	
	newList.append(company_name)
	newList.append(title)
	newList.append(name)
	newList.append(email)
	newList.append(phone)
	newList.append(cell)
	print(newList)
	print()
	writer.writerow(newList)

header = ['Company_Name', 'Title', 'Name', 'Email', 'Phone', 'Cell']
with open('contactsD.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	# tempList = detect_text("/Users/fpang/Desktop/code/oceanit-2019/Screenshots//AKA ENERGY GROUP LLC_18N7.png")
	# writeRowCSV("AKA ENERGY GROUP LLC", tempList, writer)
	cwd = os.getcwd()
	screenshot_dir = cwd+"/D/"
	onlyfiles = [f for f in listdir(screenshot_dir) if isfile(join(screenshot_dir, f))]
	numFiles = len(onlyfiles)
	for i, f in enumerate(onlyfiles):
		print("(D) " + str(i+1)+ " of "+str(numFiles))
		if i%10==0:
			credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
			credentials.refresh(google.auth.transport.requests.Request())
		if ".png" in f:
			company_name = f.split("_")[0]
			mylist = detect_text(screenshot_dir+"/"+f)
			if mylist:
				writeRowCSV(company_name, mylist, writer)
			else:
				writeFail(company_name, writer)

csvFile.close()