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
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://127.0.0.1:5000/login")
        self.driver.set_window_size(1366, 768)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("testingtest@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Password12#$")

        self.driver.find_element(By.NAME, "submit").click()

        time.sleep(2)

        success_message = self.driver.find_element(By.CLASS_NAME, "toast-body").text
        assert "Success" in success_message

if __name__ == "__main__":
    pytest.main([__file__])