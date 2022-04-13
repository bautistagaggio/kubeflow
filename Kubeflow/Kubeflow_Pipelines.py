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


class KubeflowPipelines(BasePage):

##################################################################   OBJECT SELECTORS   ####################################################################

    Artifacts = "(//button[@class='jss35 jss9 jss11 jss14 button_f17w3f2d'])[2]"
    UploadPipeline = "//button[@id='createPipelineVersionBtn']"
    Pipeline_Description = "//input[@id='pipelineDescription']"                    

##################################################################   OBJECT SELECTORS   ####################################################################

    
    def GotoPipelines(self):
        self.do_shadow_click(KubeflowHome.Pipelines)
        frame = self.find_shadow_element(KubeflowHome.Iframe)
        self.frame_switch(frame)

    def GoToArtifacts(self):
        self.GotoPipelines()
        self.do_jsclick(self.Artifacts)
    
    def PipelineUpload(self):
        self.GotoPipelines()
        self.do_jsclick(self.UploadPipeline)
        self.do_shadow_send_keys(self.Pipeline_Description,)

        
        
        

    
