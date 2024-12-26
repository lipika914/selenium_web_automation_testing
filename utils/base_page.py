# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def wait_for_element(self, by, value, timeout=100):
#         return WebDriverWait(self.driver, timeout).until(
#             EC.presence_of_element_located((by, value))
#         )
#     def quit(self):
#         self.driver.quit()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BasePage:
 def __init__(self, driver):
  self.driver = driver
  self.wait = WebDriverWait(driver, 10)
 def find_element(self, locator):return self.wait.until(EC.visibility_of_element_located(locator))
 def click(self, locator):
  self.find_element(locator).click()

 def enter_text(self, locator, text):
  self.find_element(locator).send_keys(text)