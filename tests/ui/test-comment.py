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

    def test_post_comment(self):
        self.driver.get("http://127.0.0.1:5000/items/4")

        self.driver.find_element(By.ID, "commentInput").click()
        self.driver.find_element(By.ID, "commentInput").send_keys("This is a test comment.")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.ID, "btnPostComment"))

        self.driver.find_element(By.ID, "btnPostComment").click()

        time.sleep(2) 

        comment_list = self.driver.find_element(By.ID, "commentList").text
        assert "This is a test comment." in comment_list

    def test_delete_post(self):
        self.driver.get("http://127.0.0.1:5000/items/4")

        comments = self.driver.find_elements(By.CSS_SELECTOR, ".comment")
        last_comment = comments[-1]

        self.driver.execute_script("arguments[0].scrollIntoView(true);", last_comment)

        delete_button = last_comment.find_element(By.CSS_SELECTOR, ".icon-button-delete")
        delete_button.click()

        time.sleep(2)

        comment_list = self.driver.find_element(By.ID, "commentList").text
        assert "This is a test comment." not in comment_list


if __name__ == "__main__":
    pytest.main([__file__])