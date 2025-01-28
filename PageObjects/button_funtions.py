from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
    # actiont to start driver
    def __init__(self,driver):
        self.driver = driver

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









