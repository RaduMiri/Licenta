from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

#Options prevents browser from closing, doesn't work
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

service = Service(executable_path="chromedriver.exe")#, chrome_options=options) 
driver = webdriver.Chrome(service=service)

driver.get("https://www.e-licitatie.ro/pub/notices/contract-notices/list/17/1")

def click_class(class_name):
    try:
        WebDriverWait(driver, 10).until( 
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))) 
        time.sleep(1)
    except:
        pass
    else:
        driver.find_element(By.CLASS_NAME, class_name).click()
        time.sleep(1)
        
def click_XPATH(xpath):
    try:
        WebDriverWait(driver, 10).until( 
            EC.element_to_be_clickable((By.XPATH, xpath)))
        time.sleep(1)
    except:
        pass
    else:
        driver.find_element(By.XPATH, xpath).click

#Datapicker locations
publication_start_date_XPATH = '//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[2]/div[4]/div/div[1]/div[1]/span/span/input'
publication_end_date_XPATH = '//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[2]/div[4]/div/div[2]/div[1]/span/span/input'
submit_deadline_start_date_XPATH = '//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[3]/div[4]/div/div[1]/div[1]/span/span/input'
submit_deadline_end_date_XPATH = '//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[3]/div[4]/div/div[2]/div[1]/span/span/input'

#Datapicker elements
WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.XPATH, publication_start_date_XPATH)))

publication_start_date = driver.find_element(By.XPATH, publication_start_date_XPATH)
publication_end_date = driver.find_element(By.XPATH, publication_end_date_XPATH)
submit_deadline_start_date = driver.find_element(By.XPATH, submit_deadline_start_date_XPATH)
submit_deadline_end_date = driver.find_element(By.XPATH, submit_deadline_end_date_XPATH)

calendar1 = driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[2]/div[4]/div/div[1]/div[1]/span/span/span')

# Input the desired date using JavaScript
def input_start_dates(desired_date):
    publication_start_date.clear()
    driver.execute_script(f"arguments[0].value = '{desired_date}';", publication_start_date)
    # driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", publication_start_date)
    calendar1.click()
    print(driver.find_element(By.CLASS_NAME,'k-state-selected k-state-focused'))
    #\36 062a74d-11c2-42b2-85d8-d7305814eb06_cell_selected
    # try:
    #     WebDriverWait(driver, 10).until( 
    #         EC.element_to_be_clickable((By.CLASS_NAME,'k-state-selected k-state-focused'))) 
    # except:
    #     pass
    # else:
    #     driver.find_element(By.CLASS_NAME,'k-state-selected k-state-focused').find_element(By.XPATH, '*').click()
        # "//a[@title='Tutorialspoint']"
        
        
    # driver.find_element(By.CLASS_NAME,'k-state-selected k-state-focused').find_elements(By.XPATH, '*').click()
    submit_deadline_start_date.clear()
    driver.execute_script(f"arguments[0].value = '{desired_date}';", submit_deadline_start_date)
    # driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", submit_deadline_start_date)

    
def input_end_dates(desired_date):
    publication_end_date.clear()
    driver.execute_script(f"arguments[0].value = '{desired_date}';", publication_end_date)
    # driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", publication_end_date)
    submit_deadline_end_date.clear()
    driver.execute_script(f"arguments[0].value = '{desired_date}';", submit_deadline_end_date)
    # driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", submit_deadline_end_date)

day, month, year = '21', '04', '2019'
desired_date = f"{day}/{month}/{year}"
# desired_date = f"{year}/{month}/{day}"

# publication_start_date.clear()
# publication_end_date.clear()
# driver.execute_script(f"arguments[0].value = '{desired_date}';", publication_start_date)
# driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", publication_start_date)
# driver.execute_script(f"arguments[0].value = '{desired_date}';", publication_end_date)
# driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", publication_end_date)


time.sleep(1)
input_start_dates(desired_date)
time.sleep(1)
input_end_dates(desired_date)

# click_class("pull-right.margin-left-5.btn.btn-entity") #Filtreaza

time.sleep(150)
driver.quit()