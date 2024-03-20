import unittest
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Functions.Func import Global_Functions

URL = "http://localhost:8000/app/home?user_id=1&ticket_id=1"
wait_time = 2
class Page_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_user_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("User Info"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/div/div/div/div[1]/div[1]/div[1]/h6', wait_time)
        print("The User Info section was load correctly")

    def test_team_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Team Info"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/div[2]/div[1]/div[1]/h6', wait_time)
        print("The Team Info section was load correctly")
    
    def test_Subscriptions(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Subscriptions"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/div[2]/nav/ul/li[1]/a', wait_time)
        print("The Subscriptions section was load correctly")

    def test_Account_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Account"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/div/div/nav/ul/li[1]/a', wait_time)
        print("The Account section was load correctly")

    def test_Apps_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Apps"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/div/div/nav/ul/li[1]/a', wait_time)
        print("The Apps section was load correctly")

    def test_Quotas_N_Discounts_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Quotas & Discounts"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/div/div/nav/ul/li[1]/a', wait_time)
        print("The Quotas & Dicounts section was load correctly")
    
    def test_Restores_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Restores"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/nav/ul/li[1]/a', wait_time)
        print("The Restores section was load correctly")

    def test_Paper_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Paper"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/nav/ul/li[1]/a', wait_time)
        print("The Paper section was load correctly")
    
    def test_adminExtras_info(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("/admin Extras"))]', wait_time)
        f.xpath_exists('//*[@id="content"]/div/div/nav/ul/li[1]/a', wait_time)
        print("The /admin Extras section was load correctly")
    
    def test_elemt_exists(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_click('//div/a[contains(text(),("Account"))]', wait_time)
        f.xpath_exists('//div/button[contains(@class, "MuiButtonBase-root")]', wait_time)
    
    def test_sidebar(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        f.launch_explorer(URL)
        f.xpath_exists('//*[@id="root"]/div[2]/div/div/div/div[2]/a', wait_time)
        print("The Siebar content was displayed correctly")
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[2]/div[2]/div[2]/button/span', wait_time)
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button/span', wait_time)
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[2]/div[13]/div[2]/div/button/span', wait_time)
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[2]/div[14]/div[2]/div/button/span', wait_time)
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[2]/div[15]/div[2]/div/button/span', wait_time)
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[2]/div[16]/div[2]/div/button/span', wait_time)
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[2]/div[17]/div[2]/div/button/span', wait_time)
        f.copy_button_val('//*[@id="root"]/div[2]/div/div/div/div[3]/div[3]/div[2]/button/span', wait_time)
        f.xpath_click('//*[@id="root"]/div[2]/div/div/div/div[2]/a', wait_time)
        f.xpath_exists('//*[@id="content"]/div/div/nav/ul/li[1]/a', wait_time)
        print("User Info section was loaded")
        f.xpath_click('//*[@id="root"]/div[2]/div/div/div/div[3]/a', wait_time)
        f.xpath_exists('//*[@id="content"]/nav/ul/li[1]/a', wait_time)
        print("Team Info section was loaded")
        f.xpath_click('//*[@id="root"]/div[2]/div/div/div/div[4]/a', wait_time)
        f.xpath_exists('//*[@id="content"]/div/div/nav/ul/li[3]/a', wait_time)
        print("Family Info tab was loaded")

    def test_host_details(self):
        driver  = self.driver
        f       = Global_Functions(driver)
        try:
            f.launch_explorer(URL)
            f.xpath_click('//div/a[contains(text(),("User Info"))]', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div/div/div[1]/div[1]/div[1]/h6', wait_time)
            print("User Info page was loaded")
            f.xpath_click('//*[@id="content"]/div/div/div/div[1]/div[3]/div/div/div/table/tbody/tr[2]/td[2]/a/span', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[1]/div[1]/div/div', wait_time)
            print("Host & Devices details page are displayed correctly and the breadcrumb are displayed")
            f.xpath_click('//*[@id="content"]/div/nav/ul/li[1]/a', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[3]/div/div[2]/div[1]/div[1]/h6', wait_time)
            f.xpath_click('//*[@id="content"]/div/nav/ul/li[3]/a', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[3]/div/div[1]/div[1]/h6', wait_time)
            f.xpath_click('//*[@id="content"]/div/nav/ul/li[5]/a', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[3]/p', wait_time)
            f.xpath_click('//*[@id="content"]/div/nav/ul/li[6]/a', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[3]/p', wait_time)
            f.xpath_click('//*[@id="content"]/div/nav/ul/li[7]/a', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[3]/div/div[1]/div[1]/h6', wait_time)
            print("The tabs from the Host details page are working well")
            f.xpath_click('//*[@id="content"]/div/nav/ul/li[1]/a', wait_time)
            f.xpath_exists('/html/body/div[4]/div[3]/div/div[1]/h5', wait_time)
            print("The modal was displayed well")
            f.hover_xpath('//*[@id="content"]/div/div[3]/div/div[1]/div/div/button/span','.MuiTooltip-popper', wait_time)
            f.xpath_click('//*[@id="content"]/div/nav/ul/li[1]/a', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[3]/div/div[2]/div[1]/div[1]/h6', wait_time)
            f.xpath_click('//*[@id="content"]/div/div[3]/div/div[2]/div[3]/div/div/div/table/tbody/tr[2]/td[6]/a/span', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[1]/div[1]/div/div/div', wait_time)
            print("The both bread crumbs are displyed well")
            driver.back()
            f.xpath_click('//*[@id="content"]/div/div[1]/div[1]/div/div',wait_time)
            try:
                for i in range(1, 7):
                    f.xpath_exists('//*[@id="menu-"]/div[3]/ul/li['+str(i)+']', wait_time)
                print("The list of bradcrumbs are displayed well")
            except TimeoutException as ex:
                print("the element was no located")
            f.xpath_click('//*[@id="menu-"]/div[3]/ul/li[1]',wait_time)
            driver.back()
            f.xpath_click('//*[@id="content"]/div/div[3]/div/div[2]/div[3]/div/div/div/table/tbody/tr[2]/td[6]/a/span', wait_time)
            f.xpath_exists('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div', wait_time)
            f.xpath_click('//*[@id="content"]/div/div[1]/div[3]/div/div/div', wait_time)
            try:
                for i in range(1, 7):
                    f.xpath_exists('//*[@id="menu-"]/div[3]/ul/li['+str(i)+']', wait_time)
                print("The list of bradcrumbs are displayed well")
            except TimeoutException as ex:
                print("the element was no located")
            f.xpath_click('//*[@id="menu-"]/div[3]/ul/li[3]',wait_time)
            f.xpath_exists('//*[@id="content"]/div/nav/ul/li[5]/a', wait_time)
            print("The breadcrums from Trace details are working well")
        except TimeoutException as ex:
                print("the element was no located")
    def tearDown(self):
        driver=self.driver
        driver.close()
        

if __name__ == '__main__':
    unittest.main()