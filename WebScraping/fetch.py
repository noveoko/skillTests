from selenium import webdriver
import configparser
import time 
import parseUpwork as pu
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import json


config = configparser.ConfigParser()
config.read('./config.ini')

target = config.sections()[0]
username = config[target]['Username']
password = config[target]['Password']
secretAnswer = config[target]['SecretAnswer']

#set up proxies

rproxy = RequestProxy()
proxies = rproxy.get_proxy_list() 
PROXY = proxies[0].get_address()
# download proper chromedriver for your version of chrome and add its path to executable path
PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "proxyType":"MANUAL",  
}

browser = webdriver.Chrome(executable_path="C:/Users/Marcin/Documents/software/chromedriver.exe")
browser.implicitly_wait(3)
# open login page
loginPage = config[target]['loginPage']
loginTitle = config[target]['loginTitle']

max_runs = 10
data_fetched = False
runs = 0

while data_fetched != True or runs <= max_runs:
    try:
        print(f"Attempt number:{runs} for Domain: {target}")
        runs+=1
        browser.get(f'{loginPage}')
        if browser.title == "Log In - Upwork":
        # log in to page using credentials
            try: 
                username_input = browser.find_element_by_id("login_username")
                username_input.send_keys(username)
                loginContinue_button = browser.find_element_by_id("login_password_continue")
                loginContinue_button.click()
                time.sleep(3)
                password_input = browser.find_element_by_id("login_password")
                password_input.send_keys(password)
                #login_rememberme_checkbox = browser.find_element_by_id("login_rememberme")
                #login_rememberme_checkbox.click()
                login_button = browser.find_element_by_id("login_control_continue")
                login_button.click()
                time.sleep(3)
                if verify := browser.find_element_by_id("login_deviceAuthorization_answer"):
                    verify.send_keys(secretAnswer)
                    continue_verify_button = browser.find_element_by_id("login_control_continue")
                    continue_verify_button.click()
                else:
                    print("Verification question not asked!")
                #extract critical information
                main_page = browser.page_source()
                with open('main_page.html','w',encoding='utf-8') as outfile:
                    outfile.write(main_page)
                #extract data
                try:
                    data = pu.extract_info(main_page)
                    with open('upwork_profile.json','w',encoding='utf-8') as outfile:
                        outfile.write(json.dump(data))
                        data_fetched = True
                except Exception as ee:
                    print(ee)
                #save data to json

            except Exception as ee:
                print(ee)

        else:
            print("Title mismatch!")

    except Exception as ee:
        print(ee)






