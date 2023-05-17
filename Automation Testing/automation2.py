from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

firefox_service = Service('geckodriver.exe')
firefox_browser = webdriver.Firefox(service=firefox_service)

firefox_browser.maximize_window()
firefox_browser.get('https://www.seleniumeasy.com/')

assert 'Learn Selenium with Best Practices and Examples | Selenium Easy' in firefox_browser.title

button = firefox_browser.find_element(By.CLASS_NAME, 'form-control')
print(button.get_attribute('innerHTML'))
