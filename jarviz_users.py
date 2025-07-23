import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# STEP 1: โหลดข้อมูล Excel
df = pd.read_excel("/Users/Documents/jarviz_test.xlsx", dtype={'phone': str})  # Your file path

# STEP 2: เตรียม Selenium
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("/opt/homebrew/bin/chromedriver")  # path 
driver = webdriver.Chrome(service=service, options=chrome_options)

# STEP 3: Login
driver.get("https://jarvizweb.jarvizapp.com/login")
time.sleep(1)

driver.find_element(By.ID, "input-19").send_keys("Company_Code")      # Your Company Code
driver.find_element(By.ID, "input-22").send_keys("UserID")            # Your UserID
driver.find_element(By.ID, "input-25").send_keys("Password")          # Your Password
driver.find_element(By.XPATH, "//span[text()='Login']").click()
time.sleep(3)

# STEP 4: เข้าหน้า user management
driver.get("https://jarvizweb.jarvizapp.com/dashborad/users")
time.sleep(2)

# STEP 5: Loop กรอกข้อมูลพนักงานจาก Excel
for i, row in df.iterrows():
    driver.find_element(By.XPATH, "//button[contains(text(),'New Employee')]").click()

    driver.find_element(By.ID, "inputEmpID").send_keys(str(row['emp_id']))

    # ช่อง Full Name (ไม่มี ID → ใช้ class + index)
    driver.find_elements(By.CLASS_NAME, "form-control")[1].send_keys(row['full_name'])

    driver.find_element(By.ID, "inputEmail").send_keys(row['email'])

    # ช่อง Position (ไม่มี ID → ใช้ class + index)
    driver.find_elements(By.CLASS_NAME, "form-control")[3].send_keys(row['position'])

    driver.find_element(By.ID, "inputphoneno").send_keys(str(row['phone']))

    driver.find_element(By.ID, "inputuID").clear()   # ลบค่า default
    driver.find_element(By.ID, "inputuID").send_keys(row['emp_id']) 

    # คลิกปุ่ม Add
    driver.find_element(By.XPATH, "//button[contains(text(),'Add')]").click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    time.sleep(2) 

driver.quit()
