from ctypes import string_at
from io import StringIO
from pyshadow.main import Shadow
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium.webdriver import ActionChains




"""
/**
 ?                          THIS CLASS REPRESENTS THE PARENT CLASS FOR ALL PAGES
*/"""

### it contains all the generic methods and utilities for ALL pages ###

@pytest.mark.usefixtures("api_token_init" )
class BasePage:

    ############################# CONSTRUCTOR ###################################

    def __init__(self, driver):
        self.driver = driver
        self.shadow = Shadow(driver)
        self.actions = ActionChains(driver)

    ############################## ACTIONS #####################################
    def scroll_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def frame_switch(self, frame_element):
        self.driver.switch_to_frame(frame_element)

    def get_object(self, by_locator):
        object = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return object

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator)).click()

    def do_shadow_click(self, locator):
        element = self.find_shadow_element(locator)
        if(self.shadow.is_visible(element)):
            element.click()

    def do_jsclick(self, path):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,path)))    
        self.driver.execute_script("arguments[0].click();",element)

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_shadow_send_keys(self, locator, text):
        element = self.find_shadow_element(locator)
        if(self.shadow.is_visible(element)):
            element.send_keys(text)

    def implicit_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element_tag(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def quit_browser(self, driver):
        return driver.quit()

    def find_shadow_element(self, element):
        shadow = Shadow(self.driver)
        element = shadow.find_element(element)
        return element

    def implicit_wait(self, seconds):
        shadow = Shadow(self.driver)

        shadow.set_implicit_wait(seconds)
    
    def get_shadow_element_childs(self, element):
        shadow = Shadow(self.driver)
        elements = shadow.get_child_elements(element)
        return elements

    def get_all_shadow_element(self, locator1, locator2):
        shadow = Shadow(self.driver)
        element = self.find_shadow_element(locator1)
        ele = shadow.get_shadow_element(element,locator2)
        return ele

    def select_shadow_checkbox(self, label):
        shadow = Shadow(self.driver)
        shadow.select_checkbox(label)

    def do_switch_to(self, tab):
        self.driver.switch_to_window(self.driver.window_handles[tab])
    
    def find_elements(self, xpath):
        all_elements = self.driver.find_elements_by_xpath(xpath)
        for element in all_elements:
            return element
    
    def do_right_click(self, by_locator):
        source = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))
        self.actions.context_click(source).perform()
        
    def get_text(self,by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))
        text = element.text
        return text

    def get_elements_text(self, by_locator):
        texts = []
        matched_elements = self.driver.find_elements_by_xpath(by_locator)
        for matched_element in matched_elements:
            if not matched_element:
                continue 
            text = matched_element.text
            texts.append(text)
        return texts
    
    def go_previous_page(self,by_locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))
        self.driver.execute_script("window.history.go(-1);")
    
    def Wait_for_Existence(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))

       
        
    

    

    
        
        
