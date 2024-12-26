from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.login_page import LoginPage
from config.config import Config as con
class TestLogin:
 def setup_method(self):
  self.driver = webdriver.Chrome()
  self.driver.get(con.BASE_URL)
  self.login_page = LoginPage(self.driver)
 def teardown_method(self):
  self.driver.quit()
 def test_valid_login(self):
  self.login_page.enter_username(con.USERNAME)
  self.login_page.enter_password(con.PASSWORD)
  self.login_page.click_login()
  #assert "Dashboard" in self.driver.title