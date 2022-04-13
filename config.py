import datetime
import os
import namegenerator
######################## SETTINGS THAT SERVE AS INFO FOR THE EXECUTION OF ALL TESTS ###########################

class TestData:

    CHROME_EXECUTABLE_PATH = "chromedriver.exe"
    BASE_URL = "https://workbench-us-qa.lower-pwclabs.pwcglb.com/"
    KUBEFLOW_URL = "https://dstools-kf-qa.np-pwclabs.pwcglb.com"
    CreateServer = "https://dstools-kf-qa.np-pwclabs.pwcglb.com/jupyter/new"
    Email = "bautista.f.gaggiotti@pwc.com"
    
    ############################## FILE UPLOAD ############################################
    FilesPath = "C:\\Users\\bgaggiotti001\\Desktop\\Bautista\\DataFiles\\SPAMSMS (1).ipynb"
    FileName = "toot.txt"
    ############################## FILE UPLOAD ############################################
    
    # FileName = FilesPath.split("\\",1)[1]
    
    ############################## PWC LABS CONFIG - AC-7793 ############################################
    # Command_1 = "pwclabs config"
    # ServiceAccount = "us_xlos_13d78abf-68aa-4fbf-8a38-265a0924cec4_s001"
    # ServicePassword = "U4IaDmpJo9BMsmfxERA8"
    # Namespace = "8982a90c-7f5c-487e-a25c-43a18aff6cc6"  #already on the conftest file
    # NamespacePW = "z8kmpagwynbu7488g16t"
    # Environment = "US-UDEV"
    ############################## PWC LABS CONFIG - AC-7793 ############################################

    ServerName = namegenerator.gen(separator='-')

    ############################## AC-12015 ############################################
    Command_2_1 = "pip show labs-sdk-python"
    Command_2_2 = "pip show jupyterlab"
    ############################## AC-12015 ############################################

    clusters = ("US-AI-AKS-QA","US-AI-AKS-QA-Kubeflow","US-AI-AKS-STG","US-AI-AKS-STG-Kubeflow") 
    CumulativeTitle = "Cumulative cost for last 7 days by cluster"
    
    PipelineDes = namegenerator.gen(separator='-')





    def getDriverPath(self):
        print('--------------DEBUGKEY-----------')
        print(os.listdir())
        if os.name == "posix":
            return "chromedriver"
        else:
            return "chromedriver.exe"


    
    
    




