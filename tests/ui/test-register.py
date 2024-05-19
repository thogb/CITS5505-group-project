from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

# This testing file is created with the help of ChatGPT for boilerplate setup
# and modified.

class TestRegister():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_register(self):
        self.driver.get("http://127.0.0.1:5000/register")
        self.driver.set_window_size(1366, 768)

        self.driver.find_element(By.NAME, "email").send_keys("testingtest@gmail.com")
        self.driver.find_element(By.NAME, "first_name").send_keys("selenium")
        self.driver.find_element(By.NAME, "last_name").send_keys("testing")
        self.driver.find_element(By.NAME, "password").send_keys("Password12#$")
        self.driver.find_element(By.NAME, "confirm_password").send_keys("Password12#$")

        self.driver.find_element(By.NAME, "submit").click()

        time.sleep(2)

        success_message = self.driver.find_element(By.CLASS_NAME, "toast-body").text
        assert "Success" in success_message

if __name__ == "__main__":
    pytest.main([__file__])