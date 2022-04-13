import time
from resources.jupyter_api import Jupyter_Api
import pytest
from POM.config import TestData
from selenium.webdriver.common.by import By
from POM.BasePage import BasePage
from resources.jupyter_api import KF_config_init



"""
/**
 ?   ------------------------------------------THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN THE JUPYTER HUB PAGE--------------------------------------------------     
*/"""

@pytest.mark.usefixtures("KF_config_init")
class JupyterHub(BasePage):

 ##################################################################   OBJECT SELECTORS   ####################################################################
    TerminalButton = (By.XPATH,"(//div[@class='jp-LauncherCard'])[5]")
    Terminal = (By.XPATH,"(//div[@class='terminal xterm jp-Terminal-body'])")
    FileUpload = (By.XPATH,"//button[@title='Upload Files']")
    NewFile = (By.XPATH,"(//li[starts-with(@title, 'Name: toot.txt')])")
    Open = (By.XPATH,"(//li[@class='lm-Menu-item p-Menu-item'])[1]") 
    NewTab = (By.XPATH,"(//div[@class='lm-TabBar-tabLabel p-TabBar-tabLabel'])[7]")
    Canvas = (By.XPATH,"//div[@class='terminal xterm jp-Terminal-body']")

 ##################################################################   OBJECT SELECTORS   ####################################################################
    def __init__(self, driver):
        super().__init__(driver)

    # def RunCommand_1(self):       # AC-7793
    #     self.do_click(self.TerminalButton)
    #     time.sleep(3)
    #     pyautogui.write(TestData.Command_1, interval=0.01)
    #     pyautogui.press('enter')
    #     time.sleep(1)
    #     pyautogui.write("y", interval=0.01)
    #     pyautogui.press('enter')
    #     pyautogui.write(TestData.ServiceAccount, interval=0.01)
    #     pyautogui.press('enter')    
    #     pyautogui.write(TestData.ServicePassword, interval=0.01)
    #     pyautogui.press('enter')
    #     pyautogui.write(TestData.Namespace, interval=0.01)
    #     pyautogui.press('enter')
    #     pyautogui.write(TestData.NamespacePW, interval=0.01)
    #     pyautogui.press('enter')
    #     pyautogui.write(TestData.Environment, interval=0.01)
    #     pyautogui.press('enter')

    def RunCommand_2(self):
        self.do_click(self.TerminalButton)
        time.sleep(3)
        # pyautogui.write(TestData.Command_2_1, interval=0.01)
        # pyautogui.press('enter')
        time.sleep(1)
            
    def CreateFile(self):
        self.Jupyter_Api = Jupyter_Api()
        self.Jupyter_Api.send_notebook_command(TestData.ServerName, "echo some-text  > filename.txt ")

    # create a patern that actually works, send notebooks commands when not directly subclassed

    # upload file from local
    def UploadFile(self):
        self.do_click(self.FileUpload)
        time.sleep(3)
        # pyautogui.write(TestData.FilesPath, interval=0.01) 
        # pyautogui.press('enter')
        time.sleep(2)
    
    def OpenFile(self):
        self.do_right_click(self.NewFile)
        self.do_click(self.Open)

    def GetResponse(self):
        return self.get_element_text(self.Canvas)

    # source control
    
    

        


    



    

    


            
        





