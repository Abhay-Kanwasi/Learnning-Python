from selenium import webdriver

firefox_browser = webdriver.Firefox(executable_path=r'C:\Users\djoke\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe')

# print(firefox_browser)
# firefox_browser.get('https://github.com')

firefox_browser.maximize_window()

