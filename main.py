from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("/Users/jonida/Desktop/Udemy/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
INCREMENT = 5
timeout = time.time() + 5
five_mins = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for item in items[::-1]:
            try:
                if not item.get_attribute("class"):
                    item.click()
            except:
                items = driver.find_elements(By.CSS_SELECTOR, "#store div")

        timeout = time.time() + INCREMENT
        INCREMENT = INCREMENT + 1

    if time.time() > five_mins:
        cookies_per_s = driver.find_element(By.ID, "cps").text
        print(cookies_per_s)
        break

driver.quit()
