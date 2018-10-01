import requests
from bs4 import BeautifulSoup
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

gmail_url = 'https://concord.onelogin.com/client/apps/select/59238665'
schoology_url = 'https://concord.onelogin.com/client/apps/select/59238678'
password = input('Password: ')

driver = webdriver.Chrome(executable_path='/Users/sambanks/Downloads/chromedriver')

def site_login():
    driver.get('https://concord.onelogin.com/login')

    driver.find_element_by_id('user_email').send_keys('samuel.banks')
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_id('user_submit').click()
    print(driver.current_url)

    driver.implicitly_wait(10)
    driver.find_element_by_class_name('sc-gzVnrw').click()

    driver.implicitly_wait(5)
    driver.get(gmail_url)

    driver.implicitly_wait(5)
    driver.find_element_by_class_name('U26fgb').click()

    write_email()

def write_email():  
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('div.T-I.J-J5-Ji.T-I-KE.L3').click()

    recipient = 'laird.donohue@concordacademy.org'
    subject = 'Automatic Email'
    content = 'Hi, you have received an automatic email from python.'

    driver.find_element_by_name('to').send_keys(recipient, Keys.TAB)
    sleep(2)
    driver.find_element_by_id(':mr').send_keys(subject)
    driver.find_element_by_id(':nv').send_keys(content)
    driver.find_element_by_id(':mh').click()

site_login()

