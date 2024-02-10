from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
language_id = "langSelect-EN"
cookies_amount_id = "cookies"

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@id='langSelect-EN']"))
)

language = driver.find_element(By.ID, language_id)
language.click()

WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)

#buying new product
productPrice_id = "productPrice"
while True:
    for i in range(25):
        cookie.click();
    
    cookies_amount_string = driver.find_element(By.ID, cookies_amount_id).text.split(" ")[0]    
    cookies_amount = int(cookies_amount_string.replace(",", ""))
    
    for i in range(4):      
        productPrice_string = driver.find_element(By.ID, productPrice_id + str(i)).text.split(" ")[0]
    
        if not productPrice_string:  # Dize boşsa devam et
            continue
    
        # Dize boş değilse dönüşüm yap
        productPrice_int = int(productPrice_string.replace(",", ""))
        
        productPrice_btn = driver.find_element(By.ID, "product" + str(i))

        if productPrice_int <= cookies_amount:
            productPrice_btn.click()


    if cookies_amount > 2500:
        break




time.sleep(120)

driver.quit()