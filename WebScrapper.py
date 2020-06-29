#author Asan Hai

#Importing all packages
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re
import random

#target website that is Scrapped
url='http://www.asanhai.com/'

#Sending request 
send_req= Request(url)

#Purpose of Scraping 
web_page= urlopen(send_req).read()

#apply beautifulsoup
apply_soup = soup(web_page, "html.parser")

#Scrapping title of website
title =apply_soup.find('title')
print(title)

#scrapping header section
head =apply_soup.find('head')
print(head)

#scrapping a link
a =apply_soup.find('a')
print(a)

#scrapping all links 
for link in apply_soup.find_all('a'):
    print(link.get('href'))

#Scrapping all the text in website
text =apply_soup.text
print(text)

#Scrapping the source of all images
images = apply_soup.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')