import unittest
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Global_Functions():

        def __init__(self, driver):
                self.driver = driver
        
        def launch_explorer(self, URL):
                driver  = self.driver
                driver.get(URL)
                driver.maximize_window()
                print("The explorer was excecute")
        
        def xpath_click (self, xpath, wait_time):
                try:
                    driver  = self.driver
                    wait    = WebDriverWait(driver, wait_time)
                    elemnet = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
                    elemnet[0].click()
                    print("The click action as performed")
                    return 1
                except TimeoutException as ex:
                    print("The element was not located")

        def xpath_exists (self, xpath, wait_time):
                try:
                    driver = self.driver
                    wait   = WebDriverWait(driver, wait_time)
                    element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
                    #Verify the element is displayed
                    if element:
                        element = element[0]
                        if element.is_displayed():
                            result = "The element was displayed correctly."
                        else:
                            result = "The element was not displayed."
                        print(result)
                    else:
                        print("The element was not displayed.")
                    return 1
                except TimeoutException as ex:
                        print ("The elemnt was not located")
        
        def copy_button_val (self, xpath, wait_time):
                try:
                    driver = self.driver
                    wait   = WebDriverWait(driver, wait_time)
                    #Verify the previous content
                    previous_content = pyperclip.paste()
                    elemnet = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
                    elemnet[0].click()
                    time.sleep(wait_time)
                    #Verify the current content
                    current_content = pyperclip.paste()
                    if previous_content != current_content:
                        print("The copy function is working well, Content: " + str(current_content))
                    else:
                        print("The content was not copyed")
                except TimeoutException as ex:
                    print("The button was not located")
              
        def hover_xpath (self, xpath, tooltip, wait_time):
                try:
                    driver = self.driver
                    wait   = WebDriverWait(driver, wait_time)
                    button = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
                    hover = ActionChains(driver).move_to_element(button[0])
                    hover.perform()
                    tooltip = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, tooltip)))
                    # Si se ha encontrado el tooltip, significa que ha aparecido al hacer hover
                    if tooltip:
                        print("Tooltip was displayed when made hover")
                    else:
                        print("Tooltip was not displayed when made hover")
                except TimeoutException as ex:
                    print("The elemnt was not located")
                    


                