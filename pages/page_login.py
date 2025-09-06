import pytest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    LOGIN_LOCATOR = ('xpath', "//input[@id='username']")
    PASS_LOCATOR = ('xpath', "//input[@id='password']")
    BUTTON_LOCATOR = ('xpath', "//button[@class='radius']")
    ALERT_LOCATOR = ('xpath', "//div[@id='flash']")
    URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10,1)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self,username):
        self.driver.find_element(*self.LOGIN_LOCATOR).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.PASS_LOCATOR).send_keys(password)

    def login_click(self):
        self.driver.find_element(*self.BUTTON_LOCATOR).click()

    def get_alert_text(self):
        alert = self.wait.until(EC.visibility_of_element_located(self.ALERT_LOCATOR))
        return alert.text