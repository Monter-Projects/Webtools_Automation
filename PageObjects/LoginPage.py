from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Login:
    username_xpath = "// *[ @ id = 'user-name']"
    password_xpath = "// *[ @ id = 'password']"
    login_button = "//*[@id= 'login-button']"
    sidebar_logout = "// *[ @ id = 'react-burger-menu-btn']"
    logout_link_id = "logout_sidebar_link"
    product_data_xpath = "//*[@id='header_container']/div[2]/span"
    webtools_user_xpath = "//*[@id='inputIcon']"
    webtools_pass_xpath = "//*[@id='newpwd']"



    def __init__(self,driver):
        self.driver = driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH, self.username_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def set_webtools_username(self,username):
        self.driver.find_element(By.XPATH, self.webtools_user_xpath).clear()
        self.driver.find_element(By.XPATH, self.webtools_user_xpath).send_keys(username)

    def set_webtools_password(self,password):
        self.driver.find_element(By.XPATH, self.webtools_pass_xpath).clear()
        self.driver.find_element(By.XPATH, self.webtools_pass_xpath).send_keys(password)

    def login_click(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def logout_click(self):
        self.driver.find_element(By.XPATH, self.sidebar_logout).click()

    def logout_link(self):
        self.driver.find_element(By.ID, self.logout_link_id).click()

    def escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def product_page(self):
        self.driver.find_element(By.XPATH, self.product_data_xpath)






