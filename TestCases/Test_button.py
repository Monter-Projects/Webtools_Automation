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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_001_button_checks:
    baseurl = readconfig.getappurl()
    username = readconfig.get_webtoolsusername()
    password = readconfig.get_webtoolspassword()
    logger = LogGen.loggen()

    # common function which launches web-tools main-page
    def home_page_launch(self, setup, configure):
        self.logger.info("*************** Product_update_click_functions ******************")
        self.logger.info("*************** Product_update_click_functionality ******************")
        Home_page_title = "WebTools"
        check_updates = "Fiery WebUpdater"
        self.driver = setup
        self.driver.get(self.baseurl)
        self.bc = Button_checks(self.driver)
        self.bc.Advanced()
        self.bc.Proceed()  # It will point to home page
        time.sleep(2)
        current_title = self.driver.title
        if current_title == Home_page_title:
            self.logger.info("*************** Home_Page_click_passed ******************")
            print("Home_Page_click_test_is_passed")
            if configure == 1:
                self.bc.Configure()  # clicking the configure button
                self.lp = Login(self.driver)
                self.lp.set_webtools_username(self.username)
                self.lp.set_webtools_password(self.password)
                self.bc.login()
            elif configure == 0:
                pass

        else:
            self.logger.info("*************** Home_Page_click_passed ******************")
            print("Home_Page_click_test_is_failed")
            self.driver.close()
            assert False

    def outside_click(self):
        outside_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "body")))
        actions = ActionChains(self.driver)
        actions.move_to_element(outside_element).click().perform()


    # Test-Case-1
    # Test-Case to test Docs link
    def test_button_function_docs(self, setup):
        self.home_page_launch(setup,configure=0)
        Docs_title = "WebTools | My Docs"
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
        self.driver.quit()

    # Test-Case-2
    # Test-case to test configure function
    def test_button_function_configure(self, setup):
        self.home_page_launch(setup,configure=1)
        Configure_title = "Configure"
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
        self.driver.quit()

    # Test-Case-3
    # Test-Case to test web-tools home page
    def test_button_function_webtools(self, setup):
        self.home_page_launch(setup,configure=0)
        Home_title = "WebTools"
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
        self.driver.quit()

    # Test-Case-4
    # Test-Case to test web-tools FSR page
    def test_button_function_webtools_FSR(self, setup):
        self.home_page_launch(setup,configure=0)
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
        self.driver.quit()

    #Test-case-5
    # Test case for Docs login
    def test_docs_login(self, setup):
        self.home_page_launch(setup,configure=0)
        self.bc.Docs() # clicking the about button
        Docs_title = "WebTools | My Docs"
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
        self.driver.quit()

    #Test-case-6
    #Test case to check home page manage clicks
    def test_Manage_page(self, setup):
        self.home_page_launch(setup,configure=0)
        self.bc.Manage()
        manage_title = "Manage Fiery Options"
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
        self.driver.quit()

    #Test-Case-7
    # Test case to check fiery icon click on home page
    def test_Home_fiery_icon(self, setup):
        self.home_page_launch(setup,configure=0)
        Fiery_Icon_title = "Fiery - Digital Print Servers (DFEs) and Workflow Solutions"
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
        self.driver.quit()

    # Test-Case-8
    # Test case to check_for_updates link click on home page
    def test_check_updates(self, setup):
        self.home_page_launch(setup,configure=0)
        check_updates = "Fiery WebUpdater"
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
        self.driver.quit()

    # Test-Case-9
    # Test case to check fiery license agreement link on home page
    def test_check_eula(self, setup):
        self.home_page_launch(setup,configure=0)
        self.bc.Fiery_license()
        self.bc.Fiery_eula()
        time.sleep(5)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        current_url = self.driver.current_url
        if "efieula.html" in current_url:
            self.logger.info("*************** efieula_click_passed ******************")
            print("efieula got launched sucessfully")
            self.driver.close()
        elif "efieula.html" not in current_url:
            self.logger.info("*************** efieula_click_failed ******************")
            print("efieula got launch failed")
            self.driver.close()
            assert False
        self.driver.switch_to.window(window_handles[0])
        self.bc.Fiery_license()
        self.bc.open_source_license()
        time.sleep(5)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        current_url_1 = self.driver.current_url
        if "osnotices.html" in current_url_1:
            self.logger.info("*************** osnotices_click_passed ******************")
            print("osnotices got launched sucessfully")
            self.driver.close()
            assert True
        elif "osnotices.html" not in current_url_1:
            self.logger.info("*************** osnotices_click_failed ******************")
            print("osnotices got launch failed")
            self.driver.close()
            assert False
        self.driver.quit()

    # Test-Case-10
    # Test case to check Fiery_System_image(FSR)
    def test_FSR_FSI_function(self, setup):
        self.home_page_launch(setup,configure=0)
        self.bc.Fsr()
        current_title = self.driver.current_url
        if "brhome?" in current_title:
            self.logger.info("*************** Webtools_FSR_Homepage_Check_passed ******************")
            print("Webtools_FSR_Homepage_check_test_is_passed")
            self.bc.br()
            fsr_url = self.driver.current_url
            if "wt4/fsr" in fsr_url:
                self.logger.info("*************** Webtools_FSR_Click_Check_passed ******************")
                print("Webtools_FSR_click_check_test_is_passed")
                self.driver.close()
                assert True
            elif "wt4/fsr" not in fsr_url:
                self.logger.info("*************** Webtools_FSR_Click_Check_failed ******************")
                print("Webtools_FSR_click_check_test_is_failed")
                self.driver.close()
                assert False
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
        self.driver.quit()

    # Test-Case-11
    # Test case to check Fiery_System_image(FSR)
    def test_FSR_Resource_function(self, setup):
        self.home_page_launch(setup,configure=0)
        self.bc.Fsr()
        current_title = self.driver.current_url
        if "brhome?" in current_title:
            self.logger.info("*************** Webtools_FSR_Homepage_Check_passed ******************")
            print("Webtools_FSR_Homepage_check_test_is_passed")
            self.bc.resourceSettings()
            fsr_url = self.driver.current_url
            if "wt4/br" in fsr_url:
                self.logger.info("*************** Webtools_FSR_resource_settings_Click_Check_passed ******************")
                print("Webtools_FSR_click_check_test_is_passed")
                self.driver.close()
                assert True
            elif "wt4/br" not in fsr_url:
                self.logger.info("*************** Webtools_FSR_resource_settings_Click_Check_failed ******************")
                print("Webtools_FSR_click_check_test_is_failed")
                self.driver.close()
                assert False
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
        self.driver.quit()


    def test_Fiery_Server_function_configure(self, setup):
        self.home_page_launch(setup,configure=1)
        Configure_title = "Configure"
        current_title = self.driver.title
        #configure_results = []
        configure_option_results = {"Server_name": "Pass", "IPv4_address": "Pass", "IPv6_address": "Pass",
                            "Regional Settings": "Pass", "Use Character Set": "Pass", "Print Start Page": "Pass", "System Updates": "Pass",
                                    "System Logs":"Pass", "Job-log" : "Pass", "Fiery Support Contact Information" : "Pass",
                                    "Printer Support Contact Information" : "Pass", "Backup":"Pass", "Restore":"Pass", "Restore_default": "Pass"}
        golden_configure_option_text = {"Server_name": "Server information", "IPv4_address": "IPv4 Address", "IPv6_address": "IPv6 Address",
                            "Regional Settings": "Regional Settings", "Use Character Set": "Use Character Set", "Print Start Page": "Print Start Page", "System Updates": "System Updates"}
                                    #"System Logs": "System Logs", "Job-log" : "Job Log", "Fiery Support Contact Information" : "Fiery Support Contact Information",
                                    #"Printer Support Contact Information" : "Printer Support Contact Information", "Backup":"Backup", "Restore":"Restore", "Restore Default Fiery Settings": "Restore Default Fiery Settings"}
        configure_option_text = {"Server_name": "", "IPv4_address": "", "IPv6_address": "",
                            "Regional Settings": "", "Use Character Set": "", "Print Start Page": "", "System Updates": ""}
                                    #"System Logs": "", "Job-log" : "", "Fiery Support Contact Information" : "",
                                    #"Printer Support Contact Information" : "", "Backup":"", "Restore":"", "Restore Default Fiery Settings": ""}
        if current_title == Configure_title:
            self.logger.info("*************** Configure_Check_passed ******************")
            print("Configure_check_test_is_passed")
            self.driver.maximize_window()

            # Fiery server option check
            self.bc.Fiery_server_name()
            Server_name_text = self.bc.Fiery_server_configure()
            configure_option_text["Server_name"]= Server_name_text
            self.outside_click()
            time.sleep(2)
            #ipv4 option check
            self.bc.ipv4()
            ipv4_name_text = self.bc.ipv4_text()
            configure_option_text["IPv4_address"] = ipv4_name_text
            self.outside_click()
            time.sleep(2)
            #ipv6 option check
            self.bc.ipv6()
            ipv6_name_text = self.bc.ipv6_text()
            configure_option_text["IPv6_address"] = ipv6_name_text
            self.outside_click()
            time.sleep(2)
            #regional option check
            self.bc.regional()
            regional_name_text = self.bc.regional_text()
            configure_option_text["Regional Settings"] = regional_name_text
            self.outside_click()
            time.sleep(2)
            #character option check
            self.bc.character()
            character_name_text = self.bc.character_text()
            configure_option_text["Use Character Set"] = character_name_text
            self.outside_click()
            time.sleep(2)
            #print start option check
            self.bc.print_start()
            print_start_text = self.bc.print_start_text()
            configure_option_text["Print Start Page"] = print_start_text
            self.outside_click()
            time.sleep(2)
            #system-update option check
            self.bc.system_update()
            system_update_text = self.bc.system_update_text()
            configure_option_text["System Updates"] = system_update_text
            self.outside_click()
            time.sleep(2)
            if golden_configure_option_text == configure_option_text:
                self.logger.info("*************** Fiery_Configure_Server_Click_Check_passed ******************")
                print("Fiery_Configure_Server_Click_check_test_is_passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("*************** Fiery_Configure_Server_Click_Check_Failed ******************")
                print("Fiery_Configure_Server_Click_check_test_is_Failed")
                self.driver.close()
                assert False


    def test_ipv4_function_configure(self, setup):
        self.home_page_launch(setup, configure=1)
        Configure_title = "Configure"
        current_title = self.driver.title
        golden_configure_option_text = {"System Logs": "System Logs", "Job-log" : "Job Log", "Fiery Support Contact Information" : "Fiery Support Contact Information",
                                        "Printer Support Contact Information" : "Printer Support Contact Information", "Backup":"Backup", "Restore":"Restore", "Restore Default Fiery Settings": "Restore Default Fiery Settings"}
        configure_option_text = {"System Logs": "", "Job-log" : "", "Fiery Support Contact Information" : "",
                                 "Printer Support Contact Information" : "", "Backup":"", "Restore":"", "Restore Default Fiery Settings": ""}
        if current_title == Configure_title:
            self.logger.info("*************** Configure_Check_passed ******************")
            print("Configure_check_test_is_passed")
            self.driver.maximize_window()

            time.sleep(2)
            # system logs option check
            self.bc.system_logs()
            system_log_text = self.bc.system_logs_text()
            configure_option_text["System Logs"] = system_log_text
            self.outside_click()
            time.sleep(2)
            # job logs option check
            self.bc.jobs_logs()
            jobs_logs_text = self.bc.jobs_logs_text()
            configure_option_text["Job-log"] = jobs_logs_text
            self.outside_click()
            time.sleep(2)
            # fiery support option check
            self.bc.fiery_support()
            fiery_support_text = self.bc.fiery_support_text()
            configure_option_text["Fiery Support Contact Information"] = fiery_support_text
            self.outside_click()
            time.sleep(2)
            # print support option check
            self.bc.print_support()
            print_support_text = self.bc.print_support_text()
            configure_option_text["Printer Support Contact Information"] = print_support_text
            self.outside_click()
            time.sleep(2)
            # backup option check
            self.bc.backup()
            backup_text = self.bc.backup_text()
            configure_option_text["Backup"] = backup_text
            self.outside_click()
            time.sleep(2)
            #link restore option check
            self.bc.link_restore()
            link_restore_text = self.bc.link_restore_text()
            configure_option_text["Restore"] = link_restore_text
            self.outside_click()
            time.sleep(2)
            #restore default option check
            self.bc.restore_default()
            restore_default_text = self.bc.restore_default_text()
            configure_option_text["Restore Default Fiery Settings"] = restore_default_text
            self.outside_click()
            time.sleep(2)
            if golden_configure_option_text == configure_option_text:
                self.logger.info("*************** Fiery_Configure_Server_Click_Check_passed ******************")
                print("Fiery_Configure_Server_Click_check_test_is_passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("*************** Fiery_Configure_Server_Click_Check_Failed ******************")
                print("Fiery_Configure_Server_Click_check_test_is_Failed")
                self.driver.close()
                assert False










            

            


























