import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from selenium.webdriver.common.action_chains import ActionChains

class Test_001_login:
    baseurl = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_title(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            print("Title is matching")
            assert True
        else:
            print("Title is not matching")
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        self.lp.escape()
        login_act_title = self.driver.title
        if login_act_title == "Swag Labs":
            self.driver.close()
            print("Title is matching")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_login.png")
            self.driver.close()
            print("Title is not matching")
            assert False

    def test_logout(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        self.lp.logout_click()
        self.lp.logout_link()
        logout_act_title = self.driver.title
        if logout_act_title == "Swag Labs":
            print("logout_Title is matching")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout.png")
            self.driver.close()
            print("Logout_Title is not matching")
            assert False







