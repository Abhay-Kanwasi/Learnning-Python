# Old way 
# from selenium import webdriver
# firefox_browser = webdriver.Firefox(executable_path='geckodriver.exe')



# In case if it's in a specific folder we can give the path
# (executable_path=r'C:\Users\djoke\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe')

# print(firefox_browser)

# If you want to go to any website(e.x - github)
# firefox_browser.get('https://github.com')

# Firefox will open in full size window
# firefox_browser.maximize_window()

# New way because selenium depricated the 'executable_path'
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

firefox_service = Service('geckodriver.exe')
firefox_browser = webdriver.Firefox(service=firefox_service)

firefox_browser

