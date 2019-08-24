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


def init_driver():
    path_to_chromedriver = "chromedriver"
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    driver.wait = WebDriverWait(driver, 5)
    return driver
