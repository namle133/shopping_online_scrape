from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

def create_web_driver(url: str, location: str) -> WebDriver:
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    # set chrome driver options to disable any popup's from the website
    # to find local path for chrome profile, open chrome browser
    # and in the address bar type, "chrome://version"
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('start-maximized')
    # To disable the message, "Chrome is being controlled by automated test software"
    chrome_options.add_argument("disable-infobars")
    # Pass the argument 1 to allow and 2 to block
    chrome_options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2
        })
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    if location == 'shopee':
        return auto_login_shopee(driver)
    delay = 4 #secods
    WebDriverWait(driver, delay)
    print(type(driver))
    print ("Page is ready")
    sleep(4)
    return driver

def auto_login_shopee(driver : WebDriver) -> WebDriver:
    sleep(4)
    load_dotenv()
    
    username = os.getenv("username")
    password = os.getenv("password")
    
    driver.find_element("name", "loginKey").send_keys(username)
    # find password input field and insert password as well
    driver.find_element("name", "password").send_keys(password)
    # click login button
    sleep(3)
    # click login button
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button').click()

    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=8).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    print ("Page is ready")
    sleep(20)
    return driver
