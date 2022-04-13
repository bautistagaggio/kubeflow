from POM.config import TestData
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.BasePage import BasePage
from pyshadow.main import Shadow


"""
/**
 ?  -----------------------THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN KUBEFLOW HOME PAGE --------------------------------------------------        
*/"""


class KubeflowHome(BasePage):
   

    ###############################################   OBJECT SELECTORS   #########################################

    Menu = "#icon"
    NameSpace_Selection = "#dropdown-trigger"
    Home = "#MainDrawer > iron-selector > a.iron-selected > paper-item"
    Pipelines = "#MainDrawer > iron-selector > iframe-link:nth-child(2) > paper-item" 
    NotebookServers = "#MainDrawer > iron-selector > iframe-link:nth-child(3) > paper-item"
    ManageContributors = "#MainDrawer > iron-selector > a:nth-child(9) > paper-item"  
    Iframe = "#iframe"
    Pipelines_Details = "#root > div > div > div.page_f1flacxk > div.flex_f16jawj4.banner_forn49x.mode_fo01qrq > div.flex_f16jawj4 > button.jss35.jss9.jss11.jss14.button_fu86r2b.detailsButton_fgq2mjo"
    Pipelines_Upload = "#createPipelineVersionBtn"
    Pipelines_Experiments = "#experimentsBtn"
    LogOut = "#User-Badge > a > iron-icon"
    
    ###############################################   OBJECT SELECTORS   #########################################
        
   
    
         

        
        
        
        

        
        

       

       

    
        

    
        
   
   

  