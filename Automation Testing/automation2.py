from selenium import webdriver
from selenium.webdriver.firefox.service import Service

firefox_service = Service('geckodriver.exe')

firefox_browser = webdriver.Firefox(service=firefox_service)

firefox_browser.maximize_window()
firefox_browser.get('https://www.seleniumeasy.com/')

assert 'Learn Selenium with Best Practices and Examples | Selenium Easy' in firefox_browser.title