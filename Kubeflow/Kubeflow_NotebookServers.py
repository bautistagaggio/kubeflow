from POM.JupyterHub import JupyterHub
from POM.Kubeflow.Kubeflow_Home import KubeflowHome
from POM.config import TestData
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.BasePage import BasePage
from pyshadow.main import Shadow
import time
import pytest

"""
/**
 ?                          THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN THE NOTEBOOK SERVERS PAGE     
*/"""


class KubeflowNotebookServers(BasePage):

##################################################################   OBJECT SELECTORS   ####################################################################

    
    CustomImage = "#mat-checkbox-4 > label" 
    ServerName = "#mat-input-0"   
    CreateServer = "//button[@class='ng-tns-c5-0 mat-stroked-button mat-button-base mat-accent']"
    No_Workspace_Volume ="(//input[@class='mat-checkbox-input cdk-visually-hidden'])[2]"
    GPUs = "#mat-select-0"
    Shared_Memory = "#mat-slide-toggle-1-input"
    Dismiss = "//button[@class='mat-button mat-button-base mat-accent']"
    Launch = "//button[@class='margin mat-raised-button mat-button-base mat-accent']"
    # Connect = f"((//td[starts-with(@class, 'mat-cell cdk-column-name mat-column-name')] [contains(text(), '{NotebookName}')]/following-sibling::td)[3]/descendant::button)[1]"
    Cancel = "//button[@class='margin mat-raised-button mat-button-base']"
    Delete = "(//button[starts-with(@class, 'mat-menu-item delete')])[last()]"
    # NotebookOptions = f"((//td[starts-with(@class, 'mat-cell cdk-column-name mat-column-name')] [contains(text(), '{NotebookName}')]/following-sibling::td)[3]/descendant::button)[1]/following-sibling::button"
    DeleteConfirmation = "//button[@class='mat-raised-button mat-button-base red']"
    
                    
##################################################################   OBJECT SELECTORS   ####################################################################


    def __init__(self, driver):
        super().__init__(driver)


        

    def CreateNotebookServer(self):

        self.do_shadow_click(KubeflowHome.NotebookServers)
        frame = self.find_shadow_element(KubeflowHome.Iframe)
        self.frame_switch(frame)
        self.do_jsclick(self.CreateServer)
        NotebookName = TestData.ServerName
        self.do_shadow_send_keys(self.ServerName, NotebookName)
        self.do_jsclick(self.No_Workspace_Volume)
        self.scroll_bottom()
        self.do_jsclick(self.Dismiss)
        time.sleep(0.5)                         
        self.do_jsclick(self.Launch)
        time.sleep(1.5)
        self.scroll_bottom()
        time.sleep(14)
        return NotebookName


    def LaunchNotebook(self,NotebookName):
        self.do_jsclick(self.GetNotebookConnectSelector(NotebookName))   # selector generated at run time, based on an alleatory string generated on TestData.ServerName
        self.do_switch_to(1)
        
    
    # def UseExistingNotebook(self):
    #     self.do_shadow_click(KubeflowHome.NotebookServers)
    #     frame = self.find_shadow_element(KubeflowHome.Iframe)
    #     self.frame_switch(frame)
    #     time.sleep(2)
    #     self.do_jsclick(self.Connect)
    #     self.do_switch_to(1)
        

    def DeleteNotebookServer(self, NotebookName):

        self.do_switch_to(0)   # return to notebooks page
        frame = self.find_shadow_element(KubeflowHome.Iframe)
        self.frame_switch(frame)
        time.sleep(1)
        self.scroll_bottom()
        self.do_jsclick(self.GetNotebookOptionsSelector(NotebookName))
        self.do_jsclick(self.Delete)
        self.do_jsclick(self.DeleteConfirmation)
        time.sleep(3)

    # passes the randomly generated NotebookName at runtime and creates the button's selectors
    def GetNotebookConnectSelector(self, NotebookName):
        connect = f"((//td[starts-with(@class, 'mat-cell cdk-column-name mat-column-name')] [contains(text(), '{NotebookName}')]/following-sibling::td)[3]/descendant::button)[1]"
        return connect
        
    def GetNotebookOptionsSelector(self, NotebookName):
        options = f"((//td[starts-with(@class, 'mat-cell cdk-column-name mat-column-name')] [contains(text(), '{NotebookName}')]/following-sibling::td)[3]/descendant::button)[1]/following-sibling::button"
        return options

    
    

        
         
