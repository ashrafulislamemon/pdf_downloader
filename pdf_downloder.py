import os
import sys
import time
import webbrowser
from urllib.parse import urlparse
import re

import requests
from bs4 import BeautifulSoup, Comment
from selenium import webdriver

def remove_unwanted_chars(text):
    unwanted_chars = '%$#^&*'
    translation_table = str.maketrans('', '', unwanted_chars)
    return text.translate(translation_table)


search_input = sys.argv[1]
num = sys.argv[2]
browser = webdriver.Chrome()
time.sleep(5)
url='https://www.google.com/search?q='+search_input+'&num='+num
browser.get(url)
pageContent = browser.page_source
soup = BeautifulSoup(pageContent,'html.parser')




search_result=soup.select('.yuRUbf > div > span > a[href]')
# print(search_result)

all_link=[]

for link in search_result[:100]:
   accual_links=link.get('href')
   all_link.append(accual_links)
print(all_link)
print(len(all_link))   
all_pdf_link=[]



for i in all_link:
    if i[-4:]==".pdf":
        all_pdf_link.append(i)
    else:
        continue
print(all_pdf_link)
print(len(all_pdf_link))        

def download_pdf(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF downloaded successfully and saved as '{save_path}'")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")




# os.makedirs(search_input[:-4])
for i in all_pdf_link:
    try:

        pdf_url = i
        file_path = remove_unwanted_chars(pdf_url.split('/')[-1])

        download_pdf(pdf_url, file_path)
        time.sleep(5)
    except:
        print('not download')
        
         

while True:
    pass
