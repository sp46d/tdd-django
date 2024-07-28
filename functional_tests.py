from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

driver_path = "/Users/sanghyuk/.local/bin/chromedriver"
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
s = Service(executable_path=driver_path)

browser = webdriver.Chrome(options=option, service=s)
browser.get('http://127.0.0.1:8000/')

assert 'success' in browser.title