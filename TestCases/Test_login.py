import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from selenium.webdriver.common.action_chains import ActionChains
from Utilites.ReadProperties import readconfig
from Utilites.CustomLogger import LogGen
import pytest_html

class Test_001_login:
    #baseurl = readconfig.getappurl()
    username = readconfig.get_username()
    password = readconfig.get_password()

    logger = LogGen.loggen()

    def test_title(self,setup):
        self.logger.info("*************** Test_Title ******************")
        self.logger.info("*************** Verify_Home-Page_Title ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            print("Title is matching")
            self.driver.close()
            self.logger.info("*************** Verify_Home-Page_Title Passed ******************")
            assert True
        else:
            print("Title is not matching")
            self.driver.close()
            self.logger.error("*************** Verify_Home-Page_Title Failed ******************")
            assert False

    def test_login(self,setup):
        self.logger.info("*************** Test_login test started ******************")
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
            self.logger.info("*************** Test_login test is passed ******************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_login.png")
            self.driver.close()
            print("Title is not matching")
            self.logger.error("*************** Test_login test is failed ******************")
            assert False

    def test_logout(self,setup):
        self.logger.info("*************** Test_logout test started ******************")
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
            self.logger.info("*************** Test_logout test passed ******************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout.png")
            self.driver.close()
            print("Logout_Title is not matching")
            self.logger.error("*************** Test_logout test failed ******************")
            assert False







