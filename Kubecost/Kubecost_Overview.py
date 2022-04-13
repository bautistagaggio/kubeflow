from POM.config import TestData
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.BasePage import BasePage
from pyshadow.main import Shadow


"""
/**
 ?  -----------------------THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN KUBECOST OVERVIEW PAGE --------------------------------------------------        
*/"""


class KubecostOverview(BasePage):
                                          
       

 ##################################################################   OBJECT SELECTORS   ####################################################################

    CostAllocation = (By.XPATH, "(//div[@id='detail-nav'])[1]")
    
 ##################################################################   OBJECT SELECTORS   #################################################################### 

    def GoToCostAllocation(self):
        self.do_click(self.CostAllocation)
