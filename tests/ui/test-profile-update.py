import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# This testing file is created with the help of ChatGPT for boilerplate setup
# and modified.

class TestLogin():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

        self.driver.get("http://127.0.0.1:5000/login")
        self.driver.set_window_size(1366, 968)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("testingtest@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Password12#$")

        self.driver.find_element(By.NAME, "submit").click()

        time.sleep(2)
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_update_profile(self):
        self.driver.get("http://127.0.0.1:5000/me")

        self.driver.find_element(By.NAME, "phone_number").clear()
        self.driver.find_element(By.NAME, "phone_number").send_keys("452778383")

        self.driver.find_element(By.NAME, "address").clear()
        self.driver.find_element(By.NAME, "address").send_keys("123 test street")

        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.XPATH, "//select[@name='city']/option[@value='2']").click()

        self.driver.find_element(By.NAME, "submit").click()

        time.sleep(2)

        # Refresh page
        self.driver.get("http://127.0.0.1:5000/me")

        phone_number = self.driver.find_element(By.NAME, "phone_number").get_attribute("value")
        address = self.driver.find_element(By.NAME, "address").get_attribute("value")
        city = self.driver.find_element(By.NAME, "city").get_attribute("value")

        assert phone_number == "452778383"
        assert address == "123 test street"
        assert city == "2"

        

if __name__ == "__main__":
    pytest.main([__file__])