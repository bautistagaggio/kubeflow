

from POM.config import TestData
from POM.BasePage import BasePage
from selenium.webdriver.common.by import By
from conftest import api_token_init
import pytest

"""
/**
 ?                          THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN KUBEFLOW LOGIN PAGE     
*/"""

class KubeflowLogin(BasePage):

   ##################################################################   OBJECT SELECTORS   #################################################################### 

    __LogInWithEmail = (By.XPATH, "(//span[@class='dex-btn-text'])[1]")
    __Email = (By.XPATH, "(//input[@class='theme-form-input'])[1]")
    __Password = (By.XPATH, "(//input[@class='theme-form-input'])[2]")
    __Login =  (By.XPATH, "//button[@class='dex-btn theme-btn--primary']")


   ##################################################################   OBJECT SELECTORS   ####################################################################


    # ACTIONS

    def __init__(self, driver, apiHost):
        super().__init__(driver)                                        # calls the parent class constructor
        self.driver.get(apiHost)
        #self.driver.maximize_window()
   
    def do_login(self, email, password):
        self.do_click(self.__LogInWithEmail)
        self.do_send_keys(self.__Email, email)
        self.do_send_keys(self.__Password, password)
        self.do_click(self.__Login)




        


        


