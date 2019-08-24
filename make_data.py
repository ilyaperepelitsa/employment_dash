import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import re
import selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
import json

dirpath = os.getcwd()

def init_driver():
    path_to_chromedriver = os.path.join(dirpath, "chromedriver")
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    driver.wait = WebDriverWait(driver, 5)
    return driver

def wait_for(condition_function):
  start_time = time.time()
  while time.time() < start_time + 3:
    if condition_function():
      return True
    else:
      time.sleep(0.1)
  raise Exception(
   'Timeout waiting for {}'.format(condition_function)
  )


class wait_for_page_load(object):

  def __init__(self, browser):
    self.browser = browser

  def __enter__(self):
    self.old_page = self.browser.find_element_by_tag_name('html')

  def page_has_loaded(self):
    new_page = self.browser.find_element_by_tag_name('html')
    return new_page.id != self.old_page.id

  def __exit__(self, *_):
    wait_for(self.page_has_loaded)




data = json.load(open(os.path.join(dirpath, "credentials.json")))
# data


browser = init_driver()
# browser.wait = WebDriverWait(browser, 2)

with wait_for_page_load(browser):
    # browser.find_element_by_link_text('my link').click()
    browser.get('http://hh.ru')


browser.find_element(By.XPATH, '//input[@name="username"]').send_keys(data['username'])
browser.find_element(By.XPATH, '//input[@name="password"]').send_keys(data['password'])
browser.find_element(By.XPATH, '//input[@data-qa="login-submit"]').click()

browser.get('https://hh.ru/applicant/negotiations?from=header_new')
browser.find_element(By.XPATH, '//a[@class="bloko-tabs__item"]').click()

"//*[@class="responses-table-tbody"]"


# browser.send_keys("0.00000005")

# browser.get('http://hh.ru')

# //input[@name="username"]
