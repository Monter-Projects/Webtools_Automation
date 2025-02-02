from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")  # Ensure a full-screen size
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model



class Button_checks:
    '''
    about_xpath = "//*[@id='about_sidebar_link']"
    request_demo_xpath = "//*[@id='__next']/div[3]/div[1]/div/div/div[1]/div/div[4]/div[2]/a/button[2]"
    try_it_free_xpath = "//*[@id='__next']/div[3]/div[1]/div/div/div[1]/div/div[4]/div[1]/a/button"
    learn_more_xpath = "//*[@id='__next']/div[6]/div/div[3]/a/button"
    read_case_study_xpath = "//*[@id='__next']/div[7]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[3]/a/button[2]"
    read_case_study1_xpath = "//*[@id='__next']/div[7]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[3]/a/button[2]"
    sign_up_xpath = "//*[@id='__next']/div[8]/div/div/div[2]/a[1]/button"
    last_request_demo_xpath = "//*[@id='__next']/div[8]/div/div/div[2]/a[2]/button"
    '''

    #Docs_xpath = "//*[@id='id-docs-tab']/svg"
    # Webtools mainpage clicks
    Docs_id = "Combined-Shape"
    Configure_id = "id-configure-tab"
    Fsr_id = "id-fiery-backup-restore-tab"
    Home_xpath = "//*[@id='id-home-tab']/svg"
    Advanced_xpath = "//*[@id='details-button']"
    Proceed_xpath = "//*[@id='proceed-link']"
    Login_id = "loginBtn"

    #configure clicks
    Job_submission_id = "tab_job_submission"
    Job_management_id = "tab_job_management"
    Job_network_id = "tab_network"
    Job_security_id = "tab_security"
    Job_rip_id = "tab_rip"
    Job_scan_id = "tab_scan"
    Job_user_acc_id = "tab_user_accounts"
    fiery_server_id = "tab_fiery_server"

    Docs_button_id = "id-login-btn"
    Docs_login_button_id = "id-docs-login-btn"
    Docs_printed_id = "id-printed-sub-tab"
    Docs_held_id = "id-held-sub-tab"
    Docs_logout_id = "id-docs-logout-link"
    Docs_logout_message_id = "id-docs-welcome-msg"

    Manage_button_id = "id-manage-launch-link"
    Fiery_icon_xpath = "//*[@id='id-header']/div/div[2]/a/img"
    check_for_updates_id = "id-check-for-update-link"
    Fiery_license_agree_id = "id-license-agreement-link"
    Fiery_eula_id = "id-efi-eula-link"
    open_source_license_agree_id = "id-efi-osla-link"
    backupRestore_id = "fsr"
    resourceSettings_id = "br"

    #configure Fiery-server options check
    Fiery_Server_option_xpath = "//*[@id='server_info_popup']/div[1]/h3"
    ipv4_xpath = "//*[@id='ip_address_popup_title']/h3"
    ipv6_xpath = "//*[@id='ipv6_address_popup']/div[1]/h3"
    regional_xpath  = "//*[@id='regional_settings_popup']/div[1]/h3"
    character_xpath = "//*[@id='use_character_set_popup']/div[1]/h3"
    print_start_xpath  = "//*[@id='help_title']/h3"
    system_update_xpath = "//*[@id='system_updates_popup']/div[1]/h3"
    system_logs_xpath = "//*[@id='system_logs_popup']/div[1]/h3"
    job_logs_xpath = "//*[@id='auto_joblog_popup']/div[1]/h3"
    fiery_support_xpath = "//*[@id='fiery_support_popup']/div[1]/h3"
    printer_support_xpath = "//*[@id='printer_support_popup']/div[1]/h3"
    backup_xpath = "//*[@id='backup_popup_title']/h3"
    restore_xpath = "//*[@id='restore_popup_title']/h3"
    restore_default_xpath = "//*[@id='restore_default_popup_title']/h3"
    cancel_xpath = "//*[@id='cancel']"
    restore_default_Xpath = "//*[@id='link_restore_default_fiery_settings']/h3"
    secure_erase_xpath = "//*[@id='link_server_secure_erase']/h3"
    fiery_true_brand_xpath = "//*[@id='id-truebrand-link']/img"
    secure_save_id = "ok"

    # All ID's
    cancel_id = "cancel"
    Fiery_server_name_id = "link_server_name"
    ipv4_id = "link_server_ip_address"
    ipv6_id = "link_server_ip_v6_enabled"
    regional_id = "link_server_locale"
    character_set_id = "link_server_use_character_set"
    print_start_id = "link_server_print_start_page"
    system_updates_id = "link_server_enable_system_updates"
    system_logs_id = "link_server_enable_system_log"
    job_log_id = "link_server_enable_joblog_auto_export"
    fiery_support_id = "link_server_support_fiery_contact_name"
    print_support_id = "link_server_support_printer_contact_name"
    backup_id = "link_backup"
    link_restore_id = "link_restore"
    #restore_default_id = "link_restore_default_fiery_settings"
    print_start_page_id = "server_print_start_page"
    restart_button_id = "link_restart_reboot"
    check_box_status = "server_print_start_page"
    secure_erase_checkbox_id = "server_secure_erase"
    true_brand_user_id = "inputUser"
    true_brand_pass_id = "inputPassword"
    true_login_button_id = "btnLogin"


    # actiont to start driver
    def __init__(self,driver):
        self.driver = driver

    def secure_save(self):
        # Handle overlays
        try:
            self.driver.execute_script("document.querySelector('.overlay-content, .modal, .popup').remove();")
        except:
            pass  # Ignore if there's no overlay

        # Check if inside an iframe
        try:
            iframe = self.driver.find_element(By.TAG_NAME, "iframe")
            self.driver.switch_to.frame(iframe)
        except:
            pass  # Ignore if no iframe

        # Wait for the button to be visible and clickable
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.secure_save_id)))

        # Scroll to the button
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Move to the button and click
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    '''
    def secure_save(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, "overlay-button")))
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, self.secure_save_id)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
    '''

    def secure_erase_checkbox(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "overlay-content scroller dirty")))
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.secure_erase_checkbox_id)))
        element.click()

    def true_band(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.fiery_true_brand_xpath)))
        element.click()

    def true_login_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.true_login_button_id)))
        element.click()

    def true_username(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.true_brand_user_id)))
        element.clear()
        element.send_keys("Admin")

    def true_password(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.true_brand_pass_id)))
        element.clear()
        element.send_keys("Fiery.1")

    def secure_erase(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.secure_erase_xpath)))
        element.click()

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")

    def checkbox(self):
        checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.print_start_page_id)))
        return checkbox

    def print_start_page(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.print_start_page_id)))
        element.click()

    def restart_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.restart_button_id)))
        element.click()

    def restore_default_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.restore_default_xpath)))
        text = element.text
        return text

    def restore_default(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.restore_default_Xpath)))
        element.click()

    def link_restore(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.link_restore_id)))
        element.click()

    def link_restore_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.restore_xpath)))
        text = element.text
        return text

    def backup(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.backup_id)))
        element.click()

    def backup_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.backup_xpath)))
        text = element.text
        return text

    def print_support(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.print_support_id)))
        element.click()

    def print_support_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.printer_support_xpath)))
        text = element.text
        return text



    def fiery_support(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.fiery_support_id)))
        element.click()

    def fiery_support_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.fiery_support_xpath)))
        text = element.text
        return text

    def jobs_logs(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.job_log_id)))
        element.click()

    def jobs_logs_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.job_logs_xpath)))
        text = element.text
        return text

    def system_logs(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.system_logs_id)))
        element.click()

    def system_logs_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.system_logs_xpath)))
        text = element.text
        return text


    def system_update(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.system_updates_id)))
        element.click()

    def system_update_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.system_update_xpath)))
        text = element.text
        return text

    def ipv4(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.ipv4_id)))
        element.click()

    def ipv4_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ipv4_xpath)))
        text = element.text
        return text

    ######################
    def ipv6(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.ipv6_id)))
        element.click()

    def ipv6_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ipv6_xpath)))
        text = element.text
        return text

    ####################
    def regional(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.regional_id)))
        element.click()

    def regional_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.regional_xpath)))
        text = element.text
        return text

    ###################
    def character(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.character_set_id)))
        element.click()

    def character_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.character_xpath)))
        text = element.text
        return text

    ###################
    def print_start(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.print_start_id)))
        element.click()

    def print_start_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.print_start_xpath)))
        text = element.text
        return text

    def system_update(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.system_updates_id)))
        element.click()

    def system_update_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.system_update_xpath)))
        text = element.text
        return text


    def Fiery_server_name(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Fiery_server_name_id)))
        element.click()

    def Cancel(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.cancel_xpath)))
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        element.click()

    def Fiery_server_configure(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Fiery_Server_option_xpath)))
        text = element.text
        return text

    def Proceed(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Proceed_xpath)))
        element.click()

    def Advanced(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Advanced_xpath)))
        element.click()

    def Manage(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Manage_button_id)))
        element.click()

    def Fiery_icon(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Fiery_icon_xpath)))
        element.click()

    def check_updates(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.check_for_updates_id)))
        element.click()

    def Fiery_license(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Fiery_license_agree_id)))
        element.click()

    def Fiery_eula(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Fiery_eula_id)))
        element.click()

    def open_source_license(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.open_source_license_agree_id)))
        element.click()

    def br(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.backupRestore_id)))
        element.click()

    def resourceSettings(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.resourceSettings_id)))
        element.click()

    # action for Docs button
    def Docs(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Docs_id)))
        element.click()
        #self.driver.find_element(By.XPATH, self.Docs_xpath).click()

    # action for configure button
    def Configure(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Configure_id)))
        element.click()

    def docs_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Docs_button_id)))
        element.click()

    def docs_login_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Docs_login_button_id)))
        element.click()

    def docs_printed(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Docs_printed_id)))
        element.click()


    def docs_held(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Docs_held_id)))
        element.click()

    def docs_logout(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Docs_logout_id)))
        element.click()

    def docs_logout_message(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Docs_logout_message_id)))
        message = element.text.strip()
        print("Logout message:", message)
        return message

    def fiery_server(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.fiery_server_id)))
        element.click()

    # action for Fsr button
    def Fsr(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Fsr_id)))
        element.click()

    def login(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Login_id)))
        element.click()

    # action for Home button
    def Homepage(self):
        self.driver.find_element(By.XPATH, self.Home_xpath).click()

    def job_submission(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Job_submission_id)))
        element.click()

    def job_management(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Job_management_id)))
        element.click()

    def network(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Job_network_id)))
        element.click()

    def security(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Job_security_id)))
        element.click()

    def rip(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Job_rip_id)))
        element.click()

    def scan(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Job_scan_id)))
        element.click()

    def user_acc(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.Job_user_acc_id)))
        element.click()









