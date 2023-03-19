from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class SaucedemoTests:

    def __init__(self):
        self.driver = webdriver.Chrome()
        

    def test_username_password_fields_are_required(self):
        self.driver.get('https://www.saucedemo.com/')
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message-container error']")))
        assert 'Epic sadface: Username is required' == error_message.text
        sleep(2)

    def test_password_field_is_required(self):
        self.driver.get('https://www.saucedemo.com/')
        username_input = self.driver.find_element(By.ID, 'user-name')
        username_input.send_keys('standard_user')
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message-container error']")))
        assert 'Epic sadface: Password is required' == error_message.text
        sleep(2)

    def test_locked_out_user(self):
        self.driver.get('https://www.saucedemo.com/')
        username_input = self.driver.find_element(By.ID, 'user-name')
        password_input = self.driver.find_element(By.ID, 'password')
        username_input.send_keys('locked_out_user')
        password_input.send_keys('secret_sauce')
        sleep(2)
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message-container error']")))
        assert 'Epic sadface: Sorry, this user has been locked out.' == error_message.text
        sleep(2)

    def test_red_x_icons_disappear_on_closing_error_message(self):
        self.driver.get('https://www.saucedemo.com/')
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()
        username_input = self.driver.find_element(By.ID, 'user-name')
        password_input = self.driver.find_element(By.ID, 'password')
        username_input.click()
        username_input.send_keys(' ')
        password_input.click()
        password_input.send_keys(' ')
        error_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message-container error']")))
        sleep(2)
        close_btn = self.driver.find_element(By.XPATH, "//button[@class='error-button']")
        close_btn.click()
        red_x_icons = self.driver.find_elements(By.XPATH, "//div[@class='input-error form_group']/svg[@class='svg-inline--fa fa-exclamation-circle fa-w-16']")
        assert len(red_x_icons) == 0
        sleep(2)

    def test_successful_login(self):
        self.driver.get('https://www.saucedemo.com/')
        username_input = self.driver.find_element(By.ID, 'user-name')
        password_input = self.driver.find_element(By.ID, 'password')
        username_input.send_keys('standard_user')
        password_input.send_keys('secret_sauce')
        sleep(2)
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()
        sleep(2)

        inventoryItem = self.driver.find_elements(
            By.CLASS_NAME, 'inventory_item')

        print(f"Toplam Ürün sayısı: {len(inventoryItem)}")
testClass = SaucedemoTests()
#testClass.test_username_password_fields_are_required()
#testClass.test_password_field_is_required()
#testClass.test_locked_out_user()
#testClass.test_red_x_icons_disappear_on_closing_error_message()
#testClass.test_successful_login()