import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestMyForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_submit_form(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/my-view/")

        # Fill out the form
        driver.find_element(By.NAME, "name").send_keys("John Doe")
        driver.find_element(By.NAME, "email").send_keys("john@example.com")
        driver.find_element(By.NAME, "message").send_keys("This is a test message")

        # Submit the form
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

        # Add a wait to see the result
        time.sleep(2)

        # Add assertions based on the expected behavior after form submission
        # Example: self.assertIn("success", driver.current_url)

if __name__ == "__main__":
    unittest.main()
