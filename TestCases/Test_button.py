import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from selenium.webdriver.common.action_chains import ActionChains
from Utilites.ReadProperties import readconfig
from Utilites.CustomLogger import LogGen
import pytest_html
from PageObjects.button_funtions import Button_checks

class Test_001_button_checks:
    baseurl = readconfig.getappurl()
    username = readconfig.get_webtoolsusername()
    password = readconfig.get_webtoolspassword()
    logger = LogGen.loggen()

    # Test-Case to test Docs link
    def test_button_function_docs(self, setup):
        self.logger.info("*************** Test_Button_Docs_functions ******************")
        self.logger.info("*************** Verify_Docs_Button_functionality ******************")
        Docs_title = "WebTools | My Docs"
        Configure_title = "Configure"
        Fsr_url = "https://10.210.219.37/wt4/brhome?lang=en"
        Home_title = "WebTools"
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed()
        self.bc.Docs() # clicking the about button
        current_title = self.driver.title
        if current_title == Docs_title:
            self.logger.info("*************** Docs_Check_passed ******************")
            print("Docs_check_test_is_passed")
            self.driver.close()
            assert True
        elif current_title != Docs_title:
            self.logger.info("*************** Docs_Check_failed ******************")
            print("Docs_check_test_is_failed")
            self.driver.close()
            assert False
        else:
            self.logger.info("*************** Problem in searching element on the page ******************")
            print("Problem in searching element on the page")
            self.driver.close()
            assert False

    # Test-case to test configure function
    def test_button_function_configure(self, setup):
        self.logger.info("*************** Test_Button_configure_functions ******************")
        self.logger.info("*************** Verify_Docs_configure_functionality ******************")
        Configure_title = "Configure"
        Fsr_url = "https://10.210.219.37/wt4/brhome?lang=en"
        Home_title = "WebTools"
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed()
        self.bc.Configure()  # clicking the configure button
        self.lp = Login(self.driver)
        self.lp.set_webtools_username(self.username)
        self.lp.set_webtools_password(self.password)
        self.bc.login()
        current_title = self.driver.title
        if current_title == Configure_title:
            self.logger.info("*************** Configure_Check_passed ******************")
            print("Configure_check_test_is_passed")
            self.driver.close()
            assert True
        elif current_title != Configure_title:
            self.logger.info("*************** Docs_Check_failed ******************")
            print("Configure_check_test_is_failed")
            self.driver.close()
            assert False
        else:
            self.logger.info("*************** Problem in searching element on the page ******************")
            print("Problem in searching element on the page")
            self.driver.close()
            assert False








