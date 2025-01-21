import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from selenium.webdriver.common.action_chains import ActionChains
from Utilites.ReadProperties import readconfig
from Utilites.CustomLogger import LogGen
from Utilites import XLUtils
import openpyxl
import pytest_html

class Test_002_DDT_login:
    baseurl = readconfig.getappurl()
    path = ".\\TestData\\LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("*************** Test_002_DDT_login ******************")
        self.logger.info("*************** Verify_Different_login test started ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in a excel", self.rows)
        result_lst = []
        for r in range(2,self.rows+1):
            self.lp = Login(self.driver)
            self.username = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.login_click()
            #time.sleep(5)
            act_title = self.driver.title
            exp_title = "Swag Labs"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.lp.logout_click()
                    self.lp.logout_link()
                    print("Test-case is Passed")
                    self.logger.info("*************** Test_002_DDT_login Execution Passed ******************")
                    result_lst.append("Pass")
                elif self.exp == "Fail":
                    self.driver.save_screenshot(".\\Screenshots\\" + "login_failure" + str(r) + ".png")
                    #self.driver.close()
                    self.logger.info("*************** Test_002_DDT_login Execution Failed ******************")
                    print("Test-case is Failed")
                    result_lst.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Fail":
                    #self.driver.close()
                    self.lp.logout_click()
                    self.lp.logout_link()
                    print("Test-case is Passed")
                    self.logger.info("*************** Test_002_DDT_login Passed ******************")
                    result_lst.append("Pass")
                elif self.exp == "Pass":
                    self.driver.save_screenshot(".\\Screenshots\\" + "login_failure" + str(r) + ".png")
                    #self.driver.close()
                    self.logger.info("*************** Test_002_DDT_login Execution Failed ********")
                    print("Test-case is Failed")
                    result_lst.append("Fail")
        if "Fail" not in result_lst:
            print("Test-case is Passed")
            self.logger.info("*************** Test_002_DDT_login Passed ******************")
            self.driver.close()
            assert True
        else:
            print("Test-case is Failed")
            self.logger.info("*************** Test_002_DDT_login Failed ******************")
            self.driver.close()
            assert False















