from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
import time
chrome_options = Options()

browser = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
browser.get('http://localhost:8000')
assert 'Django' in browser.title
browser.quit()