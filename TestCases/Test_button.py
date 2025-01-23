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
    username = readconfig.get_username()
    password = readconfig.get_password()
    logger = LogGen.loggen()

    def test_button_functions(self, setup):
        self.logger.info("*************** Test_Button_functions ******************")
        self.logger.info("*************** Verify_Button_functionality ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        #golden_urls = ["https://saucelabs.com/request-demo", "https://saucelabs.com/sign-up", "https://saucelabs.com/products"
                       #"https://saucelabs.com/resources/case-studies/verizon-media-accelerates-millions-of-tests-every-month-using-open-source-technology-and-sauce-labs",
                       #"https://saucelabs.com/resources/case-studies/walmart-embraces-test-automation-and-open-source-to-increase-coverage-and-deploy-more-often",
                       #"https://saucelabs.com/sign-up", "https://saucelabs.com/request-demo"]
        results = []
        url_results = []
        # Comparision variables
        request_demo_url = "https://saucelabs.com/request-demo"
        test_for_free_url = "https://saucelabs.com/sign-up"
        learn_more_url = "https://saucelabs.com/products"
        case_study1_url = "https://saucelabs.com/resources/case-studies/verizon-media-accelerates-millions-of-tests-every-month-using-open-source-technology-and-sauce-labs"
        case_study2_url = "https://saucelabs.com/resources/case-studies/walmart-embraces-test-automation-and-open-source-to-increase-coverage-and-deploy-more-often"
        sign_up_path_url = "https://saucelabs.com/sign-up"
        last_request_demo_xpath_url = "https://saucelabs.com/request-demo"
        self.lp.logout_click()
        #self.lp.driver.maximize_window()
        self.bc = Button_checks(self.driver)
        self.bc.about() # clicking the about button
        time.sleep(5)
        #button_methods = [self.bc.request_demo, self.bc.try_it_free, self.bc.learn_more, self.bc.read_case,
            #              self.bc.read_case1, self.bc.signup, self.bc.last_request]
        self.bc.request_demo()
        url_results.append(self.driver.current_url)
        self.driver.back()


        ''''
        self.bc.try_it_free()
        url_results.append(self.driver.current_url)
        self.driver.back()
        time.sleep(5)
        self.bc.learn_more()
        url_results.append(self.driver.current_url)
        self.driver.back()
        time.sleep(5)
        self.bc.read_case()
        url_results.append(self.driver.current_url)
        self.driver.back()
        time.sleep(5)
        self.bc.read_case1()
        url_results.append(self.driver.current_url)
        self.driver.back()
        time.sleep(5)
        self.bc.signup()
        url_results.append(self.driver.current_url)
        self.driver.back()
        time.sleep(5)
        self.bc.last_request()
        url_results.append(self.driver.current_url)
        self.driver.back()
        time.sleep(5)
        print(url_results)
'''









