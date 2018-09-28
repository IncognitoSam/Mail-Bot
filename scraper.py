import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path='/Users/sambanks/Downloads/chromedriver')
password = input('Password: ')

def site_login():
    driver.get('https://concord.onelogin.com/login')

    driver.find_element_by_id('user_email').send_keys('samuel.banks')
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_id('user_submit').click()
    print(driver.current_url)

    driver.implicitly_wait(10)
    driver.find_element_by_class_name('sc-gzVnrw').click()

    driver.implicitly_wait(5)
    driver.get('https://concord.onelogin.com/client/apps/select/59238678')

    driver.implicitly_wait(5)
    scrape_data()

def scrape_data():
    # page = requests.get('https://app.schoology.com/home')
    # soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)

    html_source = driver.page_source
    print(html_source)

    # links = soup.find_all('upcoming-events')
    # print(links)

site_login()

