import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
URL = "http://localhost:8000/app/host_detail?user_id=1&host_id=71434784298&ticket_id=1#traces"
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
wait   = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="content"]/div/div[3]/div/div[1]/div/div/button/span')))
hover = ActionChains(driver).move_to_element(button[0])
hover.perform()
tooltip = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.MuiTooltip-popper')))
# Si se ha encontrado el tooltip, significa que ha aparecido al hacer hover
if tooltip:
    print("El tooltip ha aparecido al hacer hover.")
else:
    print("El tooltip no ha aparecido al hacer hover.")

time.sleep(40)



