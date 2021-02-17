# download proper chromedriver for your version of chrome and add its path to executable path

from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:/Users/Marcin/Documents/software/chromedriver.exe")
browser.get('http://selenium.dev/')
