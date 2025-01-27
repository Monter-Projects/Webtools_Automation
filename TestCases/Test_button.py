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
        #configure_results = []
        configure_results = {"job_submission": "Pass", "job_management": "Pass", "network": "Pass",
                             "security": "Pass", "rip": "Pass", "scan": "Pass", "user_acc": "Pass"}
        if current_title == Configure_title:
            self.logger.info("*************** Configure_Check_passed ******************")
            print("Configure_check_test_is_passed")

            # checks Job_submission click
            self.bc.job_submission()
            time.sleep(2)
            job_sub = self.driver.current_url
            if "job_submission" in job_sub:
                self.logger.info("*************** Job_submission_Configure_Check_passed ******************")
                print("Job_submission Configure_check_test_is_passed")
                configure_results["job_submission"] = "Pass"
            else:
                self.logger.info("*************** Job_submission_Configure_Check_passed ******************")
                print("Job_submission Configure_check_test_is_failed")
                configure_results["job_submission"] = "Fail"

                # checks Job_management click
            self.bc.job_management()
            time.sleep(2)
            job_mag = self.driver.current_url
            if "job_management" in job_mag:
                self.logger.info("*************** Job_management_Configure_Check_passed ******************")
                print("Job_management Configure_check_test_is_passed")
                configure_results["job_management"] = "Pass"
            else:
                self.logger.info("*************** Job_management_Configure_Check_passed ******************")
                print("Job_submission Configure_check_test_is_failed")
                configure_results["job_management"] = "Fail"
                #self.driver.close()

            # checks network click
            self.bc.network()
            time.sleep(2)
            net = self.driver.current_url
            if "network" in net:
                self.logger.info("*************** network_Configure_Check_passed ******************")
                print("network Configure_check_test_is_passed")
                configure_results["network"] = "Pass"
            else:
                self.logger.info("*************** network_Configure_Check_passed ******************")
                print("network Configure_check_test_is_failed")
                configure_results["network"] = "Fail"
                #self.driver.close()


            # checks security click
            self.bc.security()
            time.sleep(2)
            security = self.driver.current_url
            if "security" in security:
                self.logger.info("*************** security_Configure_Check_passed ******************")
                print("security configure_check_test_is_passed")
                configure_results["security"] = "Pass"
            else:
                self.logger.info("*************** security_Configure_Check_passed ******************")
                print("security Configure_check_test_is_failed")
                configure_results["security"] = "Fail"
                #self.driver.close()

            # checks rip click
            self.bc.rip()
            time.sleep(2)
            rip = self.driver.current_url
            if "rip" in rip:
                self.logger.info("*************** Rip_Configure_Check_passed ******************")
                print("Rip configure_check_test_is_passed")
                configure_results["rip"] = "Pass"
            else:
                self.logger.info("*************** Rip_Configure_Check_passed ******************")
                print("Rip Configure_check_test_is_failed")
                configure_results["rip"] = "Fail"
                #self.driver.close()

            # checks scan click
            self.bc.scan()
            time.sleep(2)
            scan = self.driver.current_url
            if "scan" in scan:
                self.logger.info("*************** Scan_Configure_Check_passed ******************")
                print("Scan configure_check_test_is_passed")
                configure_results["scan"] = "Pass"
            else:
                self.logger.info("*************** Scan_Configure_Check_passed ******************")
                print("Scan Configure_check_test_is_failed")
                configure_results["scan"] = "Fail"
                #self.driver.close()

            # checks scan click
            self.bc.user_acc()
            time.sleep(2)
            user_acc = self.driver.current_url
            if "user_accounts" in user_acc:
                self.logger.info("*************** User_account_Configure_Check_passed ******************")
                print("User_account configure_check_test_is_passed")
                configure_results["user_acc"] = "Pass"
            else:
                self.logger.info("*************** User_account_Configure_Check_passed ******************")
                print("User_account Configure_check_test_is_failed")
                configure_results["user_acc"] = "Fail"
                #self.driver.close()

            # Check fiery server click
            self.bc.fiery_server()
            time.sleep(2)
            fiery = self.driver.current_url
            if "fiery_server" in fiery:
                self.logger.info("*************** Fiery_Configure_Check_passed ******************")
                print("Fiery Configure_check_test_is_passed")
                configure_results["Fiery_check"] = "Pass"
            else:
                self.logger.info("*************** Job_submission_Configure_Check_passed ******************")
                print("Job_submission Configure_check_test_is_failed")
                configure_results["Fiery_check"] = "Fail"

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

        failed_checks = {key: value for key, value in configure_results.items() if value == "Fail"}
        if "Fail" in configure_results.values():
            self.logger.info("*************** configure-page clicks is failed ******************")
            self.logger.info(f"Failed checks: {failed_checks.keys()}")
            print("Configure_Page_clicks_test_is_failed")
            print("Failed checks:", list(failed_checks.keys()))
            self.driver.close()
            print("Configure_check results are: ", configure_results)
            assert False
        else:
            self.logger.info("*************** configure-page clicks is passed ******************")
            print("Configure_Page_clicks_test_is_passed")
            self.driver.close()
            print("Configure_check results are: ", configure_results)
            assert True

    # Test-Case to test web-tools home page
    def test_button_function_webtools(self, setup):
        self.logger.info("*************** Test_Webtools_homepage_functions ******************")
        self.logger.info("*************** Verify_Webtools_homepage_functionality ******************")
        Home_title = "WebTools"
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed()
        current_title = self.driver.title
        if current_title == Home_title:
            self.logger.info("*************** Webtools_Homepage_Check_passed ******************")
            print("Webtools_Homepage_check_test_is_passed")
            self.driver.close()
            assert True
        elif current_title != Home_title:
            self.logger.info("*************** Webtools_Homepage_Check_failed ******************")
            print("Webtools_Homepage_check_test_is_failed")
            self.driver.close()
            assert False
        else:
            self.logger.info("*************** Problem in searching element on the page ******************")
            print("Problem in searching element on the page")
            self.driver.close()
            assert False

    # Test-Case to test web-tools FSR page
    def test_button_function_webtools_FSR(self, setup):
        self.logger.info("*************** Test_FSR_homepage_functions ******************")
        self.logger.info("*************** Verify_FSR_homepage_functionality ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed()
        self.bc.Fsr()
        current_title = self.driver.current_url
        if "brhome?" in current_title:
            self.logger.info("*************** Webtools_FSR_Homepage_Check_passed ******************")
            print("Webtools_FSR_Homepage_check_test_is_passed")
            self.driver.close()
            assert True
        elif "brhome?" not in current_title:
            self.logger.info("*************** Webtools_FSR_Homepage_Check_failed ******************")
            print("Webtools_FSR_Homepage_check_test_is_failed")
            self.driver.close()
            assert False
        else:
            self.logger.info("*************** Problem in searching element on the page ******************")
            print("Problem in searching element on the page")
            self.driver.close()
            assert False


    # Test case for Docs login
    def test_docs_login(self, setup):
        self.logger.info("*************** Test_Docs_login_functions ******************")
        self.logger.info("*************** Verify_Docs_login_functionality ******************")
        Docs_title = "WebTools | My Docs"
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
            self.bc.docs_button()
            self.lp = Login(self.driver)
            self.lp.set_docs_username(self.username)
            self.lp.set_docs_password(self.password)

            # check Docs login button functionality
            self.bc.docs_login_button()
            time.sleep(5)
            docs_title = self.driver.current_url
            if "mydocs" in docs_title:
                self.logger.info("*************** Docs_login_sucessful ******************")
                print("Docs login sucessful")
            else:
                self.logger.info("*************** Docs_login_failed ******************")
                print("Docs login failed")
                self.driver.close()
                assert False

            # check Docs printed button functionality
            self.bc.docs_printed()
            docs_print_title = self.driver.current_url
            if "printed" in docs_print_title:
                self.logger.info("*************** Printed_Docs_check_sucessful ******************")
                print("Printed_Docs_check_sucessful")
            else:
                self.logger.info("*************** Printed_Docs_check_failed ******************")
                print("Printed_Docs_check_failed")
                self.driver.close()
                assert False

            # check Docs held button functionality
            self.bc.docs_held()
            docs_held_title = self.driver.current_url
            if "held" in docs_held_title:
                self.logger.info("*************** Held_Docs_check_sucessful ******************")
                print("Held_Docs_check_sucessful")
            else:
                self.logger.info("*************** Held_Docs_check_failed ******************")
                print("Held_Docs_check_failed")
                self.driver.close()
                assert False

            message = self.bc.docs_logout()
            time.sleep(5)
            print("Message is: ", message)
            if message is None:
                self.logger.info("*************** Docs_logout_sucessful ******************")
                print("Docs_logout_sucessful")
                self.driver.close()
                assert True
            else:
                self.logger.info("*************** Docs_logout_failed ******************")
                print("Docs_logut_failed")
                self.driver.close()
                assert False

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

    #Test case to check home page manage clicks
    def test_Manage_page(self, setup):
        self.logger.info("*************** Home_Page_click_functions ******************")
        self.logger.info("*************** Home_Page_click_functionality ******************")
        Home_page_title = "WebTools"
        manage_title = "Manage Fiery Options"
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed() # It will point to home page
        current_title = self.driver.title
        if current_title == Home_page_title:
            self.logger.info("*************** Home_Page_click_passed ******************")
            print("Home_Page_click_test_is_passed")
            self.bc.Manage()
            time.sleep(5)
            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[-1])
            windows_title = self.driver.title
            if windows_title == manage_title:
                self.logger.info("*************** Manage_button_click_passed ******************")
                print("Manage page got launched sucessfully")
                self.driver.close()
                assert True
            elif windows_title != manage_title:
                self.logger.info("*************** Manage_button_click_failed ******************")
                print("Manage page got launched failed")
                self.driver.close()
                assert False

    # Test case to check fiery icon click on home page
    def test_Home_fiery_icon(self, setup):
        self.logger.info("*************** Home_Page_click_functions ******************")
        self.logger.info("*************** Home_Page_click_functionality ******************")
        Home_page_title = "WebTools"
        Fiery_Icon_title = "Fiery - Digital Print Servers (DFEs) and Workflow Solutions"
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed() # It will point to home page
        current_title = self.driver.title
        if current_title == Home_page_title:
            self.logger.info("*************** Home_Page_click_passed ******************")
            print("Home_Page_click_test_is_passed")
            self.bc.Fiery_icon()
            time.sleep(5)
            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[-1])
            windows_title = self.driver.title
            if windows_title == Fiery_Icon_title:
                self.logger.info("*************** Fiery_Icon_click_passed ******************")
                print("Fiery_Icon page got launched sucessfully")
                self.driver.close()
                assert True
            elif windows_title != Fiery_Icon_title:
                self.logger.info("*************** Fiery_Icon_click_failed ******************")
                print("Fiery_Icon page got launched failed")
                self.driver.close()
                assert False

    # Test case to check fiery icon click on home page
    def test_check_updates(self, setup):
        self.logger.info("*************** Home_Page_click_functions ******************")
        self.logger.info("*************** Home_Page_click_functionality ******************")
        Home_page_title = "WebTools"
        check_updates = "Fiery WebUpdater"
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed() # It will point to home page
        time.sleep(2)
        current_title = self.driver.title
        if current_title == Home_page_title:
            self.logger.info("*************** Home_Page_click_passed ******************")
            print("Home_Page_click_test_is_passed")
            self.bc.check_updates()
            time.sleep(5)
            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[-1])
            windows_title = self.driver.title
            if windows_title == check_updates:
                self.logger.info("*************** check_for_updates_click_passed ******************")
                print("check_for_updates got launched sucessfully")
                self.driver.close()
                assert True
            elif windows_title != check_updates:
                self.logger.info("*************** check_for_updates_click_failed ******************")
                print("check_for_updates got launched failed")
                self.driver.close()
                assert False











