import requests
import time
import os
from bs4 import BeautifulSoup

url = "http://173.255.199.232:8001/results/getresult"

result = requests.get(url)
soup = BeautifulSoup(result.content,'html.parser') 
alltext = soup.text

def rv6sem():
		six =  soup.find(value="6")
		flag = 0

		if '<option value="6">6</option>' == str(six):
				print "Check"
				flag = 1
		
		for texts in alltext:
			if '6' == texts and flag == 1:
					print "Resut Out!"
					music()
			if '6' == texts or flag == 1:
					print "Warning! Check manually once"
					music_warning()
					

def music():
	os.system("start F:/rvceresult/dantanaka.mp3")
	exit()
def music_warning():
	os.system("start F:/rvceresult/warning.mp3")
	sleep(60)

while(True):
		rv6sem()
		print "Keep calm and wait!"
		time.sleep(5)


