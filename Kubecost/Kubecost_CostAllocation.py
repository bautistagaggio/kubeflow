import time
from dotenv.main import dotenv_values
from urllib3 import request
from POM.config import TestData
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.BasePage import BasePage
from pyshadow.main import Shadow


"""
/**
 ?  -----------------------THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN KUBECOST COST ALLOCATION PAGE --------------------------------------------------        
*/"""

@pytest.mark.usefixtures("api_token_init")
class KubecostCostAllocation(BasePage):
   
      ##################################################################   OBJECT SELECTORS   ####################################################################
        
   Breakdown = (By.XPATH, "//div[@id='aggregation-select']")
   ClusterOption = (By.XPATH, "(//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button'])[1]")
   AKS_Kubeflow = (By.XPATH, f"//td[contains(@class, 'MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft')] [contains(text(), '{TestData.clusters[1]}')]")
   Time_Sleep_object = (By.XPATH, "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft']")
   Cumulative_Cost = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5']")
   Namespaces_Kubeflow_QA = ("//td[@class = 'MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft']")
    
   

      ##################################################################   OBJECT SELECTORS   ####################################################################

   def SelectBreakdown(self):
      self.Wait_for_Existence(self.Time_Sleep_object)
      self.do_click(self.Breakdown)
      self.do_click(self.ClusterOption)

   def EnterClusters(self, cluster): 
      self.do_click(cluster)
      self.scroll_bottom() 

   def GetNamespaces(self):
      return self.get_elements_text(self.Namespaces_Kubeflow_QA) 
   
   def GetClusterSelector(self,index):
      return (By.XPATH, f"//td[contains(@class, 'MuiTableCell-root MuiTableCell-body MuiTableCell-alignLeft')] [text() = '{TestData.clusters[index]}']")

   def GetCumulativeTitle(self):
      return self.get_element_text(self.Cumulative_Cost) 

   def EnterCluster0(self):
      cluster = self.GetClusterSelector(0)
      self.EnterClusters(cluster)

   def EnterCluster1(self):
      self.go_previous_page(self.Time_Sleep_object)
      cluster = self.GetClusterSelector(1)
      self.EnterClusters(cluster)

   def EnterCluster2(self):
      self.go_previous_page(self.Time_Sleep_object)
      cluster = self.GetClusterSelector(2)
      self.EnterClusters(cluster)

   def EnterCluster3(self):
      self.go_previous_page(self.Time_Sleep_object)
      cluster = self.GetClusterSelector(3)
      self.EnterClusters(cluster)


