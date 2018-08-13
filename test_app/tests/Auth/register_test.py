from selenium import webdriver
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_successfully_registered(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8085/register/")
        first_name = driver.find_element_by_name("firstName")
        last_name = driver.find_element_by_name("lastName")
        password = driver.find_element_by_name("password")
        repassword = driver.find_element_by_name("repassword")
        email = driver.find_element_by_name("email")
        phone_number = driver.find_element_by_name("phoneNumber")
        register_button = driver.find_element_by_name("registerButton")
        first_name.send_keys("ali")
        last_name.send_keys("alavi")
        password.send_keys("1234")
        repassword.send_keys("1234")
        email.send_keys("ali@gmail.com")
        phone_number.send_keys("09121234567")
        register_button.click()

        try:
            WebDriverWait(driver, 2) \
                .until(expected_conditions.presence_of_element_located((By.NAME, "register_successful")))
            flag = True
        except TimeoutException:
            flag = False

        assert flag

    def test_passwords_equality(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8085/register/")
        first_name = driver.find_element_by_name("firstName")
        last_name = driver.find_element_by_name("lastName")
        password = driver.find_element_by_name("password")
        repassword = driver.find_element_by_name("repassword")
        email = driver.find_element_by_name("email")
        phone_number = driver.find_element_by_name("phoneNumber")
        register_button = driver.find_element_by_name("registerButton")
        first_name.send_keys("ali")
        last_name.send_keys("alavi")
        password.send_keys("1234")
        repassword.send_keys("123456")
        email.send_keys("ali@gmail.com")
        phone_number.send_keys("09121234567")
        register_button.click()

        try:
            WebDriverWait(driver, 2) \
                .until(expected_conditions.presence_of_element_located((By.NAME, "not_equal_pass")))
            flag = True
        except TimeoutException:
            flag = False

        assert flag

    # def test_not_empty_field(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8085/register/")
    #     first_name = driver.find_element_by_name("firstName")
    #     last_name = driver.find_element_by_name("lastName")
    #     password = driver.find_element_by_name("password")
    #     repassword = driver.find_element_by_name("repassword")
    #     email = driver.find_element_by_name("email")
    #     phone_number = driver.find_element_by_name("phoneNumber")
    #     register_button = driver.find_element_by_name("registerButton")
    #     first_name.send_keys("ali")
    #     last_name.send_keys("alavi")
    #     password.send_keys("1234")
    #     repassword.send_keys("1234")
    #     email.send_keys("ali@gmail.com")
    #     phone_number.send_keys("09121234567")
    #     register_button.click()
    #     assert driver.find_element_by_name("emptyField") is not None

    # def test_valid_email(self):
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8085/register/")
    #     first_name = driver.find_element_by_name("firstName")
    #     last_name = driver.find_element_by_name("lastName")
    #     password = driver.find_element_by_name("password")
    #     repassword = driver.find_element_by_name("repassword")
    #     email = driver.find_element_by_name("email")
    #     phone_number = driver.find_element_by_name("phoneNumber")
    #     register_button = driver.find_element_by_name("registerButton")
    #     first_name.send_keys("ali")
    #     last_name.send_keys("alavi")
    #     password.send_keys("1234")
    #     repassword.send_keys("1234")
    #     email.send_keys("aligmail.com")
    #     phone_number.send_keys("09121234567")
    #     register_button.click()
    #     assert driver.find_element_by_name("invalidEmail") is not None

    def test_valid_phone_number(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8085/register/")
        first_name = driver.find_element_by_name("firstName")
        last_name = driver.find_element_by_name("lastName")
        password = driver.find_element_by_name("password")
        repassword = driver.find_element_by_name("repassword")
        email = driver.find_element_by_name("email")
        phone_number = driver.find_element_by_name("phoneNumber")
        register_button = driver.find_element_by_name("registerButton")
        first_name.send_keys("ali")
        last_name.send_keys("alavi")
        password.send_keys("1234")
        repassword.send_keys("1234")
        email.send_keys("ali@gmail.com")
        phone_number.send_keys("rfdkfojaoj")
        register_button.click()

        try:
            WebDriverWait(driver, 2) \
                .until(expected_conditions.presence_of_element_located((By.NAME, "invalid_phone")))
            flag = True
        except TimeoutException:
            flag = False

        assert flag

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()