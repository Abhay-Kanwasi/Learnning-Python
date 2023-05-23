from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

firefox_service = Service('geckodriver.exe')
firefox_browser = webdriver.Firefox(service=firefox_service)

firefox_browser.get('https://github.com/')

firefox_browser.maximize_window()
assert 'github' in firefox_browser.page_source

# It will go to search bar
search = firefox_browser.find_element(By.ID('query-builder-test'))
search.clear() # Clear the search bar
search.send_keys('abhay_kanwasi') # Search for abhay_write