import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        
    
    def test_1(self):
        d=self.driver
        d.get("http://localhost:8000/app/home?user_id=1")
        time.sleep(5)
        #case 1: Validate if the button exists in screen
        print("Case 1: Validate if the button exists in screen")
        d.maximize_window()
        wait = WebDriverWait(d, 20)
        account = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div/a[contains(text(),("Account"))]')))
        account[0].click()
        disconnect = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div/button[contains(@class, "MuiButtonBase-root")]')))
        #Verify the button displayed
        if disconnect:
            disconnect_button = disconnect[0]
            if disconnect_button.is_displayed():
                result = "Discconnect button was displayed disabled correctly."
            else:
                result = "Discconnect button was not displayed disabled."
            print(result)
        else:
            print("Discconnect button was not displayed disabled correctly.")
        # Check if the button is enabled (not disabled)
        if "Discconnect button was displayed disabled correctly." in result:
            hover = ActionChains(d).move_to_element(disconnect_button)
            hover.perform()
            tooltip = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@title,"You do not have Agent permissions to perform this action.")]')))
    
    def test_2(self):
        d=self.driver
        d.get("http://localhost:8000/app/home?user_id=1")
        time.sleep(5)
        #case 1: Validate if the button exists in screen
        print("Case 1: Validate if the button exists in screen")
        d.maximize_window()
        wait = WebDriverWait(d, 20)
        account = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div/a[contains(text(),("Account"))]')))
        account[0].click()
        disconnect = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div/button[contains(@class, "MuiButtonBase-root")]')))
        #Verify the button displayed
        if disconnect:
            disconnect_button = disconnect[0]
            if disconnect_button.is_displayed():
                result = "Discconnect button was displayed disabled correctly."
            else:
                result = "Discconnect button was not displayed disabled."
            print(result)
        else:
            print("Discconnect button was not displayed disabled correctly.")
        # Check if the button is enabled (not disabled)
        if "Discconnect button was displayed disabled correctly." in result:
            hover = ActionChains(d).move_to_element(disconnect_button)
            hover.perform()
            tooltip = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@title,"You do not have Agent permissions to perform this action.")]')))

    def tearDown(self):
        d=self.driver
        d.close()


if __name__ == '__main__':
    unittest.main()