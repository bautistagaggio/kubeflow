import time
from POM.config import TestData
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.BasePage import BasePage
from pyshadow.main import Shadow


"""
/**
 ?  -----------------------THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN KUBECOST HOME PAGE --------------------------------------------------        
*/"""


class KubecostLogin(BasePage):
   
    def __init__(self, driver, KubecostHost):
        super().__init__(driver)                                        # calls the parent class constructor
        self.driver.get(KubecostHost)
        self.driver.maximize_window()

 ##################################################################   OBJECT SELECTORS   ####################################################################

    STG_Cluster = (By.XPATH, "//div[@id='cluster-row0']")
    Email = (By.XPATH, "//input[@id='initEmail']")    
    Next = (By.XPATH, "//button[@class='a-btn a-btn-primary a-btn-xl']")

 ##################################################################   OBJECT SELECTORS   ####################################################################

    def do_login(self):
        self.do_send_keys(self.Email, TestData.Email)
        self.do_click(self.Next)
        time.sleep(1.5)
        # pyautogui.press('enter')

    def select_cluster(self):
        self.do_click(self.STG_Cluster)

        # source control
        