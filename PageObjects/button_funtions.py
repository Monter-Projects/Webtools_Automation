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
    Docs_id = "Combined-Shape"
    Configure_id = "id-configure-tab"
    Fsr_id = "id-fiery-backup-restore-tab"
    Home_xpath = "//*[@id='id-home-tab']/svg"
    Advanced_xpath = "//*[@id='details-button']"
    Proceed_xpath = "//*[@id='proceed-link']"
    Login_id = "loginBtn"
    # actiont to start driver
    def __init__(self,driver):
        self.driver = driver

    def Proceed(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Proceed_xpath)))
        element.click()

    def Advanced(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Advanced_xpath)))
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

    '''
    # action for read_case button
    def read_case(self):
        self.driver.find_element(By.XPATH, self.read_case_study_xpath).click()

    # action for read_case1 button
    def read_case1(self):
        self.driver.find_element(By.XPATH, self.read_case_study1_xpath).click()

    # action for signup button
    def signup(self):
        self.driver.find_element(By.XPATH, self.sign_up_xpath).click()

    # action for last_request button
    def last_request(self):
        self.driver.find_element(By.XPATH, self.last_request_demo_xpath).click()
'''





#About_Tiltle = "CrazyEgg Tracking iframe"
#request_demo_url = "https://saucelabs.com/request-demo"
#test_for_free = "https://saucelabs.com/sign-up"
#learn more = "https://saucelabs.com/products"
#case_study1 = "https://saucelabs.com/resources/case-studies/verizon-media-accelerates-millions-of-tests-every-month-using-open-source-technology-and-sauce-labs"
#case_study2 = "https://saucelabs.com/resources/case-studies/walmart-embraces-test-automation-and-open-source-to-increase-coverage-and-deploy-more-often"
#sign_up_path = "https://saucelabs.com/sign-up"
#last_request_demo_xpath = "https://saucelabs.com/request-demo"


