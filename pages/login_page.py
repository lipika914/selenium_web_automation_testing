# from utils.base_page import BasePage
# import time
# class LoginPage(BasePage):
#   def __init__(self, driver):
#    super().__init__(driver)
#    self.url = "https://rahulshettyacademy.com/loginpagePractise/"
#   def open(self):
#    self.driver.get(self.url)
#   def login(self, username, password):
#     self.wait_for_element("id", "username").send_keys(username)
#     self.wait_for_element("id", "password").send_keys(password)
#     self.wait_for_element("id", "signInBtn").click()
#     time.sleep(20)
from selenium.webdriver.common.by import By
from utils.base_page import BasePage
import time

class LoginPage(BasePage):

# Locators
 USERNAME_FIELD = (By.ID, "username")
 PASSWORD_FIELD = (By.ID, "password")
 LOGIN_BUTTON = (By.ID, "signInBtn")
 # Constructor
 def __init__(self, driver):
  super().__init__(driver)
 # Page Actions
 def enter_username(self, username):
  self.enter_text(self.USERNAME_FIELD, username)
 def enter_password(self, password):
  self.enter_text(self.PASSWORD_FIELD, password)
 def click_login(self):
  self.click(self.LOGIN_BUTTON)
  time.sleep(20)