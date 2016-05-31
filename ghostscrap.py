import mechanize
import re
from bs4 import BeautifulSoup
import os


def select_form(form):
  return form.attrs.get('id', None) == 'new_result'

index = 0

for i in range(1,210):
		line = ""
		index = index + 1
		usn = '1RV13CV' + '{0:0{width}}'.format(index, width=3)
		
		print usn
		try:
			browser = mechanize.Browser()
			browser.open('http://173.255.199.232:8001/results/getresult')
			browser.select_form(predicate=select_form)
			browser.form['result[usn]'] = usn
			browser.form['result[department]'] = ['5687f1b26e95525d0e0000b5',]
			browser.form['result[sem]'] = ['6',]
			#browser.form['result[year]'] = '2016'

			browser.submit()

			soup = BeautifulSoup(browser.response().read())
			ob = soup.prettify()

			res =  soup.find_all('p')
			for re in res:
				res = str(re)
				#res =  res[3:]
				#res = res[:-4]
				res = res.replace("<p>", "")
				res = res.replace("</p>", "")
				res = res.replace("<b>", "")
				res = res.replace("</b>", "")
				print res
				line = line + res
					

		except: 
			print "NO result for this usn!"
			file = open('scrapresultcv.txt','a+')
			file.write('NO result for this usn!')	

		

		file = open('scrapresultcv.txt','a+')
		file.write(line)
		file.write("#####################################################################")


