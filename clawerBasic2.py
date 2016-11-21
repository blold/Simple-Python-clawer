# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import codecs
import urllib2
import sys  

reload(sys)  
sys.setdefaultencoding('utf-8')  

# Get the source soup data from url
def getSourceSoup(url):

	html_content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html_content, 'html.parser')
	return soup

# Get the result from soup data and filter the result with input key word
def searchOutcomeFromKeyWord(soup,keyWord):
 
	results = soup.find_all('a', text=re.compile(ur".*({}).*".format(keyWord))) 
	resultsOfP = soup.find_all(text = re.compile(ur".*({}).*".format(keyWord)))
	allResult = results + resultsOfP

	for i in results:
		print i.encode('utf-8')
	for i in resultsOfP:
		print i.encode('utf-8')

	return allResult

# Save the filterd datas the local txt file
def saveToFile(title,datas):
	f = open(title +'.txt','w+')  
	for i in datas:
		f.write("%s" % i.encode('utf-8'))  
	f.close()  

	print u'File report：the txt fille is saved'  
	print u'please press any key to quit...'  
	raw_input(); 

#-------- Program Entrance ------------------  
print u"""#--------------------------------------- 
#   Name：Blold clawer
#   Version：1.0 
#   Author：Blold
#   Date：2016-10-24
#   Language：Python 2.7 
#   Function：search the input word and save the outcome to a local txt file
#--------------------------------------- 
"""  

searchWord = raw_input('Please input the key word：')  
print "The search word is: %s" % searchWord

# Call function  
url = 'http://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0x9a2d3b570004b523&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=7&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=1380&rsv_sug4=3078'
htmlS = getSourceSoup(url)
outCome = searchOutcomeFromKeyWord(htmlS,searchWord) 
saveToFile("Results", outCome)

