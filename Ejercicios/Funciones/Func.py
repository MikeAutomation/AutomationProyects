import time
import unittest


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class Funciones_Glob():

        def __init__(self, driver):
                self.driver = driver
        
        def saludos(self):
                print("Bienvenido a Page Object Model")