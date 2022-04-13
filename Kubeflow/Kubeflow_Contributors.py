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


class KubeflowContributors(BasePage):

    def GoToContributors(self):
        self.do_shadow_click(KubeflowHome.ManageContributors)
        frame = self.find_shadow_element(KubeflowHome.Iframe)
        self.frame_switch(frame)