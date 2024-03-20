import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
URL = "http://localhost:8000/app/subscriptions?user_id=1&ticket_id=1&tab=user_subscriptions#subscriptions"
driver=webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get(URL)
driver.maximize_window()

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='Search by keyword']")))
search.click()
search.send_keys("email john.doe@dropbox.com")
search.send_keys(Keys.ENTER)
search = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-active,'true')]")))
search.click()
time.sleep(30)
print("Bienvenido")
print(driver.title)

driver.close()
