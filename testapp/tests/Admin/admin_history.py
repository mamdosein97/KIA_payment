from selenium import webdriver
import unittest


class CheckActivities(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_check_users_activities(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8085/admin/panel")
        admin_history_button = driver.find_element_by_name("admin_history_btn")
        admin_history_button.click()
        assert driver.find_element_by_name("admin_history_table") is not None

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()