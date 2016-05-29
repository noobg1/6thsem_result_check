import requests
import time
import os
from bs4 import BeautifulSoup
import filecmp

url = "http://173.255.199.232:8001/results/getresult"
index = 0
fstatic = ""


					

def music():
	os.system("start F:/rvceresult/dantanaka.mp3")
	exit()

def music_warning():
	print "Warning! There is a change in the page!"
	os.system("start F:/rvceresult/warning.mp3")
	time.sleep(2)
	

def rv6sem():
		global index,fstatic
		result = requests.get(url)
		soup = BeautifulSoup(result.content,'html.parser') 
		alltext = soup.get_text()
		s = "6"		
		alltext = str(alltext)
		six =  soup.find(value=s)
		flag = 0
		
		f = open('static.txt','w+')
		fr = open('dynamic.txt','w+')
		fr.write(alltext)
		
		if index == 0:
			index = 1
			f.write(alltext)
			f.seek(0)
			fstatic = f.read()
			
		fr.seek(0)		
		fdynamic = fr.read()
	
		if fstatic == fdynamic:
			print ""
		else:
			 music_warning()

		

		if '<option value="'+s+'">'+s+'</option>' == str(six):
				print "Check"
				flag = 1
		
		for text in alltext:
			if s == text and flag == 1:
					print "########### Resuts Out! ############"
					music()
			

while(True):
		rv6sem()
		print "Keep calm and wait!"
		time.sleep(5)


