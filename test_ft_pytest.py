from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = "/Users/sanghyuk/.local/bin/chromedriver"
BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

def get_browser():

    option = webdriver.ChromeOptions()
    option.binary_location = BRAVE_PATH
    service = Service(executable_path=DRIVER_PATH)
    browser = webdriver.Chrome(options=option, service=service)

    return browser

def test_title_header(url: str='http://127.0.0.1:8000/'):
    browser = get_browser()
    browser.get(url)
    assert 'To-Do' in browser.title

