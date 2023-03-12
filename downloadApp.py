from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pytube import YouTube
import time
import os

def find_name_video(source,by,query): 
	element = WebDriverWait(source, 10).until(EC.presence_of_all_elements_located((by, query)))
	return element

def check_path_download(drive, path):
	if not os.path.exists(path):
		os.mkdir(path)

	name = find_name_video(drive, By.XPATH, '//div[@id="title"][@class="style-scope ytd-watch-metadata"]')[0].text
	direction = os.path.join(path, name)
	return direction

if __name__ == "__main__":
	path = 'video'
	url = 'https://www.youtube.com/watch?v=1-SONRlZ9cQ&t=2057s'
	'''
  		Cài đặt các option của chrome driver dẫn đến đường dẫn url
	'''
	chrome_options = webdriver.ChromeOptions()
	drive = webdriver.Chrome('chromedriver',options=chrome_options)
	drive.implicitly_wait(10)
	drive.get(url)

	path_download = check_path_download(drive, path)
	drive.quit()

	yt = YouTube(url) 
	yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	yt.download(path_download) #youtube highest quality video

	
	# path = 'video'
	# if not os.path.exists(path):
	# 	os.mkdir(path)
	